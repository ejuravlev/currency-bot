import os
import logging
import aiohttp


logging.basicConfig(
    format='[API]: %(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class CurrencyApi:
    api_base = 'https://api.apilayer.com'
    headers = {
        "apikey": os.environ.get('CURRENCY_API')
    }

    @classmethod
    async def get_currency(self, from_currency, to_currency, amount=1) -> float:
        api_url = f'{self.api_base}/currency_data/convert'
        api_url += f'?from={from_currency}&to={to_currency}&amount={amount}'
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, headers=self.headers) as response:
                if response.status == 200:
                    result = await response.json()
                    logging.info(f'api result: {result}')
                    if result['success']:
                        return result['result']
