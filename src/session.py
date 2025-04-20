import streamlit as st

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

def set_api_token(token):
    """Store API token in session state"""
    if token:
        st.session_state.replicate_api_token = token