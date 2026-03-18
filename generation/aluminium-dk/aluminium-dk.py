import requests
import os
import re
from bs4 import BeautifulSoup

# Import grâce au package utils
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils.start_xml_file import start_file
from utils.end_xml_file import end_file
from utils.write_xml import write_xml

os.chdir(os.path.dirname(__file__))


# Connexion au site
base_url = "https://www.aluminiumdunkerque.fr/actualites/"

print("\n\nScrapping", base_url, "\n\n")

try:
    response = requests.get(base_url, verify=False)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Erreur HTTP:", e)
    exit(1)

# Instanciation de soup
soup = BeautifulSoup(response.text, "html.parser")

articles = []

images_divs = soup.find_all("div", class_="post_image")
dates = soup.find_all("time", class_="post_date")
titres = soup.find_all("h2", class_="post_title")
links = soup.find_all("a", class_="w-text-h")
descriptions = soup.find_all("div", class_="post_content")


for i in range(len(images_divs)):

    # Limite de 10 articles
    if i < 10:
        article = {}

        link = links[i].get("href")

        img = [image for image in images_divs[i].children][0]

        article["Titre"] = titres[i].get_text(" ", strip=True)
        article["Date"] = dates[i].get("datetime")
        article["Image"] = img.get("src")
        article["Lien"] = link
        article["Description"] = descriptions[i].get_text(strip=True)


        articles.append(article)


# Ecriture

start_file(
    "aluminium-dk/actu.rss",
    "Flux RSS actualités Aluminium DK",
    "https://workai7.github.io/auto-rss/rss/aluminium-dk/actu.rss",
    "Flux RSS contenant les informations sur les actualités du site de Aluminium DK, généré par un script de scrapping",
    base_url
)

for article in articles:
    write_xml(
        "aluminium-dk/actu.rss",
        article["Titre"],
        article["Description"],
        article["Image"],
        article["Lien"],
        article["Date"]
    )

end_file("aluminium-dk/actu.rss")


print("\nDone\n")