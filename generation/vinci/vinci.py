# import requests
# import os
# from bs4 import BeautifulSoup

# # Import grâce au package utils
# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parents[2]))

# from utils.start_xml_file import start_file
# from utils.end_xml_file import end_file
# from utils.write_xml import write_xml
# from utils.ai_summary import ai_summary


# os.chdir(os.path.dirname(__file__))


# # Connexion au site
# base_url = "https://www.vinci.com"

# # URL spécifique pour les communiques de presse : https://www.vinci.com/newsroom?f[0]=newsroom_content_type:communique
# #                                 Pour les actu : https://www.vinci.com/newsroom?f[0]=newsroom_content_type:actu

# url_list = []

# def scrap(url: str, category: str, file: str, first_page: bool = False, affichage: bool = False):
#     response = requests.get(url)
#     response.raise_for_status()

#     # Instanciation de soup
#     soup = BeautifulSoup(response.text, "html.parser")

#     if first_page:
#         pager_items = soup.find_all("li", class_="pager__item")
#         last_pager_item = [item for item in pager_items if item.get("class") == ["pager__item"] or item.get("class") == ["pager__item", "is-active"]][-1]
#         last_page_number = 0

#         for child in last_pager_item.children:
#             text = child.get_text(" ", strip=True)
#             if text:
#                 last_page_number = int(text[-1])

#         for i in range(1, last_page_number):
#             url_list.append(url + "&page=" + str(i))


#     # Recherche des divs qu'on a besoin
#     articles_divs = soup.find_all("article", class_=f"{category}-teaser")
#     titres = soup.find_all(class_=f"{category}-teaser__title")
#     images_divs = soup.find_all("div", class_=f"{category}-teaser__image")
#     details_divs = soup.find_all("div", class_=f"{category}-teaser__details")


#     articles = []

#     # Boucle sur chaque articles trouvé
#     for i in range(len(titres)):
#         article = {}

#         # Récupération des informations nécessaires
#         article_link = [child for child in articles_divs[i].children if child.name][0].get("href")
#         image = images_divs[i].find("img")
#         enfants = [child for child in details_divs[i].children if child.name]
#         date = enfants[-1]


#         # Alimentation du dictionnaire avec les données trouvées
#         article["Titre"] = titres[i].get_text(" ", strip=True)
#         article["Image"] = base_url + image.get("src")
#         article["Date"] = date.get_text(" ", strip=True)
#         article["Lien"] = base_url + article_link


#         articles.append(article)


#     # Affichage
#     if affichage:
#         for article in articles:
#             print("--------------------------------\n")
#             print("Titre :", article["Titre"])
#             print("Image :", article["Image"])
#             print("Categorie :", article["Categorie"])
#             print("Date :", article["Date"])
#             print("Pays :", article["Pays"])
#             print("Lien :", article["Lien"], "\n")



#     # Ecriture dans un fichier XML pour générer un flux RSS

#     # Boucle sur les articles
#     for article in articles:

#         # Description générée par IA
#         description = scrap_summary(article["Lien"])
        
#         write_xml(
#             file,
#             article["Titre"],
#             description,
#             article["Image"],
#             article["Lien"],
#             article["Date"]
#         )


#     print("Articles générés pour la page", url)


# def scrap_summary(url: str):
#     response = requests.get(url)
#     response.raise_for_status()

#     # Instanciation de soup
#     soup = BeautifulSoup(response.text, "html.parser")

#     important = soup.find(class_="pr-important")
#     article = soup.find("div", class_="paragraph__wrapper")

#     article_to_summarize = important.get_text(strip=True) if important else ""
#     article_to_summarize += article.get_text(strip=True)

#     summary = ai_summary(article_to_summarize)

#     return summary


# # ----- FICHIER PRESSE -----

# start_file(
#     "vinci/presse.rss",
#     "Flux RSS communiqués de presse VINCI",
#     "https://workai7.github.io/auto-rss/rss/vinci/presse.rss",
#     "Flux RSS contenant les informations sur les communiqués de presse du site de VINCI, généré par un script de scrapping",
#     base_url + "/newsroom?f[0]=newsroom_content_type:communique"
# )

# scrap(base_url + "/newsroom?f[0]=newsroom_content_type:communique", "pr", "vinci/presse.rss", True)

# for url in url_list:
#     scrap(url, "pr", "vinci/presse.rss")

# end_file("vinci/presse.rss")



# url_list.clear()


# # ----- FICHIER ACTU -----

# start_file(
#     "vinci/actu.rss",
#     "Flux RSS actualités VINCI",
#     "https://workai7.github.io/auto-rss/rss/vinci/actu.rss",
#     "Flux RSS contenant les informations sur les actualités du site de VINCI, généré par un script de scrapping",
#     base_url + "/newsroom?f[0]=newsroom_content_type:actu"
# )

# scrap(base_url + "/newsroom?f[0]=newsroom_content_type:actu", "actu", "vinci/actu.rss")

# for url in url_list:
#     scrap(url, "actu", "vinci/actu.rss")

# end_file("vinci/actu.rss")