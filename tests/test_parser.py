# tests/test_parser.py

from src.parser import parse_mbox_file

def test_parse_mbox_file_returns_email_list():
    """Checks that parsed MBOX file returns a list of valid email dicts."""
    emails = parse_mbox_file("data/test_emails.mbox")
    assert isinstance(emails, list)
    assert len(emails) == 3  # Expected based on test data
    first_email = emails[0]
    assert "from" in first_email
    assert "to" in first_email
    assert "subject" in first_email
    assert "date" in first_email
    assert "body" in first_email
