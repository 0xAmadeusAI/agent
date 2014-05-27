import asyncio
from pydantic import BaseModel

from twikit import Client

from src.llm.model import PostRequest, ReplyRequest
from src.llm.service import Generator


class Config(BaseModel):
    twitter_username: str
    twitter_password: str
    interval_minutes: int
    twitter_list_id: str

class Bot:
    def __init__(self, config:Config, generator: Generator):
        print(config)
        self.__client = Client('en-US')

        self.__llm_lock = asyncio.Lock()

        self.__twitter_lock = asyncio.Lock()

        self.__config = config

        self.__generator = generator

    async def initialize(self):
        async with self.__twitter_lock:
            await self.__client.login(
                auth_info_1=self.__config.twitter_username,
                password=self.__config.twitter_password
            )

    async def _create_tweet(self, text: str, reply_to: str = None):
        async with self.__twitter_lock:
            if reply_to:
                return await self.__client.create_tweet(text=text, reply_to=reply_to)
            return await self.__client.create_tweet(text=text)

    async def _get_list_tweets(self, list_id: str, count: int):
        async with self.__twitter_lock:
            return await self.__client.get_list_tweets(list_id, count)

    async def start_async_poster(self):
        while True:
            response = self.__generator.generate_response(
                request=PostRequest(
                    user_prompt="Write a twitter post"
                )
            )

            await self._create_tweet(text=response.message.content)

            await asyncio.sleep(self.__config.interval_minutes * 60)

    async def start_async_replier(self):
        while True:
            tweets = await self._get_list_tweets(self.__config.twitter_list_id, 1)

            tweet_text = ""
            tweet_id = ""
            twitter_username = ""
            for tweet in tweets:
                tweet_id = tweet.id
                tweet_text = tweet.text
                twitter_username = tweet.user.name
                break

            response = self.__generator.generate_reply(
                request=ReplyRequest(
                    user_prompt="Generate a reply to this user's tweet",
                    twitter_username=twitter_username,
                    message=tweet_text
                )
            )

            await self._create_tweet(
                text=response.message.content,
                reply_to=tweet_id
            )

            await asyncio.sleep(self.__config.interval_minutes * 60)

