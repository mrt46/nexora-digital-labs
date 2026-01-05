# content_brief.py

def generate_content_brief(report: dict, governance: dict) -> dict:
    if governance["recommendation"] != "SEND_TO_GOVERNANCE":
        return {}

    return {
        "title_suggestion": (
            f"Why {report['trend']['primary_topic']} Is Trending "
            f"in {report['trend']['region']} — Analysis"
        ),
        "content_type": "evergreen_analysis",
        "key_angles": [
            "Why this topic is trending now",
            "Underlying structural reasons",
            "Risks and uncertainties",
            "What would need to change for long-term relevance"
        ],
        "constraints": {
            "no_speculation": True,
            "no_price_prediction": True,
            "tone": "analytical"
        },
        "seo_intent": "informational",
        "priority": "medium"
    }
