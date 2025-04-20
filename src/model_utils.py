import streamlit as st
import replicate
from pdf_utils import search_pdf

def get_available_models():
    """Return dictionary of available models"""
    return {
        'llama2-7b': 'meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0',
        'llama3-8b-instruct': 'meta/meta-llama-3-8b-instruct',
        'claude-3.7-sonnet': 'anthropic/claude-3.7-sonnet',
        'deepseek-r1': 'deepseek-ai/deepseek-r1',
        'llama2-70b': 'meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3'
    }

def generate_response(prompt_input):
    """Generate response based on selected model"""
    selected_model = st.session_state.get('selected_model', 'llama2-7b')
    models = get_available_models()
    llm = models.get(selected_model, models['llama2-7b'])

    try:
        if st.session_state.pdf_mode:
            context = search_pdf(prompt_input)
            
            string_dialogue = f"""You are a helpful assistant analyzing a PDF document titled '{st.session_state.pdf_name}'.
Use ONLY the following context from the document to answer the user's question.
If you don't find the answer in the context, say that you don't know based on the provided document.
Don't make up information that's not in the context.

CONTEXT:
{context}

CHAT HISTORY:
"""
        else:
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