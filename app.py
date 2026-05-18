# app.py
from flask import Flask, render_template_string, request, jsonify
import sys
import re

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
        input[type="text"] { width: 75%; padding: 12px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; }
        button { background-color: #0056b3; color: white; border: none; padding: 12px 24px; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; }
        button:hover { background-color: #004085; }
        button:disabled { background-color: #cccccc; cursor: not-allowed; }
        .console-log { background-color: #1e1e1e; color: #39ff14; font-family: 'Courier New', Courier, monospace; padding: 15px; border-radius: 4px; margin-top: 20px; max-height: 250px; overflow-y: auto; display: none; white-space: pre-wrap; text-align: left; }
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
            <input type="text" id="repo-url" placeholder="https://github.com/username/repository">
            <button id="deploy-btn" onclick="triggerDeployment()">Trigger Cloud Deployment</button>
            
            <div id="console" class="console-log"></div>
        </div>
    </div>

    <script>
        function triggerDeployment() {
            const urlInput = document.getElementById('repo-url').value.trim();
            const btn = document.getElementById('deploy-btn');
            const consoleBox = document.getElementById('console');

            if (!urlInput) {
                alert('Please enter a valid GitHub repository URL.');
                return;
            }

            // UI Reset
            btn.disabled = true;
            consoleBox.style.display = 'block';
            consoleBox.innerText = 'Initializing connection to deployment framework...\\n';

            // Send request to Flask Backend
            fetch('/deploy', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ repo_url: urlInput })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    consoleBox.innerText += `\\n❌ ERROR: ${data.error}`;
                    btn.disabled = false;
                    return;
                }
                
                // Stream the returned mock deployment sequence steps onto screen
                let i = 0;
                function printLogs() {
                    if (i < data.logs.length) {
                        consoleBox.innerText += data.logs[i] + '\\n';
                        consoleBox.scrollTop = consoleBox.scrollHeight;
                        i++;
                        setTimeout(printLogs, 800); // 800ms delay between log messages for realistic simulation
                    } else {
                        btn.disabled = false;
                    }
                }
                printLogs();
            })
            .catch(err => {
                consoleBox.innerText += '\\n❌ Transmission failure communicating with cloud pipeline orchestration.';
                btn.disabled = false;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/deploy', methods=['POST'])
def deploy_project():
    data = request.get_json() or {}
    repo_url = data.get('repo_url', '').strip()

    # Simple validation using regex to check for valid GitHub links
    if not re.match(r'^https://github\.com/[\w-]+/[\w.-]+/?$', repo_url):
        return jsonify({"error": "Invalid URL structure. Must match https://github.com/user/repo"}), 400

    # Extract repository name from string to make logs dynamic
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    
    print(sys.stdout.flush())
    print(f"Deployment triggered for repository target: {repo_url}", flush=True)

    # Simulated systemic steps representing the architecture loop we completed manually!
    deployment_logs = [
        "🌐 Fetching remote Git configurations...",
        f"📥 Successfully cloned source repository branch [{repo_name}/main].",
        "📦 Compiling environment dependencies inside local workspace context...",
        "🔨 Executing container compilation: 'docker build -t cloud-portal-app:latest .'",
        "🐋 Container metadata layer generated successfully.",
        "🔐 Autoconfiguring credentials wrapper targeting AWS ECR Registry...",
        "🚀 Transferring image payload layers to repository architecture...",
        "⚙️ Provisioning cloud container cluster blueprint mappings...",
        "⚡ Launching container environment layout on serverless AWS Fargate compute layer...",
        f"✨ DEPLOYMENT COMPLETE! Application [{repo_name}] live at http://127.0.0.1:8080"
    ]

    return jsonify({"status": "processing", "logs": deployment_logs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
