def get_css():
    """Renvoie les styles CSS pour l'application"""
    return """
        <style>
            .sidebar .stButton > button {
                margin: 0 auto;
                width: 90px;
                font-size: 12px;
            }
            .sidebar hr {
                margin: 15px 0;
                border: none;
                border-top: 1px solid #ccc;
            }
            
            /* Styles pour les messages */
            .chat-container {
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
            }
            
            .user-message {
                background-color: #e6f7ff;
            }
            
            .assistant-message {
                background-color: #f0f0f0;
            }
        </style>
    """

def get_github_button():
    """Renvoie le code HTML pour le bouton GitHub"""
    return """
        <a href="https://github.com/MatthieuGillieron/chatbot" target="_blank" class="github-button">
            <button style="background-color: #0E1117; color: white; border: none; border-radius: 12px; padding: 10px 15px; display: flex; align-items: center; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub Logo" width="20" height="20" style="margin-right: 10px; filter: invert(1);">
                GitHub
            </button>
        </a>
    """