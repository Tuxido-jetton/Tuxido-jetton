
#!/usr/bin/env python3
"""
Tuxido Mining Bot Web Interface
Simple web dashboard for monitoring mining bot status
"""

from flask import Flask, jsonify, render_template_string
import os
import json
import threading
import asyncio
from datetime import datetime

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Tuxido Mining Bot Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #1a1a1a; color: #fff; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { text-align: center; margin-bottom: 30px; }
        .card { background: #2d2d2d; padding: 20px; margin: 10px 0; border-radius: 8px; border: 1px solid #444; }
        .metric { display: inline-block; margin: 10px 20px; text-align: center; }
        .metric-value { font-size: 24px; font-weight: bold; color: #4CAF50; }
        .metric-label { font-size: 14px; color: #ccc; }
        .status-active { color: #4CAF50; }
        .status-inactive { color: #f44336; }
        .refresh-btn { background: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        .refresh-btn:hover { background: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Tuxido Mining Bot Dashboard</h1>
            <p>TON Blockchain Mining Bot - Real-time Status</p>
        </div>
        
        <div class="card">
            <h3>🔋 Mining Status</h3>
            <div id="status">Loading...</div>
            <button class="refresh-btn" onclick="refreshStatus()">Refresh Status</button>
        </div>
        
        <div class="card">
            <h3>📊 Performance Metrics</h3>
            <div id="metrics">Loading...</div>
        </div>
        
        <div class="card">
            <h3>💰 Profit Summary</h3>
            <div id="profit">Loading...</div>
        </div>
        
        <div class="card">
            <h3>🌐 Project Links</h3>
            <p>🔗 <a href="https://replit.com/@s9igma/TuxidoMineBot" target="_blank" style="color: #4CAF50;">Main Project Repository</a></p>
            <p>🌊 <a href="https://ston.fi" target="_blank" style="color: #4CAF50;">StonFi DEX Trading</a></p>
            <p>📱 <a href="https://t.me/tuxidomining" target="_blank" style="color: #4CAF50;">Telegram Community</a></p>
        </div>
    </div>

    <script>
        function refreshStatus() {
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').innerHTML = 
                        `<span class="${data.mining_active ? 'status-active' : 'status-inactive'}">
                            ${data.mining_active ? '✅ ACTIVE' : '⏸️ INACTIVE'}
                         </span>`;
                    
                    document.getElementById('metrics').innerHTML = `
                        <div class="metric">
                            <div class="metric-value">${data.total_mined.toLocaleString()}</div>
                            <div class="metric-label">Total Tx Mined</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">${data.blocks_mined.toLocaleString()}</div>
                            <div class="metric-label">Blocks Mined</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">${data.current_hash_rate}</div>
                            <div class="metric-label">Hash Rate (Tx/s)</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">${data.runtime}</div>
                            <div class="metric-label">Runtime</div>
                        </div>
                    `;
                    
                    document.getElementById('profit').innerHTML = `
                        <div class="metric">
                            <div class="metric-value">$${data.profit_metrics.daily_earnings.toFixed(2)}</div>
                            <div class="metric-label">Estimated Value</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">${data.profit_metrics.performance_score.toFixed(1)}%</div>
                            <div class="metric-label">Efficiency Score</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">${data.profit_metrics.hourly_rate.toFixed(0)}</div>
                            <div class="metric-label">Tx/hour</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">$${data.market_data.ton_price_usd.toFixed(2)}</div>
                            <div class="metric-label">TON Price</div>
                        </div>
                    `;
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('status').innerHTML = '<span class="status-inactive">❌ ERROR</span>';
                });
        }
        
        // Refresh every 10 seconds
        setInterval(refreshStatus, 10000);
        refreshStatus(); // Initial load
    </script>
</body>
</html>
'''

@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/status')
def api_status():
    """API endpoint for mining bot status"""
    try:
        # Try to load current mining data
        if os.path.exists('mining_progress.json'):
            with open('mining_progress.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            # Return default status
            return jsonify({
                "mining_active": False,
                "total_mined": 0,
                "daily_mined": 0,
                "blocks_mined": 0,
                "current_hash_rate": 0,
                "runtime": "0:00:00",
                "network": "mainnet",
                "profit_metrics": {
                    "daily_earnings": 0.0,
                    "performance_score": 0.0,
                    "hourly_rate": 0.0
                },
                "market_data": {
                    "ton_price_usd": 2.5
                },
                "ai_optimized": True
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/start')
def start_mining():
    """API endpoint to start mining"""
    try:
        # This would start the mining bot in a separate thread
        return jsonify({"status": "Mining start requested", "success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
