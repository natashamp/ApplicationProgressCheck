# Gmail Word Extractor


This project fetches emails from Gmail using the Gmail API and securely stores relevant messages in an SQLite database. It **removes the need to store authentication credentials in the source code** by using environment variables.

---

Inital steps to use Python with Gmail API to fetch emails

Python 3 installed (`python --version` to check)

- install packages
```pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

google-auth → Handles authentication with Google services.
google-auth-oauthlib → Manages OAuth flow.
google-api-python-client → Allows us to interact with Gmail API.
sqlite3 → Database to store emails.

1) Google Cloud Console ([Sign up here](https://console.cloud.google.com/))
- Create an account
- Select on API & Services and Library 
- Enable an Gmail API
- Create an credentials 
    - OAuth Credentials:
        - Create Credentials → OAuth Client ID
        - Under Application Type, select "Desktop App"
        - Click Create, then Download the credentials.json file



2) Set use Enviroment Variables on macOS 

Run this command (replace with your actual file path):

   ```bash
   export GOOGLE_CREDENTIALS_PATH="/Users/yourusername/Documents/credentials.json"

Verify variable is set:

echo $GOOGLE_CREDENTIALS_PATH



3) Run this script to authenticate gmail

```python3 authenticate_gmail.py

- generated token.pickle



```python3 create_db.py

- creates sqlite3 database emails.db in folder



```python3 fetch_keywords_emails.py

- fetches last 20 gmails from inbox and filters


