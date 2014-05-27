import argparse
import asyncio

from pathlib import Path
import yaml
from typing import Dict, Any

from twitter.bot.poster_bot import Bot, Config
from src.llm.ollama_generator import OllamaGenerator, OllamaGeneratorConfig


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a YAML file with optional default values.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        Dictionary containing the configuration

    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If YAML parsing fails
    """
    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)

        return config

    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")

async def start():
    parser = argparse.ArgumentParser(description='AmadeusAI Twitter Agent')
    parser.add_argument('--config', type=str, help='config file arg')
    args = parser.parse_args()

    config = load_config(args.config)

    ollama_generator = OllamaGenerator(
        config=OllamaGeneratorConfig(
            base_url=config["ollama"]["base_url"],
            model_name=config["ollama"]["model_name"],
            system_prompt=config["ollama"]["system_prompt"]
        ),
    )


    bot = Bot(
        config=Config(
            twitter_username=config["bot"]["twitter_username"],
            twitter_password=config["bot"]["twitter_password"],
            interval_minutes=config["bot"]["interval_minutes"],
            twitter_list_id=config["bot"]["twitter_list_id"],
        ),
        generator=ollama_generator
    )

    await bot.initialize()

    poster_task = asyncio.create_task(bot.start_async_poster())
    replier_task = asyncio.create_task(bot.start_async_replier())

    await asyncio.gather(poster_task, replier_task)

def main():
    asyncio.run(start())

if __name__ == "__main__":
    asyncio.run(start())



