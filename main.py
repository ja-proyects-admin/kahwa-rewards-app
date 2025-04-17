import functions_framework
from datetime import datetime
from flask import Request

@functions_framework.http
def hello_http(request: Request):
    name = request.args.get("name") or (request.get_json(silent=True) or {}).get("name", "Julian")
    timestamp = datetime.utcnow().isoformat()

    message = f"Hola {name}, bienvenido a Kahwa Rewards!"
    print(f"[INFO] {message} @ {timestamp}")

    return {
        "message": message,
        "timestamp": timestamp
    }
