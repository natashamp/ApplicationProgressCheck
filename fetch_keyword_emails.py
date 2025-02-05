import base64
import email
from googleapiclient.discovery import build
from authenticate_gmail import authenticate_gmail
import sqlite3

KEYWORDS = ["Thank you"]



def store_email(sender, subject, body):
    """Save extracted emails to the SQLite database."""
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO emails (sender, subject, body) VALUES (?, ?, ?)",
                   (sender, subject, body))
    conn.commit()
    conn.close()



def get_filtered_emails():
    """Fetches filtered emails from Gmail"""
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)

    # Get list of emails
    results = service.users().messages().list(userId="me", maxResults=100).execute() # Get first 20 emails
    messages = results.get("messages", [])

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = msg_data["payload"]["headers"]

        # Extract email subject & sender
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown Sender")

        # Extract email body
        parts = msg_data["payload"].get("parts", [])
        body = ""
        for part in parts:
            if part.get("mimeType") == "text/plain":
                body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")

       # Filter by keywords
        if any(keyword.lower() in body.lower() or keyword.lower() in subject.lower() for keyword in KEYWORDS):
            store_email(sender, subject, body)  # Store in database

            print(f"Stored email from {sender} with subject: {subject}")
            print(f"From: {sender}")
            print(f"Subject: {subject}")
            print(f"Body: {body[:50]}...\n")
            print("=" * 50)

if __name__ == "__main__":
    get_filtered_emails()


