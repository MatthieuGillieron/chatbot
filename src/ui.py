import streamlit as st
from streamlit_option_menu import option_menu
from styles import get_github_button
from session import clear_chat_history, set_api_token
from pdf_utils import process_pdf, clear_pdf_data

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
        uploaded_file = st.sidebar.file_uploader("Upload your PDF", type="pdf", key="pdf_uploader")
        
        if process_pdf(uploaded_file):
            st.rerun()
        
        if st.session_state.pdf_mode:
            st.sidebar.success(f"Active PDF: {st.session_state.pdf_name}")
            if st.sidebar.button('Clear PDF and Chat'):
                clear_pdf_data()
                clear_chat_history()
                st.rerun()
        
        selected_model = st.sidebar.selectbox(
            'Choose a model',
            ['llama2-7b', 'llama3-8b-instruct', 'claude-3.7-sonnet', 'deepseek-r1', 'llama2-70b'],
            key='selected_model'
        )

    elif selected_option == "Settings":
        st.sidebar.markdown("### Replicate Token")
        token_input = st.sidebar.text_input(
            'Enter your API token:', 
            type='password',
            value=st.session_state.replicate_api_token, 
            key='token_input'
        )
        
        set_api_token(token_input)
        
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

def display_chat():
    """Display chat messages from session state"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def handle_user_input(generate_response_function):
    """Handle user input and generate response"""
    if prompt := st.chat_input(disabled=not st.session_state.replicate_api_token):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response_function(prompt)
                    st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})