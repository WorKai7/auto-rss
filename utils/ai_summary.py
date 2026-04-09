import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("La clé API OPENROUTER_API_KEY n'est pas définie")

prompt = "Voici un texte censé représenter un article ou autre chose, si c'est écrit que l'article est disponible en pdf et qu'il n'y a pas d'article écrit directement, réponds moi 'Article disponible uniquement sur le site', si l'article est écrit alors tu ne m'écris pas que l'article est dispo sur le site ok ? c'est que si c'est juste écrit un truc comme 'dispo en pdf' fais moi un résumé de celui ci comme si tu écrivais un article mais en plus court genre vraiment pas long si possible 3-4 phrases. Même si c'est une assemblée générale ou peu importe, tant qu'il y a du texte que tu peux résumer, résume le. Et pour ce qui est des acronymes, tu peux également écrire leur signification si elle est indiquée dans l'article. Tu n'as pas le droit d'inventer des informations, tu dois uniquement utiliser ce qui est présent dans le texte fourni. Le résumé doit être propre et à but journalistique, tu dois alors uniquement faire le résumé et n'ajouter aucune phrase inutile. Voici le texte : "


def ai_summary(text: str, prompt: str = prompt):
    try:
        print("Generating AI summary...")
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "nvidia/nemotron-3-super-120b-a12b:free",
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
        # print(response)
        response = response['choices'][0]['message']['content']

        print("Done.")

        return response

    except:
        print("Erreur de génération du résumé")
        return "Erreur de génération du résumé"
    

# print(ai_summary("exceptionnel", "Combien y a-t-il de e dans ce texte: "))