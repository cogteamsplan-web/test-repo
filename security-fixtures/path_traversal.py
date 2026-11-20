# INTENTIONALLY VULNERABLE - security scanner test fixture. NEVER DEPLOY.
# See README.md in this directory.
from flask import Flask, request

app = Flask(__name__)


# A01: path traversal via unsanitized file path from request
@app.route("/read")
def read_file():
    with open(request.args["file"]) as f:
        return f.read()
