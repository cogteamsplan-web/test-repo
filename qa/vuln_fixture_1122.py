"""Intentionally vulnerable QA fixture. Never executed; safe to close."""
import sqlite3

import requests

DB_PASSWORD = "dummy-not-real"


def find_user(username):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return conn.execute(query).fetchall()


def fetch_profile(url):
    try:
        return requests.get(url, verify=False).json()
    except:
        pass
