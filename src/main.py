from utils import logger_config
from ingestion.client import DataCollector, DataCollectorSync
import asyncio
import time

BTC_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
ETH_PRICE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSD"
XRP_PRICE_URL = "https://api.coinbase.com/v2/prices/XRP-USD/spot"
DOGE_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
URL_FAIL_404 = "https://falsa_error"

URLS = {
    "BTC": BTC_PRICE_URL,
    "ETH": ETH_PRICE_URL,
    "XRP": XRP_PRICE_URL,
    "DOGE": DOGE_PRICE_URL
}

def main_sync():
    client = DataCollectorSync(8)


    start_time_sync = time.time()
    logger_config.logger.info("Comienzo del script de llamadas sincrónicas")

    resultado = []

    for name, url in URLS.items():
        try:
            resultado.append(client.get_data(name, url))
        except Exception as e:
            logger_config.logger.error(f"Error al obtener datos: {e}")
            
    final_time = time.time() - start_time_sync

    logger_config.logger.info("Fin del script de llamadas sincrónicas")    
    logger_config.logger.info(f"Tiempo de ejecución: {final_time} segundos")

    for i in resultado:
        logger_config.logger.info(f"Resultado de las llamadas sincrónicas: {i}")

    return final_time

async def main():

    logger_config.logger.info("Comienzo de las consulta asyncronas")

    time_start = time.time()
    time_final = 0

    async with DataCollector(timeout=4) as client:
        urls_copy = URLS.copy()
        urls_copy.update({"FAIL_404": URL_FAIL_404})

        tasks = [client.safe_fetch(name, url) for name, url in urls_copy.items()]
        results = await asyncio.gather(*tasks)

        for item in results:
            if item["ok"]:
                print(f"[OK] {item['name']}: {item['data']}")
            else:
                print(f"[ERR] {item['name']}: {item['error']}")

        time_end = time.time()
        time_final = time_end - time_start
        
        logger_config.logger.info(f"Tiempo de ejecución: {time_final} segundos")

        return time_final


if __name__ == '__main__':
    logger_config.logger.info("Comienzo del script de consultas. ")
    time_async = asyncio.run(main())
    time_sync = main_sync()

    logger_config.logger.info(f"Diferencia de tiempo entre llamadas sincrónicas y asincrónicas. Las llamadas asyncronas son mas rapidas por: {time_sync - time_async} segundos")