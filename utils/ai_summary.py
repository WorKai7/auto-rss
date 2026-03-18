import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("La clé API OPENROUTER_API_KEY n'est pas définie")


def ai_summary(text: str):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "google/gemma-3n-e4b-it:free",
        "messages": [
            {
            "role": "user",
            "content": "Fais moi un résumé de cet article comme si tu écrivais le même article mais plus court, tout en un seul paragraphe, puis à la fin de l'article rajoute '(Résumé généré par IA)': " + text
            }
        ]
    }),
    verify=False
    )

    response = response.json()
    response = response['choices'][0]['message']['content']

    return response


text = """
Un projet pionnier au service de la transition énergétique bas carbone du Royaume-Uni 
La conception-construction de l’infrastructure principale
Un contrat d’une valeur de 200 millions £ (environ 230 millions d’euros)

UK Fusion Energy (anciennement UK Industrial Fusion Solutions) a retenu le groupement ILIOS* dirigé par Nuvia, filiale de VINCI Construction spécialisée dans les projets et services dans le domaine du nucléaire, pour la conception et la construction des infrastructures du programme STEP Fusion** dans le Nottinghamshire au Royaume-Uni. 

UK Fusion Energy est un partenariat industriel financé par l'État britannique, conçu pour développer d’ici à 2040 un prototype de centrale capable de produire de l’électricité à partir d’énergie de fusion.

Le contrat, d’une durée de 4,5 ans et d’un montant de 200 millions de livres (environ 230 millions d’euros, dont 50 % pour Nuvia), porte sur la phase 1 du projet. Elle comprend la conception et la construction de l’ensemble des bâtiments, des infrastructures et des installations du site. 

Ce projet majeur témoigne de l’expertise reconnue de VINCI Construction dans les grands projets d’infrastructures d’énergie, notamment de fusion. On rappellera que les entreprises de VINCI Construction sont actuellement engagées sur le projet ITER (International Thermonuclear Experimental Reactor) - l’un des plus ambitieux programmes internationaux de recherche sur la fusion - en cours de construction à Cadarache en France.  

 

* Le groupement ILIOS est composé de Nuvia, Kier, AECOM, AL_A et Turner & Townsend

** Spherical Tokamak for Energy Production
"""

print(ai_summary(text))