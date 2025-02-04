from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    response = {
        "message": "Hello, Render! Your API is working.",
        "status": "success"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # سازگار با پلتفرم‌های استقرار مانند Render
    app.run(host="0.0.0.0", port=port, debug=True)  # فعال‌سازی حالت debug برای خطایابی بهتر
