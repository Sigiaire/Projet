from file_read import lines_from_file
from getters import get_host, get_complete_date, get_message, get_program, get_process_id
from dates import logs_by_day, formated_date, logs_between

# from getters import get_host, get_complete_date, get_message, get_program, get_process_id
# from dates import logs_by_day, formated_date, logs_between

def logs_with_tag(logs, tag="error"):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - tag est une chaine de caractères à trouver dans le message.
            Par défaut : "error"
    Post :
        - retourne une liste de logs qui concernent uniquement des logs
            contenant le tag (minuscule ou majuscule) dans le message
    """
    error_logs = []
    
    for log_line in logs:
        if tag in log_line.lower():
            error_logs.append(log_line)
            
    return error_logs

def logs_from_program(logs, program):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - program (str) est le programme à trouver
    Post :
        - retourne une liste de logs qui concernent uniquement les programmes
            correspondant à "program"
    """
    program_logs = []
    
    for log_line in logs:
        log_program = get_program(log_line)
        if program in log_program:
            program_logs.append(log_line)
            
    return program_logs

def list_process_for_program(logs, program):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - program (str) est le programme à trouver
    Post :
        - retourne une liste des process_id gérés par le programme.
            La liste ne contient aucun doublon.
"""
    processes = []
    
    for log_line in logs:
        log_program = get_program(log_line)
        if program in log_program:
            process = get_process_id(log_line)
            if process not in processes:
                if process != -1 :
                    processes.append(process)
            
    return processes

def suspects(logs, limit):
    """ Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - limit est le nombre limite d'erreurs tolérées pour un programme
    Post :
        - retourne une liste des programmes (sans doublons) qui ont généré
            plus que le nombre limite de log signalant des erreurs (error).
    """
    suspects = []
    
    for log_line in logs:
        if "error" in log_line.lower():
            program = get_program(log_line)
            if program not in suspects:
                if len(logs_from_program(logs, program)) >= limit:
                    suspects.append(program)
            
    return suspects

if __name__ == '__main__':
    file = lines_from_file(r"TIR121_TI1E_WattierTristan\log\syslog.log")
    
    # print(get_host(file[1]))
    # print(get_complete_date(file[1]))
    # print(get_message(file[1]))
    # print(get_program(file[1]))
    # print(get_process_id(file[1]))
    
    # print(logs_by_day(file, "Oct 26"))
    # print(formated_date("Oct 26 00:00:00"))
    # print(logs_between(file, "Oct 26 00:00:00"))
    
    # print(logs_with_tag(file))
    # print(logs_from_program(file, "kernel"))
    
    print(list_process_for_program(file, "rtkit-daemon"))
    
# for i in range(5000):
#     print(f"\n=============================\n======LIGNE NUMÉRO {i+1}======\n=============================")
#     print(f"===HOST===  {get_host(file[i])}")
#     print(f"===DATE===  {get_complete_date(file[i])}")
#     print(f"===MESSAGE===  {get_message(file[i])}")
#     print(f"===PROGRAMME===  {get_program(file[i])}")
#     print(f"===PROCESS_ID===  {get_process_id(file[i])}")
#     print(f"===DATE_FORMATÉE===  {formated_date(get_complete_date(file[i]))}")
    