import main

# tests partie 1 : get basiques
def test_get_host():
    """ Test unitaire pour get_host """
    assert main.get_host("Moi JJ HH:MM:SS host program[process_id]: message") == "host"

def test_get_message():
    """ Test unitaire pour get_message """
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message") == " message"
def test_get_composed_message1():
    """ Test unitaire pour get_message (avec un sous message) """
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message : sous-message") == " message : sous-message"
def test_get_composed_message2():
    """ Test unitaire pour get_message (avec plein de sous message) """
    assert main.get_message("Moi JJ HH:MM:SS host program[process_id]: message : sous-message : sous-message : sous-message : sous-message") == " message : sous-message : sous-message : sous-message : sous-message"

def test_get_program_with_process_id():
    """ Test unitaire pour get_program (avec process id) """
    assert main.get_program("Moi JJ HH:MM:SS host program[process_id]: message") == "program"
def test_get_program_without_process_id():
    """ Test unitaire pour get_program (sans process id) """
    assert main.get_program("Moi JJ HH:MM:SS host program: message") == "program"

def test_get_exist_process_id():
    """ Test unitaire pour get_process_id (avec process id)) """
    assert main.get_process_id("Moi JJ HH:MM:SS host program[10]: message") == 10
def test_get_not_exist_process_id():
    """ Test unitaire pour get_process_id (sans process id) """
    assert main.get_process_id("Moi JJ HH:MM:SS host program: message") == -1

def test_get_complete_date():
    """ Test unitaire pour get_complete_date """
    assert main.get_complete_date("Moi JJ HH:MM:SS host program[10]: message") == "Moi JJ HH:MM:SS"

# tests partie 2 : dates
def test_formated_date_january():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Jan 18 22:30:15") == "01:18 22:30:15"
def test_formated_date_february():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Feb 18 22:30:15") == "02:18 22:30:15"
def test_formated_date_march():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Mar 28 22:30:15") == "03:28 22:30:15"
def test_formated_date_april():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Apr 08 22:30:15") == "04:08 22:30:15"
def test_formated_date_may():
    """ Test unitaire pour formated_date """
    assert main.formated_date("May 08 22:30:15") == "05:08 22:30:15"
def test_formated_date_june():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Jun 18 22:30:15") == "06:18 22:30:15"
def test_formated_date_july():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Jul 18 22:30:15") == "07:18 22:30:15"
def test_formated_date_august():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Aug 10 22:30:15") == "08:10 22:30:15"
def test_formated_date_september():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Sep 01 22:30:15") == "09:01 22:30:15"
def test_formated_date_november():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Nov 18 22:30:15") == "11:18 22:30:15"
def test_formated_date_october():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Oct 18 22:30:15") == "10:18 22:30:15"
def test_formated_date_december():
    """ Test unitaire pour formated_date """
    assert main.formated_date("Dec 18 22:30:15") == "12:18 22:30:15"

L_TEST = [
        "Jan 13 22:30:15 blabla",
        "Jan 14 23:30:15 blabla",
        "Jan 16 26:30:15 blabla",
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla"
    ]
def test_logs_by_day1():
    """ Test unitaire pour logs_by_day """
    output = main.logs_by_day(L_TEST, "Jan 14")
    expected = [
        "Jan 14 23:30:15 blabla",
        "Jan 14 24:30:15 blabla"
        ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output
    

def test_logs_by_day2():
    """ Test unitaire pour logs_by_day """
    output = main.logs_by_day(L_TEST, "Jan 13")
    expected = ["Jan 13 22:30:15 blabla"]
    assert output == expected


def test_logs_between():
    """ Test unitaire pour logs_between """
    output = main.logs_between(L_TEST, "01:14 24:29:15", "01:16 26:31:15")
    expected = [
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla",
        "Jan 16 26:30:15 blabla"
    ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output

def test_logs_between_limite_min():
    """ Test unitaire pour logs_between (min limite) """
    output = main.logs_between(L_TEST, "01:14 24:30:15", "01:16 26:29:15")
    expected = [
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla"
    ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output

def test_logs_between_limite_max():
    """ Test unitaire pour logs_between (max limite) """
    output = main.logs_between(L_TEST, "01:14 24:29:15", "01:16 26:30:15")
    expected = [
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla",
        "Jan 16 26:30:15 blabla"
    ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output

def test_logs_between_default_min():
    """ Test unitaire pour logs_between (min par défaut) """
    output = main.logs_between(L_TEST, date_max="01:14 23:40:00")
    expected = [
            "Jan 13 22:30:15 blabla",
            "Jan 14 23:30:15 blabla"
        ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output

def test_logs_between_default_max():
    """ Test unitaire pour logs_between (max par défaut) """
    output = main.logs_between(L_TEST, date_min="01:14 23:40:00")
    expected = [
        "Jan 16 26:30:15 blabla",
        "Jan 14 24:30:15 blabla",
        "Jan 15 25:30:15 blabla"
    ]
    for elem in output :
        assert elem in expected
    for elem in expected :
        assert elem in output
