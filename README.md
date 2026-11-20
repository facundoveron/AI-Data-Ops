# AI-Data-Ops

# Que datos consume el proyecto

El proyecto consume el precio de diferentes criptomonedas, de diferentes portales, para que no nos bloqueen las peticiones asyncronas.
Las urls que consume el proyecto son:
- Precio de btc en coingecko: "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
- Precio de eth en binance: "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSD"
- Precio de xrp en coinbase: "https://api.coinbase.com/v2/prices/XRP-USD/spot"
- Precio de doge en coingecko: "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"

Ademas el proyecto consume una url que falla, para demostrar el manejo de errores:
- Url falsa: "https://falsa_error" 

# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# ejecutar
python src/main.py