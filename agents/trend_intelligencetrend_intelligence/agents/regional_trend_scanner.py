# agents/regional_trend_scanner.py

from agents.base_agent import BaseAgent

class RegionalTrendScanner(BaseAgent):
    def run(self, input_data: dict) -> dict:
        region = input_data.get("region", "GLOBAL")

        # --- STUB: gerçek scraping / API sonra ---
        return {
            "region": region,
            "site": "99bitcoins.com",
            "url": "https://99bitcoins.com",
            "primary_topic": "crypto speculation",
            "signal_type": "Search + News",
            "traffic_level": "High",
            "velocity": "Spike"
        }
