from abc import ABC, abstractmethod
from src.llm.model import PostRequest, ReplyRequest

# AbstractClass/Interface implementations are in {integration}_generator.py files
class Generator(ABC):

    @abstractmethod
    def generate_response(self, request:PostRequest):
        pass

    @abstractmethod
    def generate_reply(self, request:ReplyRequest):
        pass
