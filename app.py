from flask import Flask, jsonify
from flask_cors import CORS

from routes.upload import upload_bp
from routes.chat import chat_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    upload_bp,
    url_prefix="/api"
)

app.register_blueprint(
    chat_bp,
    url_prefix="/api"
)

@app.route("/")
def home():
    return jsonify({
        "message": "Multi-Document RAG Backend is running!"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
