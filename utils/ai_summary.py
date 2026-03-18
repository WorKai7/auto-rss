import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("La clé API OPENROUTER_API_KEY n'est pas définie")

prompt = "Voici un texte censé représenter un article, si c'est écrit que l'article est disponible en pdf et qu'il n'y a pas d'article écrit directement, réponds moi 'Article disponible sur le site', si l'article est écrit alors tu ne m'écris pas que l'article est dispo sur le site ok ? c'est que si c'est juste écrit un truc comme 'dispo en pdf' fais moi un résumé de celui ci comme si tu écrivais un article mais en plus court. Puis a la fin du message, toujours si l'article est écrit, ajoute '(Résumé généré par IA)', voici le texte : "


def ai_summary(text: str):
    try:
        print("Generating AI summary...")
        response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "stepfun/step-3.5-flash:free",
            "messages": [
                {
                "role": "user",
                "content": prompt + text
                }
            ]
        }),
        verify=False
        )

        response = response.json()
        print(response)
        response = response['choices'][0]['message']['content']

        print("Done.")

        return response

    except:
        print("Erreur de génération du résumé")
        return "Erreur de génération du résumé"