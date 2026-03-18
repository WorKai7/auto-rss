correspondance = {
    "janvier": "01",
    "février": "02",
    "fevrier": "02",
    "mars": "03",
    "avril": "04",
    "mai": "05",
    "juin": "06",
    "juillet": "07",
    "août": "08",
    "aout": "08",
    "septembre": "09",
    "octobre": "10",
    "novembre": "11",
    "décembre": "12",
    "decembre": "12"
}

def parse_date(date: str):
    date_split = date.split(" ")
    
    jour_int = int(date_split[0])
    jour = "0" if jour_int < 10 else ""
    jour += date_split[0]
    mois = correspondance[date_split[1]]
    annee = date_split[2]

    parsed_date = jour + "." + mois + "." + annee

    return parsed_date

print(parse_date("10 mars 2022"))