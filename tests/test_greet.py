from lib.greet import *

def test_greet():
    result = greet("Great Person")
    assert result == "Hello, Great Person!"