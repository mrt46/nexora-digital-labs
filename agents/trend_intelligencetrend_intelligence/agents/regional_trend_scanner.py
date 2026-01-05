# agents/regional_trend_scanner.py

import feedparser
from agents.base_agent import BaseAgent

class RegionalTrendScanner(BaseAgent):
    def run(self, input_data: dict) -> dict:
        region = input_data.get("region", "TR")

        feed_url = "https://news.google.com/rss/search?q=crypto&hl=tr&gl=TR&ceid=TR:tr"
        feed = feedparser.parse(feed_url)

        top_entry = feed.entries[0]

        return {
            "region": region,
            "site": top_entry.source.get("title", "unknown"),
            "url": top_entry.link,
            "primary_topic": top_entry.title,
            "signal_type": "Google News RSS",
            "traffic_level": "High",
            "velocity": "Spike"
        }
