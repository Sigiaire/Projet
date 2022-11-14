def lines_from_file(path):
    """ Pre : path (str) est le chemin menant au fichier à lire
            (à partir du dossier courant)
         Post : Retourne une liste où chaque élément est une ligne du fichier.
            En cas d'erreur, retourne une liste vide
    """
    try :
        with open(path) as file:
            log = file.readlines()
            return log
        
    except Exception as e :
        print(e)
        return []