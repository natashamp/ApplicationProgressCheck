import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define Gmail API scope
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Load credentials from environment variable
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

def authenticate_gmail():
    """Authenticate with Gmail API using OAuth 2.0 without hardcoding credentials."""
    creds = None

    # Load credentials from token.pickle if available
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If credentials are invalid, request authentication
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_PATH:
                raise ValueError("GOOGLE_CREDENTIALS_PATH environment variable is not set.")
            
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

if __name__ == "__main__":
    authenticate_gmail()
    print("Authentication successful!")

