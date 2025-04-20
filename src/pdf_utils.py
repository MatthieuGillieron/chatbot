import os
import streamlit as st
import PyPDF2
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        tmp_file_path = tmp_file.name
    
    text = ""
    with open(tmp_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    
    os.unlink(tmp_file_path)
    return text

def create_vector_store(text):
    """Create a vector store from the PDF text"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embeddings)
    
    return vectorstore

def process_pdf(uploaded_file):
    """Process uploaded PDF file and create vector store"""
    if uploaded_file is not None and (st.session_state.pdf_name != uploaded_file.name):
        processing_placeholder = st.sidebar.empty()
        processing_placeholder.info("Processing PDF... Please wait.")
        
        with st.spinner("Processing PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            
            vectorstore = create_vector_store(pdf_text)
            
            st.session_state.pdf_vectorstore = vectorstore
            st.session_state.pdf_name = uploaded_file.name
            st.session_state.pdf_mode = True
            
            processing_placeholder.empty()
            st.sidebar.success(f"PDF processed: {uploaded_file.name}")
            
            st.session_state.messages = [{"role": "assistant", 
                                         "content": f"I've processed '{uploaded_file.name}'. What would you like to know about it?"}]
            return True
    return False

def search_pdf(query):
    """Search the PDF for relevant content based on the query"""
    if st.session_state.pdf_vectorstore:
        results = st.session_state.pdf_vectorstore.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in results])
        return context
    return ""

def clear_pdf_data():
    """Clear all PDF-related data from session state"""
    st.session_state.pdf_vectorstore = None
    st.session_state.pdf_name = ""
    st.session_state.pdf_mode = False