# scoring.py

def score_report(report: dict) -> dict:
    score = 0

    if report["trend"]["traffic_level"] == "High":
        score += 30
    if report["trend"]["velocity"] == "Spike":
        score += 20
    if report["adaptation"]["risk_level"] == "Low":
        score += 30
    elif report["adaptation"]["risk_level"] == "Medium":
        score += 15

    return {
        "score": score,
        "recommendation": (
            "SEND_TO_GOVERNANCE" if score >= 60 else "IGNORE"
        )
    }
