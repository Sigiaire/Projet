from file_read import lines_from_file
from getters import get_host, get_complete_date, get_message, get_program, get_process_id
from dates import logs_by_day, formated_date, logs_between

# from getters import get_host, get_complete_date, get_message, get_program, get_process_id
# from dates import logs_by_day, formated_date, logs_between

if __name__ == '__main__':
    file = lines_from_file(r"TIR121_TI1E_WattierTristan\log\syslog.log")
    
    
    
    
    print(get_host(file[1]))
    print(get_complete_date(file[1]))
    print(get_message(file[1]))
    print(get_program(file[1]))
    print(get_process_id(file[1]))
    
    print(logs_by_day(file, "Oct 26"))
    print(formated_date("Oct 26 00:00:00"))
    print(logs_between(file, "Oct 26 00:00:00"))
    
# for i in range(5000):
#     print(f"\n=============================\n======LIGNE NUMÉRO {i+1}======\n=============================")
#     print(f"===HOST===  {get_host(file[i])}")
#     print(f"===DATE===  {get_complete_date(file[i])}")
#     print(f"===MESSAGE===  {get_message(file[i])}")
#     print(f"===PROGRAMME===  {get_program(file[i])}")
#     print(f"===PROCESS_ID===  {get_process_id(file[i])}")