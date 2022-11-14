from file_read import lines_from_file
from getters import get_host, get_complete_date, get_message

file = lines_from_file(r"TIR121_TI1E_WattierTristan\log\syslog.log")

print(get_host(file[0]))
print(get_complete_date(file[0]))
print(get_message(file[2]).strip("[ ]"))