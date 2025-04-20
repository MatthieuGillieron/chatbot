import streamlit as st
import replicate
import os
from streamlit_option_menu import option_menu
from styles import get_css, get_github_button

# Configuration de la page
st.set_page_config(page_title="CHATBOT-IA", layout="wide")

# Chargement des styles CSS
st.markdown(get_css(), unsafe_allow_html=True)

# Initialisation des variables de session
def initialiser_session():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Comment puis-je vous aider aujourd'hui ?"}]
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.1

# Fonction pour effacer l'historique de chat
def effacer_historique_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Comment puis-je vous aider aujourd'hui ?"}]

# Fonction pour générer une réponse
def generer_reponse(prompt_input):
    selected_model = st.session_state.get('selected_model', 'llama2-7b')
    
    # Sélection du modèle approprié
    modeles = {
        'llama2-7b': 'meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0',
        'llama3-8b-instruct': 'meta/meta-llama-3-8b-instruct',
        'claude-3.7-sonnet': 'anthropic/claude-3.7-sonnet',
        'deepseek-r1': 'deepseek-ai/deepseek-r1',
        'llama2-70b': 'meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3'
    }
    
    llm = modeles.get(selected_model, modeles['llama2-7b'])

    try:
        string_dialogue = "Tu es un assistant utile."
        for msg in st.session_state.messages:
            role = "user" if msg["role"] == "user" else "assistant"
            string_dialogue += f"\n{role}: {msg['content']}"

        temperature = st.session_state.get('temperature', 0.1)

        output = replicate.run(llm, input={"prompt": f"{string_dialogue}\nassistant: {prompt_input}", "temperature": temperature})
        return output
    except Exception as e:
        st.error(f"Erreur lors de la génération de la réponse: {str(e)}")
        return "Désolé, une erreur s'est produite. Veuillez vérifier votre configuration et réessayer."

# Création de la barre latérale
def creer_sidebar():
    with st.sidebar:
        selected_option = option_menu(
            menu_title="IA BOT",
            options=["Chatbot", "Réglages", "À propos"],
            icons=["chat", "gear", "info-circle"],
            menu_icon="cast",
            default_index=0,
        )
    
    replicate_api = None
    
    if selected_option == "Chatbot":
        st.sidebar.button('Effacer Chat', on_click=effacer_historique_chat)

        selected_model = st.sidebar.selectbox(
            'Choisir un modèle',
            ['llama2-7b', 'llama3-8b-instruct', 'claude-3.7-sonnet', 'deepseek-r1', 'llama2-70b'],
            key='selected_model'
        )

    elif selected_option == "Réglages":
        st.sidebar.markdown("### Jeton API")
        replicate_api = st.sidebar.text_input('Entrer le jeton API:', type='password', key='replicate_api_token')

        st.sidebar.markdown("### Température")
        temperature = st.sidebar.slider("Régler la température", 0.0, 1.0, 0.1, 0.1)
        st.session_state.temperature = temperature

    elif selected_option == "À propos":
        st.sidebar.markdown("### À propos")
        st.sidebar.markdown("Interagissez avec différents modèles Llama🦙\n\nEntrez votre jeton API Replicate dans les réglages pour commencer🚀")
        st.sidebar.markdown('<hr>', unsafe_allow_html=True)
        st.sidebar.markdown(get_github_button(), unsafe_allow_html=True)

    return replicate_api

# Initialisation de la session
initialiser_session()

# Création de la barre latérale et récupération du jeton API
replicate_api = creer_sidebar()

# Configuration de l'API Replicate
if replicate_api:
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Affichage de l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Gestion de l'entrée utilisateur
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Réflexion en cours..."):
                response = generer_reponse(prompt)
                st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})