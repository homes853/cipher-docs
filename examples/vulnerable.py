import sqlite3
import os

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def render_page(template_name):
    path = "/var/www/templates/" + template_name
    with open(path) as f:
        return f.read()

def run_report(report_id):
    os.system("generate_report.sh " + report_id)

