import requests

def test_analyze_api():
    """
    Sends a test MBOX file to the /analyze API endpoint
    and verifies that the response contains expected fields.
    """
url = 'http://127.0.0.1:5000/analyze'
with open('data/test_emails.mbox', 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())
