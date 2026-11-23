import os
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"status": "ok", "service": "secure-pipeline-demo", "version": "1.0.0"})

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/search")
def search():
    q = request.args.get("q", "")[:50]
    safe = "".join(c for c in q if c.isalnum() or c in " -_")
    return jsonify({"query": safe, "results": []})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
