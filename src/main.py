from utils import logger_config
from ingestion.client import DataCollector
import asyncio
import time

BTC_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
ETH_PRICE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSD"
XRP_PRICE_URL = "https://api.coinbase.com/v2/prices/XRP-USD/spot"
DOGE_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
URL_FAIL_404 = "https://falsa_error"

def main_sync():
    client = DataCollector()

    urls = [
        BTC_PRICE_URL,
        ETH_PRICE_URL,
        XRP_PRICE_URL,
        DOGE_PRICE_URL
    ]

    start_time_sync = time.time()
    logger_config.logger.info("Comienzo del script de llamadas sincrónicas")

    resultado = []

    for url in urls:
        try:
            resultado.append(client.get_data(url))
        except Exception as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            
    final_time = time.time() - start_time_sync

    logger_config.logger.info("Fin del script de llamadas sincrónicas")    
    logger_config.logger.info(f"Tiempo de ejecución: {final_time} segundos")

    for i in resultado:
        logger_config.logger.info(f"Resultado de las llamadas sincrónicas: {i}")

    return final_time



async def main_async():

    client = DataCollector()

    logger_config.logger.info("Comienzo del script de llamadas asincronicas")
    start_time_async = time.time()

    resultado = await asyncio.gather(
        client.get_data_async(BTC_PRICE_URL),
        client.get_data_async(ETH_PRICE_URL),
        client.get_data_async(XRP_PRICE_URL),
        client.get_data_async(DOGE_PRICE_URL)
    )

    final_time = time.time() - start_time_async    
    logger_config.logger.info("Fin del script de llamadas asincronicas")
    logger_config.logger.info(f"Tiempo de ejecución: {final_time} segundos")
    logger_config.logger.info(f"Resultado de las llamadas asincrónicas: {resultado}")

    return final_time


if __name__ == "__main__":
    logger_config.logger.info("Comienzo del script de llamadas.")

    time_sync = main_sync()
    time_async = asyncio.run(main_async())

    logger_config.logger.info("Fin del script de llamadas.")
    logger_config.logger.info(f"Diferencia de tiempo entre llamadas sincrónicas y asincrónicas. Las llamadas asyncronas son mas rapidas por: {time_sync - time_async} segundos")