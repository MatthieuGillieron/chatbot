# Chatbot IA - Version Française

[![English](https://img.shields.io/badge/English-gray.svg)](../README.md)  [![Français](https://img.shields.io/badge/Français-yellow.svg)](./READMEfr.md)  

<p align="center">
  <img src="../.streamlit/thumbnail.png" alt="Chatbot Thumbnail" width="500">
</p>

---

### 📝 Description

Chatbot IA est une application conversationnelle alimentée par plusieurs modèles de langage (LLMs) tendance,
complétée par une fonctionnalité de RAG (Retrieval-Augmented Generation) pour discuter avec vos fichiers PDF et documents de manière fluide.

Vous pouvez sélectionner parmi une variété de modèles performants et tirer parti du RAG pour enrichir les réponses avec du contexte réel.

Modèles actuellement pris en charge :
- `llama2-7b`
- `llama3-8b-instruct`
- `claude-3.7-sonnet`
- `deepseek-r1`
- `llama2-70b`

Développé avec **Streamlit** et l'API **Replicate**, ce chatbot permet une interaction en temps réel avec différents LLMs open source.

---

### ▶️ Tester le Chatbot en Ligne

<p align="center">
  <a href="https://chatbot-ia.streamlit.app">
    <img src="https://img.shields.io/badge/Streamlit-Demo-orange?logo=streamlit" alt="Streamlit Demo">
  </a>
</p>

<p align="center">
  *Cette application est déployée sur Streamlit Cloud et se met à jour automatiquement à chaque push GitHub.*
</p>

---

### 📦 Prérequis

1. [Créez un compte gratuit sur Replicate](https://replicate.com)
2. Récupérez votre **clé API Replicate** depuis votre profil
3. [Facultatif] Configurez un environnement local pour les tests

---

### ⚙️ Installation (Locale)

```bash
git clone https://github.com/MatthieuGillieron/chatbot.git
cd chatbot
pip install -r requirements.txt
streamlit run src/app.py
```

Une fois l'application lancée :
- Collez votre **clé API Replicate** dans l'onglet des paramètres
- Choisissez votre modèle et la température
- Commencez à discuter !

---

### 🧠 Fonctionnalités

- Chat en temps réel avec des LLMs
- Sélection de plusieurs modèles puissants
- Réglage de la température pour des réponses plus créatives ou précises
- Interface propre et réactive via Streamlit

---

### 🛡️ Sécurité

⚠️ Cette application est à but éducatif et peut comporter des limitations de sécurité. À utiliser avec prudence.

---

### 📄 Licence

Ce projet est sous licence [MIT](./doc/LICENSE)

---

### 🌟 Contribuer

Si vous appréciez le projet, laissez une ⭐ sur GitHub !
N'hésitez pas à forker, améliorer ou soumettre une pull request
