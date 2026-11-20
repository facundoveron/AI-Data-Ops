import aiohttp
import requests
from utils import logger_config


class DataCollector:
    def __init__(self):
        pass

    async def get_data_async(self, url: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    return await resp.json()
        except aiohttp.ClientError as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            raise
        except Exception as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            raise
    
    def get_data(self, url: str):
        try:
            resp = requests.get(url)
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logger_config.logger.error(f"Error HTTP al obtener datos: {e}")
            raise
        except Exception as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            raise