from lib.check_codeword import *

def test_check_codeword_returns_invite_for_correct_codeword():
    res = check_codeword("horse")
    assert res == "Correct! Come in."

def test_check_codeword_returns_closeWhengivenHope():
    res = check_codeword("hope")
    assert res == "Close, but nope."

def test_check_codeword_returns_WRONG_for_bad_word():
    res = check_codeword("hotel")
    assert res == "WRONG!"
