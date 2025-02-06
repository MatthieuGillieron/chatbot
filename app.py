import streamlit as st
import replicate
import os
from ui import create_sidebar 


st.set_page_config(page_title="CHATBOT-IA", layout="wide")

# effacer l'historique du chat
def clear_chat_history():

    if 'agent_option' in st.session_state:
        if st.session_state.agent_option == "SEO":
            st.session_state.messages = [{"role": "assistant", "content": st.session_state.pre_prompt_seo}]
        else:
            st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    else:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Init sidebar et recup. param
replicate_api, llm, agent_option = create_sidebar(st.session_state.get('replicate_api_token', None), None, clear_chat_history)

# Configurer key
if replicate_api:
    os.environ['replicate_api_token'] = replicate_api

# Stocker les réponses générées par LLM
if "messages" not in st.session_state:
    # Si agent SEO est choisi, appliquer le pré-prompt SEO comme message initial
    if agent_option == "SEO":
        st.session_state.messages = [{"role": "assistant", "content": st.session_state.pre_prompt_seo}]
    else:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Afficher messages du chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Générer une réponse
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant."
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "assistant"
        string_dialogue += f"\n{role}: {msg['content']}"

    
    temperature = st.session_state.get('temperature', 0.1)

    output = replicate.run(llm, input={"prompt": f"{string_dialogue}\nassistant: {prompt_input}", "temperature": temperature})
    return output


# entrée user
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Générer la réponse
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(st.session_state.messages[-1]["content"])
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
