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
    date = " ".join(split_line[0:3])
    return date

def get_message(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le message de la ligne
            !!! le message peut être composé de sous messages (séparés pas d’autres « : »),
                dans ce cas, il faut tout
    """
    split_line = line.split(":",3)
    message = split_line[-1]
    return message
    
def get_program(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le nom du programme
    """
    split_line = line.split("[", 2)
    split_line = split_line[0].split()
    program = split_line[4]
    program = program[:-1] if program.endswith(":") else program
    return program
    
def get_process_id(line):
    """ Pre : line est une ligne de log bien formée (str)
        Post : Retourne le numéro du processus. Si aucun id n’est disponible
            (dans le cas d’un kernel par exemple), -1 est retourné.
    """
    try:
        program = get_program(line) # On va tester si le programme est un kernel
        if program == "kernel":
            process_id = -1
            return process_id
        else:
            split_line = line.split("[")
            split_line = split_line[1].split("]")
            process_id = split_line[0].split()
            return int(float(process_id[0])) if int(float(process_id[0])) > 0 else -1
    except (IndexError, ValueError):
        process_id = -1
        return process_id