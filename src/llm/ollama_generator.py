from pydantic import BaseModel

from src.llm.service import Generator
from src.llm.model import PostRequest, ReplyRequest

from ollama import Client as OllamaClient

class OllamaGeneratorConfig(BaseModel):
    base_url: str
    model_name: str
    system_prompt: str

class OllamaGenerator(Generator):
    def __init__(self, config:OllamaGeneratorConfig):
        print(config)
        self.__ollama_client = OllamaClient(
            host=config.base_url,
        )

        self.__model_name = config.model_name
        self.__system_prompt = config.system_prompt

    def generate_response(self, request:PostRequest) -> str:
        messages = [
            {
                'role': 'system',
                'content': self.__system_prompt
            },
            {
                'role': 'user',
                'content': request.user_prompt
            }
        ]

        return self.__ollama_client.chat(
            # 'mannix/llama3.1-8b-lexi'
            model=self.__model_name,
            messages=messages
        )

    def generate_reply(self, request:ReplyRequest):
        reply_message_with_metadata = f"""
            {request.user_prompt}
            
            username: {request.twitter_username},
            user_tweet: {request.message}
        """

        messages = [
            {
                'role': 'system',
                'content': self.__system_prompt
            },
            {
                'role': 'user',
                'content': reply_message_with_metadata
            }
        ]

        return self.__ollama_client.chat(
            # 'mannix/llama3.1-8b-lexi'
            model=self.__model_name,
            messages=messages
        )

