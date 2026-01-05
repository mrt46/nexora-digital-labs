# agents/performance_decomposer.py

from agents.base_agent import BaseAgent

class PerformanceDecomposer(BaseAgent):
    def run(self, input_data: dict) -> dict:
        return {
            "primary_driver": "timeliness",
            "secondary_drivers": ["speculative headline", "AI mention"],
            "structural_notes": "short content, fast publish"
        }
