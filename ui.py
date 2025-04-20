import streamlit as st
from streamlit_option_menu import option_menu

def create_sidebar(replicate_api, llm, clear_chat_history):
    st.markdown("""
        <style>
            .sidebar .stButton > button {
                margin: 0 auto;
                width: 90px;
                font-size: 12px;
            }
            .sidebar hr {
                margin: 15px 0;
                border: none;
                border-top: 1px solid #ccc;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        selected_option = option_menu(
            menu_title="IA BOT",
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

        if "messages" in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Hi, I'm an assistant. How can I help you today?"}]

    elif selected_option == "Settings":
        st.sidebar.markdown("### API Token")
        replicate_api = st.sidebar.text_input('Enter API token:', type='password', key='replicate_api_token')

        st.sidebar.markdown("### Temperature")
        temperature = st.sidebar.slider("Set temperature", 0.0, 1.0, 0.1, 0.1)
        st.session_state.temperature = temperature

    elif selected_option == "About":
        st.sidebar.markdown("### About")
        st.sidebar.markdown("Interact with different Llama models🦙\n\nEnter your Replicate API token in the settings to get started🚀")
        st.sidebar.markdown('<hr>', unsafe_allow_html=True)

        github_button_html = """
            <a href="https://github.com/MatthieuGillieron/chatbot" target="_blank" class="github-button">
                <button style="background-color: #0E1117; color: white; border: none; border-radius: 12px; padding: 10px 15px; display: flex; align-items: center; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo" width="20" height="20" style="margin-right: 10px; filter: invert(1);">
                    GitHub
                </button>
            </a>
        """
        st.sidebar.markdown(github_button_html, unsafe_allow_html=True)

    return replicate_api, llm
