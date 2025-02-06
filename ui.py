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
    agent_option = "Classic"  # Valeur par défaut
    if selected_option == "Chatbot":

        st.sidebar.button('Clear Chat', on_click=clear_chat_history)

        # Sélectionner l'agent
        agent_option = st.sidebar.selectbox("Choose Agent", ["Classic", "SEO"], key="selected_agent")



        # Menu déroulant pour choisir un modèle (en dessous du bouton Clear Chat)
        selected_model = st.sidebar.selectbox('Choose a model', ['llama2-7b', 'llama2-13b', 'llama2-70b'],
                                              key='selected_model')

        # Mise à jour du pré-prompt selon l'agent sélectionné
        if agent_option == "SEO":
            st.session_state.pre_prompt = """
            I am creating an SEO-optimized article on the following topic: [Insert the main topic here, for example "How to improve website SEO"].

            Here are the requirements I want you to follow when writing the article:
            - Title: Suggest an engaging and SEO-optimized title that includes the main keywords related to the topic.
            - Keywords: Use secondary keywords throughout the article.
            - Structure: Organize the article with relevant subheadings (H2, H3).
            - Conclusion: Write a conclusion that encourages action, using keywords.
            """
        else:
            st.session_state.pre_prompt = "Hi, I'm an assistant. How can I help you today?"

        # Réinitialiser l'historique des messages
        if "messages" in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": st.session_state.pre_prompt}]

    elif selected_option == "Settings":
        st.sidebar.markdown("### API Token")
        replicate_api = st.sidebar.text_input('Enter API token:', type='password', key='replicate_api_token')

        # Température
        st.sidebar.markdown("### Temperature")
        temperature = st.sidebar.slider("Set temperature", 0.0, 1.0, 0.1, 0.1)
        st.session_state.temperature = temperature  # Enregistrer la température dans la session

    elif selected_option == "About":
        st.sidebar.markdown("### About")
        st.sidebar.markdown("Interact with different Llama models🦙\n\n Enter your Replicate API token in the settings to get started🚀 ")

        st.sidebar.markdown('<hr>', unsafe_allow_html=True)

        # Button for redirecting to GitHub with a white logo and no border
        github_button_html = """
            <a href="https://github.com/MatthieuGillieron/chatbot" target="_blank" class="github-button">
                <button style="background-color: #0E1117; color: white; border: none; border-radius: 12px; padding: 10px 15px; display: flex; align-items: center; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo" width="20" height="20" style="margin-right: 10px; filter: invert(1);">
                    GitHub
                </button>
            </a>
        """
        st.sidebar.markdown(github_button_html, unsafe_allow_html=True)

    return replicate_api, llm, agent_option
