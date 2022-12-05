L_TEST = [
        "Jan 13 22:30:15 blabla",
        "Jan 14 23:30:15 blabla",
        "Jan 16 26:30:15 blabla",
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla"
    ]

for log_line in L_TEST: # la boucle for parcourt la liste logs et affecte à log_line chaque élément de la liste
        split_line = log_line.split() # split_line est une liste qui contient les éléments de log_line séparés par des espaces
        date = " ".join(split_line[0:2]) # date est une str qui contient les 2 premiers éléments de split_line
        print(date)
        if date == 'Jan 14': # si la date du log est égale au jour demandé
            print(log_line)