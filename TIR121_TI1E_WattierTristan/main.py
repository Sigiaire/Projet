from file_read import lines_from_file
from getters import get_host, get_complete_date, get_message, get_program

file = lines_from_file(r"TIR121_TI1E_WattierTristan\log\syslog.log")

# for i in range(50):
#     print(f"\n{i+1}\n")
#     print(f"{get_host(file[i])}")
#     print(f"{get_complete_date(file[i])}")
#     print(f"{get_message(file[i])}")
#     print(f"{get_program(file[i])}")

print(get_host(file[0]))
print(get_complete_date(file[0]))
print(get_message(file[0]))
print(get_program(file[0]))