"""
Defines the LLM Interface which all models must adhere to
in order to be used in this project
"""

from abc import ABC, abstractmethod
from collections import namedtuple

ChatMessage = namedtuple(
    # A single message, typically one of many in
    # a chain of messages forming a chat with the LLM
    # (follows the format used by GPT4 at time of writing)
    "ChatMessage",
    ["role", "content"],
)


class LlmInterface(ABC):
    """Shared interface which all LLMs must use in order
    to be used in this project
    """

    def __init__(self, name: str) -> None:
        """Defines attributes at instantiation time

        Args:
            name (str): An identifying label for the LLM
        """
        self.name = name

    @abstractmethod
    def complete_chat(self, prev_messages=list[ChatMessage]) -> ChatMessage:
        """LLM generates a message in response to the existing
        chain of messages `prev_messages`"""
        pass
