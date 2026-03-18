from email.utils import format_datetime
from datetime import datetime

correspondance = {
    "janvier": "January",
    "février": "February",
    "fevrier": "February",
    "mars": "March",
    "avril": "April",
    "mai": "May",
    "juin": "June",
    "juillet": "July",
    "août": "August",
    "aout": "August",
    "septembre": "September",
    "octobre": "October",
    "novembre": "November",
    "décembre": "December",
    "decembre": "December"
}

def parse_date(date: str):
    date_split = date.split(" ")
    
    jour_int = int(date_split[0])
    jour = "0" if jour_int < 10 else ""
    jour += date_split[0]
    mois = correspondance[date_split[1].lower()]
    annee = date_split[2]

    translated_date = jour + " " + mois + " " + annee

    parsed_date = datetime.strptime(translated_date, "%d %B %Y")
    parsed_date = format_datetime(parsed_date)

    return parsed_date