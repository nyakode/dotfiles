from binance.client import Client
import config.config as cfg

bClient = Client(cfg.api_key, cfg.secret_key)
print('logged in')

info = bClient.get_symbol_info('BTCUSDT')

for i in info:
    print(i)
    print('Hola Mundo')
