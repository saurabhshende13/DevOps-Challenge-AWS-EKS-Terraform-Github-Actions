from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import psutil
import time

app = Flask(__name__)
CORS(app)

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_struct = time.gmtime(uptime_seconds)
    days = uptime_struct.tm_yday - 1
    uptime_str = f"{days} days, {uptime_struct.tm_hour:02d}:{uptime_struct.tm_min:02d}:{uptime_struct.tm_sec:02d}"
    return uptime_str

@app.route("/", methods=["GET"])
def system_info():
    current_time = datetime.utcnow().isoformat() + "Z"
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    data = {
        "timestamp": current_time,
        "visitor_ip": visitor_ip,
        "system_metrics": {
            "uptime": get_uptime(),
            "cpu_percent": f"{cpu_percent}%",
            "memory": {
                "total_mb": mem.total // (1024**2),
                "available_mb": mem.available // (1024**2),
                "used_mb": mem.used // (1024**2),
                "percent": mem.percent,
            },
            "disk": {
                "total_gb": disk.total // (1024**3),
                "used_gb": disk.used // (1024**3),
                "free_gb": disk.free // (1024**3),
                "percent": disk.percent,
            },
        }
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

