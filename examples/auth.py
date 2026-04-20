import sqlite3
import os
import hashlib

def login(username, password):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
    return cur.fetchone()

def get_file(path):
    base = "/var/app/uploads/"
    full_path = base + path
    with open(full_path) as f:
        return f.read()

def ping(host):
    os.system("ping -c 1 " + host)
