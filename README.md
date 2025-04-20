# 🤖 AI Chatbot - English Version

[![English](https://img.shields.io/badge/English-yellow.svg)](./README.md)  [![Français](https://img.shields.io/badge/Français-gray.svg)](./doc/READMEfr.md)

<p align="center">
  <img src=".streamlit/thumbnail.png" alt="Chatbot Thumbnail" width="500">
</p>
---

### 📝 Description

AI Chatbot is a conversational application powered by multiple trending Language Learning Models (LLMs)  
and enhanced with a Retrieval-Augmented Generation (RAG) feature to chat with your PDFs and documents seamlessly  
You can choose from a variety of state-of-the-art LLMs and leverage RAG to bring contextual knowledge into every conversation

Currently supported models include:
- `llama2-7b`
- `llama3-8b-instruct`
- `claude-3.7-sonnet`
- `deepseek-r1`
- `llama2-70b`

Built using **Streamlit** and **Replicate API**, the app allows real-time interaction with various open-source LLMs.

---

### ▶️ Try the Chatbot Live

 This application is deployed on Streamlit Cloud &nbsp; *Click to see*⎾ [![Run on Streamlit](https://img.shields.io/badge/Streamlit-Demo-orange?logo=streamlit)](https://chatbot-ia.streamlit.app)

---

### 📦 Prerequisites

1. [Create a free Replicate account](https://replicate.com)
2. Get your **Replicate API key** from your profile
3. [Optional] Set up a local environment if testing locally

---

### ⚙️ Installation (Local)

```bash
git clone https://github.com/MatthieuGillieron/chatbot.git
cd chatbot
pip install -r requirements.txt
streamlit run app.py
```

Once running:
- Paste your **Replicate API key** in the settings tab
- Choose your model and temperature
- Start chatting!

---

### 🧠 Features

- Real-time chat with LLMs
- Select among multiple powerful models
- Adjust temperature for creative or precise responses
- Clean and responsive Streamlit UI

---

### 🛡️ Security Note

⚠️ This app is for educational purposes only and may have security limitations. Use with caution.

---

### 📄 License

Licensed under the [MIT License](./doc/LICENSE)

---

### 🌟 Contribute

If you like the project, give it a ⭐ on GitHub!  
Feel free to fork, improve, or submit pull requests.

