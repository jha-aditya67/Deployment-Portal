# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Deployment Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 40px; color: #333; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #0056b3; margin-top: 0; }
        .status-badge { display: inline-block; padding: 6px 12px; background-color: #28a745; color: white; border-radius: 20px; font-size: 14px; font-weight: bold; }
        .card { border: 1px solid #e1e4e8; padding: 20px; border-radius: 6px; margin-top: 20px; background-color: #fafbfc; }
        button { background-color: #0056b3; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #004085; }
    </style>
</head>
<body>
    <div class="container">
        <h1>☁️ Cloud Deployment Portal</h1>
        <p>Status: <span class="status-badge">Base Engine Active</span></p>
        <hr>
        <div class="card">
            <h3>Deploy a New Project</h3>
            <p>Paste your GitHub repository URL below to provision serverless container infrastructure dynamically.</p>
            <input type="text" placeholder="https://github.com/user/repo" style="width: 80%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;"><br>
            <button onclick="alert('Engine linkage initialized! Architecture deployment system coming up next.')">Trigger Cloud Deployment</button>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    print("Dashboard requested by a visitor!", flush=True)
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("Starting Flask application server on Port 80...", flush=True)
    app.run(host='0.0.0.0', port=80)
