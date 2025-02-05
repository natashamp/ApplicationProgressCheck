from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_stored_emails():
    """Retrieve all stored emails from the database."""
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    # Fetch all emails
    cursor.execute("SELECT id, sender, subject, body FROM emails ORDER BY id DESC")
    emails = cursor.fetchall()
    
    conn.close()
    return emails

@app.route("/")
def index():
    emails = get_stored_emails()
    return render_template("index.html", emails=emails)

if __name__ == "__main__":
    app.run(debug=True)

