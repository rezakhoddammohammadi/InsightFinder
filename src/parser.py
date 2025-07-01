import mailbox
from email.utils import parsedate_to_datetime

def parse_mbox_file(file_path):
    """Parses an MBOX file and extracts relevant email fields."""
    mbox = mailbox.mbox(file_path)
    email_list = []

    for message in mbox:
        try:
            email_entry = {
                "from": message.get("From"),
                "to": message.get("To"),
                "subject": message.get("Subject"),
                "date": str(parsedate_to_datetime(message.get("Date"))),
                "body": extract_plain_text_body(message)
            }
            email_list.append(email_entry)
        except Exception as error:
            print(f"[WARN] Skipping message due to error: {error}")

    return email_list

def extract_plain_text_body(message):
    """Extracts the plain text body of an email message."""
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                try:
                    return part.get_payload(decode=True).decode(errors="ignore")
                except Exception:
                    return ""
    else:
        try:
            return message.get_payload(decode=True).decode(errors="ignore")
        except Exception:
            return ""
