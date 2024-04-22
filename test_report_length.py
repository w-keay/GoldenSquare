from report_length import report_length

def test_report_length():
    assert report_length("hello") == "This string was 5 characters long."
    assert report_length("") == "This string was 0 characters long."
    assert report_length("123456789") == "This string was 9 characters long."
