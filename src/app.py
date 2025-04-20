import streamlit as st
import replicate
import os
from streamlit_option_menu import option_menu
from styles import get_css, get_github_button

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


def clear_chat_history():
    """Clear the chat history"""
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you today?"}]


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
        string_dialogue = "You are a helpful assistant."
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
            options=["Chatbot", "Settings", "About"],
            icons=["chat", "gear", "info-circle"],
            menu_icon="cast",
            default_index=0,
        )
    
    if selected_option == "Chatbot":
        st.sidebar.button('Clear Chat', on_click=clear_chat_history)

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
        
        # Update the token in session state when input changes
        if token_input:
            st.session_state.replicate_api_token = token_input

        st.sidebar.markdown("### Temperature")
        temperature = st.sidebar.slider("Set the temperature", 0.0, 1.0, 0.1, 0.1)
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