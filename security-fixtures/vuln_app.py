# INTENTIONALLY VULNERABLE - security scanner test fixture. NEVER DEPLOY.
# See README.md in this directory.
import hashlib
import pickle
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# A02/A07: hardcoded credential (obviously fake)
AWS_ACCESS_KEY_ID = "AKIAFAKEFAKEFAKE0000"


# A03: SQL injection via string concatenation
@app.route("/user")
def get_user():
    conn = sqlite3.connect("fixtures.db")
    query = "SELECT * FROM users WHERE name = '" + request.args["name"] + "'"
    return str(conn.execute(query).fetchall())


# A03: OS command injection via shell=True
@app.route("/ping")
def ping():
    host = request.args["host"]
    return subprocess.check_output("ping -c 1 " + host, shell=True)


# A03: code injection via eval
@app.route("/calc")
def calc():
    return str(eval(request.args["expr"]))


# A08: insecure deserialization
@app.route("/load", methods=["POST"])
def load():
    obj = pickle.loads(request.get_data())
    return str(obj)


# A02: weak password hashing (MD5, unsalted)
@app.route("/register", methods=["POST"])
def register():
    password = request.form["password"]
    digest = hashlib.md5(password.encode()).hexdigest()
    return digest


# A03: reflected XSS via unescaped user input
@app.route("/hello")
def hello():
    return "<html><body>Hello " + request.args["name"] + "</body></html>"


if __name__ == "__main__":
    app.run(debug=True)
