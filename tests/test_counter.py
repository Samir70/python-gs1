from lib.counter import Counter

def test_counter_starts_at_zero():
    c = Counter()
    assert c.report() == "Counted to 0 so far."

def test_counter_reports_correct_total():
    c = Counter()
    c.add(7)
    c.add(54)
    assert c.report() == "Counted to 61 so far."
    