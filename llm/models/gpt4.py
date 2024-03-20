"""
OpenAI GPT model interface
"""

from llm.llm_interface import ChatMessage, LlmInterface

class Gpt4(LlmInterface):
    def __init__(self) -> None:
        super().__init__("OpenAI GPT-4")

    def complete_chat(self, prev_messages: list[ChatMessage]) -> ChatMessage:
        return ChatMessage(role="assistant", content="test") 
