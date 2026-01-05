# events.py

def emit_event(event_type: str, payload: dict):
    print(f"[EVENT] {event_type}")
    print(payload)
