import xml.etree.ElementTree as ET

def index_rss(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    index = {}

    for item in root.find("channel").findall("item"):
        title = item.find("title").text.strip()

        index[title] = {
            "title": title,
            "link": item.find("link").text,
            "description": item.find("description").text,
            "pubDate": item.find("pubDate").text,
            "image": item.find("enclosure").get("url") if item.find("enclosure") is not None else None
        }

    return index