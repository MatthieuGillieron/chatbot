import streamlit as st
import replicate
import os
from streamlit_option_menu import option_menu
from styles import get_css, get_github_button
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import tempfile

st.set_page_config(page_title="CHATBOT-AI", layout="wide")

st.markdown(get_css(), unsafe_allow_html=True)


def initialize_session():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you today?"}]
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.1
    if "replicate_api_token" not in st.session_state:
        st.session_state.replicate_api_token = ""
    if "pdf_mode" not in st.session_state:
        st.session_state.pdf_mode = False
    if "pdf_vectorstore" not in st.session_state:
        st.session_state.pdf_vectorstore = None
    if "pdf_name" not in st.session_state:
        st.session_state.pdf_name = ""


def clear_chat_history():
    """Clear the chat history"""
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you today?"}]


def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        tmp_file_path = tmp_file.name
    
    text = ""
    with open(tmp_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    
    os.unlink(tmp_file_path)
    return text


def create_vector_store(text):
    """Create a vector store from the PDF text"""
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Create embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embeddings)
    
    return vectorstore


def process_pdf():
    """Process uploaded PDF file and create vector store"""
    # Utiliser une clé unique pour le file_uploader
    uploaded_file = st.sidebar.file_uploader("Upload your PDF", type="pdf", key="pdf_uploader")
    
    # Vérifier si un fichier est téléchargé ET qu'il n'a pas encore été traité
    if uploaded_file is not None and (st.session_state.pdf_name != uploaded_file.name):
        # First show a message in the sidebar
        processing_placeholder = st.sidebar.empty()
        processing_placeholder.info("Processing PDF... Please wait.")
        
        # Use the main area for the spinner
        with st.spinner("Processing PDF..."):
            # Extract text from PDF
            pdf_text = extract_text_from_pdf(uploaded_file)
            
            # Create vector store
            vectorstore = create_vector_store(pdf_text)
            
            # Store in session state
            st.session_state.pdf_vectorstore = vectorstore
            st.session_state.pdf_name = uploaded_file.name
            st.session_state.pdf_mode = True
            
            # Replace the processing message with success message
            processing_placeholder.empty()
            st.sidebar.success(f"PDF processed: {uploaded_file.name}")
            
            # Clear chat history when new PDF is uploaded
            st.session_state.messages = [{"role": "assistant", 
                                         "content": f"I've processed '{uploaded_file.name}'. What would you like to know about it?"}]
            # Use st.rerun() to refresh the UI
            st.rerun()


def search_pdf(query):
    """Search the PDF for relevant content based on the query"""
    if st.session_state.pdf_vectorstore:
        results = st.session_state.pdf_vectorstore.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in results])
        return context
    return ""


def generate_response(prompt_input):
    """Generate response based on selected model"""
    selected_model = st.session_state.get('selected_model', 'llama2-7b')
    
    models = {
        'llama2-7b': 'meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0',
        'llama3-8b-instruct': 'meta/meta-llama-3-8b-instruct',
        'claude-3.7-sonnet': 'anthropic/claude-3.7-sonnet',
        'deepseek-r1': 'deepseek-ai/deepseek-r1',
        'llama2-70b': 'meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3'
    }
    
    llm = models.get(selected_model, models['llama2-7b'])

    try:
        if st.session_state.pdf_mode:
            # If in PDF mode, search for relevant content
            context = search_pdf(prompt_input)
            
            string_dialogue = f"""You are a helpful assistant analyzing a PDF document titled '{st.session_state.pdf_name}'.
Use ONLY the following context from the document to answer the user's question.
If you don't find the answer in the context, say that you don't know based on the provided document.
Don't make up information that's not in the context.

CONTEXT:
{context}

CHAT HISTORY:
"""
        else:
            string_dialogue = "You are a helpful assistant."
            
        # Add chat history
        for msg in st.session_state.messages:
            role = "user" if msg["role"] == "user" else "assistant"
            string_dialogue += f"\n{role}: {msg['content']}"

        temperature = st.session_state.get('temperature', 0.1)

        output = replicate.run(llm, input={"prompt": f"{string_dialogue}\nassistant: {prompt_input}", "temperature": temperature})
        return output
    except Exception as e:
        st.error(f"Error while generating the response: {str(e)}")
        return "Sorry, an error occurred. Please check your configuration and try again"


def create_sidebar():
    """Create and manage sidebar UI elements"""
    with st.sidebar:
        selected_option = option_menu(
            menu_title="AI BOT",
            options=["Chatbot", "Chat with PDF", "Settings", "About"],
            icons=["chat", "file-pdf", "gear", "info-circle"],
            menu_icon="cast",
            default_index=0,
        )
    
    if selected_option == "Chatbot":
        st.session_state.pdf_mode = False
        st.sidebar.button('Clear Chat', on_click=clear_chat_history)

        selected_model = st.sidebar.selectbox(
            'Choose a model',
            ['llama2-7b', 'llama3-8b-instruct', 'claude-3.7-sonnet', 'deepseek-r1', 'llama2-70b'],
            key='selected_model'
        )

    elif selected_option == "Chat with PDF":
        st.sidebar.markdown("### Upload PDF")
        process_pdf()
        
        if st.session_state.pdf_mode:
            st.sidebar.success(f"Active PDF: {st.session_state.pdf_name}")
            if st.sidebar.button('Clear PDF and Chat'):
                st.session_state.pdf_vectorstore = None
                st.session_state.pdf_name = ""
                st.session_state.pdf_mode = False
                clear_chat_history()
                st.rerun()
        
        selected_model = st.sidebar.selectbox(
            'Choose a model',
            ['llama2-7b', 'llama3-8b-instruct', 'claude-3.7-sonnet', 'deepseek-r1', 'llama2-70b'],
            key='selected_model'
        )

    elif selected_option == "Settings":
        st.sidebar.markdown("### Replicate Token")
        # Use the stored token as the default value
        token_input = st.sidebar.text_input(
            'Enter your API token:', 
            type='password',
            value=st.session_state.replicate_api_token, 
            key='token_input'
        )
        
        # Update token in session state
        if token_input:
            st.session_state.replicate_api_token = token_input
        
        st.sidebar.markdown("### Temperature")
        temperature = st.sidebar.slider(
            "Set the temperature", 
            0.0, 1.0, 
            value=st.session_state.temperature,
            step=0.1
        )
        st.session_state.temperature = temperature

    elif selected_option == "About":
        st.sidebar.markdown("### About")
        st.sidebar.markdown("Interact with different trending LLM models🤖\n\nEnter your Replicate API token in the settings to get started🚀")
        st.sidebar.markdown('<hr>', unsafe_allow_html=True)
        st.sidebar.markdown(get_github_button(), unsafe_allow_html=True)


# Main execution

# Initialize session state
initialize_session()

# Setup sidebar
create_sidebar()

# Set API token from session state
if st.session_state.replicate_api_token:
    os.environ['REPLICATE_API_TOKEN'] = st.session_state.replicate_api_token

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle user input - disabled if no token
if prompt := st.chat_input(disabled=not st.session_state.replicate_api_token):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt)
                st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})