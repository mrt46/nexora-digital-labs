# agents/strategy_inquiry.py

from agents.base_agent import BaseAgent

class StrategyInquiryAgent(BaseAgent):
    def run(self, input_data: dict) -> dict:
        return {
            "questions": {
                "content": "How to convert this into evergreen analysis?",
                "seo": "Which long-tail intent fits this topic?",
                "monetization": "When is monetization safe?"
            }
        }
