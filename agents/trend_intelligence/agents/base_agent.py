# agents/base_agent.py

from pathlib import Path

class BaseAgent:
    def __init__(self, name: str, prompt_path: str):
        self.name = name
        self.prompt = Path(prompt_path).read_text(encoding="utf-8")

    def run(self, input_data: dict) -> dict:
        """
        Override this method in child agents.
        """
        raise NotImplementedError("Agent must implement run()")
