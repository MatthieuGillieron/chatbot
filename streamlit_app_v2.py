import streamlit as st
import replicate
import os
from ui import create_sidebar  # Importer la fonction mise à jour

# Configuration de l'application
st.set_page_config(page_title="CHATBOT-IA", layout="wide")


# Fonction pour effacer l'historique du chat
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]


# Initialiser la sidebar et récupérer les paramètres
replicate_api, llm = create_sidebar(st.session_state.get('replicate_api_token', None), None, clear_chat_history)

# Configurer la clé API
if replicate_api:
    os.environ['replicate_api_token'] = replicate_api

# Stocker les réponses générées par LLM
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Afficher les messages du chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Générer une réponse
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant."
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "assistant"
        string_dialogue += f"\n{role}: {msg['content']}"

    output = replicate.run(llm, input={"prompt": f"{string_dialogue}\nassistant: {prompt_input}", "temperature": 0.1})
    return output


# Boîte d'entrée utilisateur
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Générer la réponse de l'assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(st.session_state.messages[-1]["content"])
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
