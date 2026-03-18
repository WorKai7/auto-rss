from utils.escape_xml import escape_xml
from utils.parse_date import parse_date

def write_xml(file: str, title: str, description: str, image: str, link: str, date: str, date_parse: bool = False):

    if date_parse:
        date = parse_date(date)

    with open(f"../../rss/{file}", "a", encoding="utf-8") as rss:
        print("Writing in", file)
        
        rss.write('\n        <item>\n')
        rss.write(f'            <title>{escape_xml(title)}</title>\n')
        rss.write(f'            <link>{escape_xml(link)}</link>\n')
        rss.write(f'            <description>{escape_xml(description)}</description>\n')
        rss.write(f'            <pubDate>{escape_xml(date)}</pubDate>\n')
        rss.write(f'            <enclosure url="{escape_xml(image)}" type="image/jpeg" />\n')
        rss.write('        </item>\n')