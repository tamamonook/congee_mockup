from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def echo():
    return jsonify({
        "method": request.method,
        "headers": dict(request.headers),
        "args": request.args,
        "form": request.form,
        "json": request.json,
        "data": request.data.decode("utf-8"),
        "message": "This message is from Congee mockup"
    }), 200

if __name__ == "__main__":
    cert_file = os.getenv("CERT_FILE", "cert.pem")
    key_file = os.getenv("KEY_FILE", "key.pem")
    app.run(host="0.0.0.0", port=5000, ssl_context=(cert_file, key_file))
