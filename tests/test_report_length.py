from lib.report_length import *

def test_reports_length_of_six_char_string():
    res = report_length("123456")
    assert res == "This string was 6 characters long."