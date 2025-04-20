# AI Chatbot - English Version

[![English](https://img.shields.io/badge/English-yellow.svg)](./READMEen.md)  [![Français](https://img.shields.io/badge/Français-gray.svg)](./README.md)  

<p align="left">
  <img src="/images/chatbot_message.png" alt="Chatbot Screenshot" width="300" height="auto">
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="/images/setting.png" alt="Chatbot Screenshot" width="305" height="auto">
</p>

---
### Description:

AI Chatbot is an intelligent chatbot project that allows the use of different Language Learning Models (LLM).  
Currently, the project supports **three Llama models**:
- `llama2-7b`
- `llama2-13b`
- `llama2-70b`

The project also includes an **agent section** *(under development)*. For now, only the pre-prompt has been modified. This section will be designed to use an LLM trained for a specific task (e.g., an SEO agent, etc.).

---

### Prerequisites:

Before testing and using this project, you need to:

1. Create a (free) account on the following platforms:
   - [Streamlit](https://streamlit.io)
   - [Replicate](https://replicate.com)

2. Obtain your Replicate API key:
   - Log in to your Replicate account
   - Go to your account settings
   - Copy your API key

---

### Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MatthieuGillieron/chatbot.git
   cd chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Configuration:**
   - In the application, go to the "Settings" tab
   - Enter your Replicate API key
   - Adjust the temperature according to your preferences

---

### Usage:

1. Select a Llama 2 model from the dropdown menu
2. Choose the agent type (Classic or SEO)
3. Start chatting with the chatbot
4. Use the "Clear Chat" button to reset the conversation

---

### Security:

**Warning:** This project is an experiment and may contain security vulnerabilities. It was created for learning and training purposes. Use it at your own risk.

---

### Contribute:

If you clone or fork this repository, feel free to leave a star on the repo to support the project!  
Any contribution is welcome.

---

### Notes:

- The agent section is still under development. Improvements and additional features will be added soon.
- Be sure to check for updates and documentation regularly to take advantage of the latest features.

---

### License :

his project is licensed under [MIT](doc/./LICENSE).