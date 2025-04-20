import streamlit as st
import os
from styles import get_css
from session import initialize_session
from ui import create_sidebar, display_chat, handle_user_input
from model_utils import generate_response

def main():
    st.set_page_config(page_title="CHATBOT-AI", layout="wide")
    
    st.markdown(get_css(), unsafe_allow_html=True)
    
    initialize_session()
    
    create_sidebar()
    
    if st.session_state.replicate_api_token:
        os.environ['REPLICATE_API_TOKEN'] = st.session_state.replicate_api_token
    
    display_chat()
    
    handle_user_input(generate_response)

if __name__ == "__main__":
    main()