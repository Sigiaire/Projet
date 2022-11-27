def logs_by_day(logs, day):
    """
    Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - day (str) est une date au format « Moi JJ »
    Post :
        - retourne une liste de logs qui concernent uniquement le jour
            correspondant à day.
    """
    for log_line in logs:
        split_line = log_line.split()
        date = " ".join(split_line[0:2])
        if date == day:
            print(log_line)

def formated_date(date):
    """
        Pre : date (str) est la date au format "Mois JJ HH:MM:SS" où :
            - Mois : est les 3 première lettres du mois en anglais
                (commencant par une majuscule)
            - JJ : est le numéro du jour (sur 2 chiffres)
            - HH : est l'heure (sur 2 chiffres)
            - MM : sont les minutes (sur 2 chiffres)
            - SS : sont les secondes (sur 2 chiffres)
        Post : Retourne la date sous le format "XX:JJ HH:MM:SS"
            où XX est le nombre du mois (sur 2 chiffres)
    """
    months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    split_date = date.split()
    month = months[split_date[0]]
    day = split_date[1]
    time = split_date[2]
    return f"{month}:{day} {time}"