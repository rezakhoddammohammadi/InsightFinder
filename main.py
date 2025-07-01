from src.parser import parse_mbox_file
from src.analyzer import count_senders, count_by_day, get_most_common_words
from src.visualizer import plot_email_counts_by_sender, plot_emails_over_time

import nltk
nltk.download('punkt')
nltk.download('stopwords')

if __name__ == "__main__":
    emails = parse_mbox_file("data/test_emails.mbox")
    print(f"{len(emails)} emails parsed.\n")

    for i, email in enumerate(emails, start=1):
        print(f"--- Email #{i} ---")
        print(f"From   : {email['from']}")
        print(f"To     : {email['to']}")
        print(f"Subject: {email['subject']}")
        print(f"Date   : {email['date']}")
        print(f"Body   : {email['body']}\n")

    # Aggregate statistics
    sender_stats = count_senders(emails)
    day_stats = count_by_day(emails)

    print("Emails per Sender:")
    for sender, count in sender_stats.items():
        print(f"{sender}: {count}")

    print("\nEmails per Day:")
    for day, count in day_stats.items():
        print(f"{day}: {count}")

    # Analyze most common words
    print("\nTop 10 Most Common Words:")
    common_words = get_most_common_words(emails)
    for word, count in common_words:
        print(f"{word}: {count}")

    # Plot results
    plot_email_counts_by_sender(sender_stats)
    plot_emails_over_time(day_stats)
