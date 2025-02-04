from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    # رندر کردن فایل index.html از دایرکتوری templates
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # سازگار با پلتفرم‌های استقرار مانند Render
    app.run(host="0.0.0.0", port=port, debug=True)  # فعال‌سازی حالت debug برای خطایابی بهتر
