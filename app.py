from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs', methods=['POST'])
def analyze_logs():
    log_data = request.form.get("log_data", "")
    alerts = []

    for line in log_data.splitlines():
        if "failed login" in line.lower():
            alerts.append({"type": "Brute Force", "message": line})

    return render_template('index.html', alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
