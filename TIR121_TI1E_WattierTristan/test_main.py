import main

# tests sur get basiques
def test_get_host():
    assert main.get_host("Moi JJ HH:MM:SS host program[process_id]: message") == "host"

def test_get_message():
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message") == " message"
def test_get_composed_message1():
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message : sous-message") == " message : sous-message"
def test_get_composed_message2():
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message : sous-message : sous-message : sous-message : sous-message") == " message : sous-message : sous-message : sous-message : sous-message"

def test_get_program_with_process_id():
    assert main.get_program("Moi JJ HH:MM:SS host program[process_id]: message") == "program"
def test_get_program_without_process_id():
    assert main.get_program("Moi JJ HH:MM:SS host program: message") == "program"

def test_get_exist_process_id():
    assert main.get_process_id("Moi JJ HH:MM:SS host program[10]: message") == 10
def test_get_not_exist_process_id():
    assert main.get_process_id("Moi JJ HH:MM:SS host program: message") == -1

def test_get_complete_date():
    assert main.get_complete_date("Moi JJ HH:MM:SS host program[10]: message") == "Moi JJ HH:MM:SS"
