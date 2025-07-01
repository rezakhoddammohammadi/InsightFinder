from src.analyzer import count_senders, count_by_day, get_most_common_words

mock_emails = [
    {"from": "a@example.com", "date": "2022-01-01T10:00:00", "body": "Hello world"},
    {"from": "b@example.com", "date": "2022-01-01T12:00:00", "body": "World is great"},
    {"from": "a@example.com", "date": "2022-01-02T08:30:00", "body": "Hello again"},
]

def test_count_senders_works():
    """Verifies that senders are counted correctly."""
    result = count_senders(mock_emails)
    assert result["a@example.com"] == 2
    assert result["b@example.com"] == 1

def test_count_by_day_works():
    """Checks daily email counts are accurate."""
    result = count_by_day(mock_emails)
    assert result["2022-01-01"] == 2
    assert result["2022-01-02"] == 1

def test_get_most_common_words_works():
    """Ensures most common words are extracted correctly from email bodies."""
    result = get_most_common_words(mock_emails)
    assert isinstance(result, list)
    words = [w for w, _ in result]
    assert "hello" in words
    assert "world" in words
