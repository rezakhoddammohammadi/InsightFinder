import matplotlib.pyplot as plt
import pandas as pd

def plot_email_counts_by_sender(sender_count_dict):
    """Generates a bar chart showing the number of emails per sender."""
    senders = list(sender_count_dict.keys())
    email_counts = list(sender_count_dict.values())

    plt.figure(figsize=(8, 5))
    plt.bar(senders, email_counts, color='steelblue')
    plt.title("Email Volume by Sender")
    plt.xlabel("Sender")
    plt.ylabel("Email Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_emails_over_time(date_count_dict):
    """Generates a line chart showing daily email activity over time."""
    df = pd.DataFrame({
        "Date": list(date_count_dict.keys()),
        "EmailCount": list(date_count_dict.values())
    })
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    plt.figure(figsize=(8, 4))
    plt.plot(df["Date"], df["EmailCount"], marker='o', linestyle='-', color='darkgreen')
    plt.title("Email Activity Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Emails")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
