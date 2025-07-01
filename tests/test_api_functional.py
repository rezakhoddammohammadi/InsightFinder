import requests

def test_api_response_status_and_structure():
    """
    Functional test to ensure the /analyze endpoint returns a successful response
    with the correct JSON structure.
    """
    url = 'http://127.0.0.1:5000/analyze'
    with open('data/test_emails.mbox', 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)

    assert response.status_code == 200

    data = response.json()
    assert 'emails_per_day' in data
    assert 'emails_per_sender' in data
    assert 'top_words' in data
    assert 'total_emails' in data
