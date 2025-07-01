from collections import Counter
import nltk
import os

# Add custom NLTK data path (relative to project structure)
nltk.data.path.append(os.path.join(os.path.dirname(__file__), '..', 'nltk_data'))
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def count_senders(emails):
    """Counts the number of emails sent by each sender."""
    return Counter(email['from'] for email in emails)

def count_by_day(emails):
    """Counts the number of emails per day (YYYY-MM-DD)."""
    return Counter(email['date'][:10] for email in emails)

def get_most_common_words(emails, n=10):
    """Finds the top N most common words in email bodies, excluding stopwords."""
    nltk_stopwords = set(stopwords.words('english'))
    all_words = []

    for email in emails:
        body = email.get("body", "")
        tokens = word_tokenize(body.lower())
        words = [
            word for word in tokens
            if word.isalpha() and word not in nltk_stopwords
        ]
        all_words.extend(words)

    return Counter(all_words).most_common(n)
