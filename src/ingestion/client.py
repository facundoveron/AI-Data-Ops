import aiohttp
import requests
import asyncio
from utils import logger_config

class DataCollectorSync:
    def __init__(self, timeout):
        self.timeout = timeout
    
    def get_data(self, name, url):
        try:
            logger_config.logger.info(f"Obteniendo datos de {name}. Para la url: {url}")
            resp = requests.get(url)
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logger_config.logger.error(f"Error HTTP al obtener datos: {e}")
            raise
        except Exception as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            raise

class DataCollector:

    def __init__(self, timeout = 8):
        self.timeout = timeout
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout),
                headers={'User-Agent': 'CryptoWatcher/1.0'}
            )

        return self

    async def close(self):
        if self._session is not None and not self._session.closed:
            await self._session.close()
            await asyncio.sleep(0.25)
        self._session = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            raise RuntimeError("La sesión no está activa. Usá `async with MultiUrlClient()`.")
        return self._session

    async def __fetch_json__(self, url, params=None):
        """Pide una URL absoluta y devuelve el JSON, o lanza error si falla."""
        session = self._get_session()
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def safe_fetch(self, name, url):
        try:
            logger_config.logger.info(f"Obteniendo datos de {name}. Para la url: {url}")
            data = await self.__fetch_json__(url)
            return {"name": name, "ok": True, "data": data, "error": None}
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError) as exc:
            # ClientError cubre errores HTTP (4xx/5xx tras raise_for_status), DNS, conexión, etc.
            return {"name": name, "ok": False, "data": None, "error": str(exc)}