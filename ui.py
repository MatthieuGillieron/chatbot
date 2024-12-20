import streamlit as st
from streamlit_option_menu import option_menu


def create_sidebar(replicate_api, llm, clear_chat_history):
    # Personnalisation du style
    st.markdown("""
        <style>
            .sidebar .stButton > button {
                margin: 0 auto;  /* Centrer le bouton */
                width: 90px;  /* Largeur personnalisée */
                font-size: 12px;  /* Ajuster la taille */
            }
            .sidebar hr {
                margin: 15px 0;  /* Espacement au-dessus et en dessous */
                border: none;
                border-top: 1px solid #ccc;
            }

        </style>
    """, unsafe_allow_html=True)

    # Sidebar : Menu principal
    with st.sidebar:
        selected_option = option_menu(
            menu_title="IA BOT",  # Titre du menu
            options=["Chatbot", "Settings", "About"],  # Options
            icons=["chat", "gear", "info-circle"],  # Icônes
            menu_icon="cast",  # Icône principale
            default_index=0,  # Option sélectionnée par défaut
        )

    # Afficher les options du chatbot
    if selected_option == "Chatbot":
        # Ajouter une séparation
        st.sidebar.button('Clear Chat', on_click=clear_chat_history)

        # Menu déroulant pour choisir un modèle
        selected_model = st.sidebar.selectbox('Choose a model', ['llama2-7b', 'llama2-13b', 'llama2-70b'],
                                              key='selected_model')

        # Configuration du modèle en fonction de la sélection
        if selected_model == 'llama2-7b':
            llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
        elif selected_model == 'llama2-13b':
            llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
        else:
            llm = 'replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48'

    elif selected_option == "Settings":
        st.sidebar.markdown("### API Token")
        replicate_api = st.sidebar.text_input('Enter API token:', type='password', key='replicate_api_token')

        # Ajout du slider pour la température
        temperature = st.sidebar.slider('Temperature', min_value=0.01, max_value=1.0, value=0.5, step=0.01)
        st.session_state['temperature'] = temperature  # Stocker la température dans la session

    elif selected_option == "About":
        st.sidebar.markdown("### About")
        st.sidebar.markdown(
            "Interact with different Llama models🦙\n\n Enter your Replicate API token in the settings to get started🚀 ")

        st.sidebar.markdown('<hr>', unsafe_allow_html=True)

        # Button for redirecting to GitHub
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
