# events.py

import json
import uuid
from datetime import datetime

def emit_event(event_type: str, payload: dict):
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "source": "trend_intelligence",
        "event_type": event_type,
        "payload": payload
    }

    print("[EVENT QUEUE MESSAGE]")
    print(json.dumps(event, indent=2))
