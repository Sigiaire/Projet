def get_host(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le hostname
    """
    split_line = line.split()
    return split_line[3]
    
def get_complete_date(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne la date et l’heure sous forme de chaine de caractère
            sans changer le format.
    """
    split_line = line.split()
    return split_line[2]

def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le message de la ligne
            !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
                dans ce cas, il faut tout
    """
    if ":" in line:
        split_line = line.split(":")
        return ":".join(split_line[3:])