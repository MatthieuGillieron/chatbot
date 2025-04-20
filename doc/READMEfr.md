# Chatbot IA - Version Française

[![English](https://img.shields.io/badge/English-gray.svg)](../README.md)  [![Français](https://img.shields.io/badge/Français-yellow.svg)](./READMEfr.md)  

<p align="left">
  <img src="/images/chatbot_message.png" alt="Chatbot Screenshot" width="300" height="auto">
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="/images/setting.png" alt="Chatbot Screenshot" width="305" height="auto">
</p>


---
### Description :

Chatbot IA est un projet de chatbot intelligent qui permet d'utiliser différents modèles de Language Learning Models (LLM).  
Actuellement, le projet supporte **trois modèles Llama** :
- `llama2-7b`
- `llama2-13b`
- `llama2-70b`

Le projet comprend également une section **agent** *(en cours de développement)*. Pour l'instant, seul le pré-prompt a été modifié. Cette section sera destinée à utiliser un LLM entraîné sur une tâche précise (par exemple, un agent SEO, etc.).

---

### Prérequis :

Avant de pouvoir tester et utiliser ce projet, il est nécessaire de :

1. Créer un compte (gratuit) sur les plateformes suivantes :
   - [Streamlit](https://streamlit.io)
   - [Replicate](https://replicate.com)

2. Obtenir votre clé API Replicate :
   - Connectez-vous à votre compte Replicate
   - Allez dans les paramètres de votre compte
   - Copiez votre clé API

---

### Installation :

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/MatthieuGillieron/chatbot.git
   cd chatbot
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application :**
   ```bash
   streamlit run app.py
   ```

4. **Configuration :**
   - Dans l'application, allez dans l'onglet "Settings"
   - Entrez votre clé API Replicate
   - Ajustez la température selon vos préférences

---

### Utilisation :

1. Sélectionnez un modèle Llama 2 dans le menu déroulant
2. Choisissez le type d'agent (Classic ou SEO)
3. Commencez à discuter avec le chatbot
4. Utilisez le bouton "Clear Chat" pour réinitialiser la conversation

---

### Sécurité :

**Attention :** Ce projet est une expérimentation et peut contenir des failles de sécurité. Il a été réalisé dans un but d'apprentissage et d'entraînement. Utilisez-le en connaissance de cause.

---

### Contribuer :

Si vous clonez ou forkez ce dépôt, n'hésitez pas à laisser une étoile sur le dépôt pour soutenir le projet !
Toute contribution est la bienvenue.

---

### Remarques

- La section agent est encore en développement. Des améliorations et des fonctionnalités supplémentaires seront ajoutées prochainement.
- N'oubliez pas de vérifier régulièrement les mises à jour et la documentation pour profiter des dernières fonctionnalités.

---

### License :

Ce projet est sous licence [MIT](doc/./LICENSE).
