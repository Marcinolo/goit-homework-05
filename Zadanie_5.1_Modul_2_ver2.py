
from datetime import datetime, timedelta
import platform
import aiohttp
import asyncio
from datetime import datetime, timedelta

async def fetch_currency_rate(currency_code, start_date, end_date):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{start_date}/{end_date}/?format=json') as response:
            print(f"Status for {currency_code}:", response.status)
            result = await response.json()
            return result

async def main():
    current_date = datetime.now()
    start_date = (current_date - timedelta(days=10)).strftime("%Y-%m-%d")
    end_date = current_date.strftime("%Y-%m-%d")

    tasks = [
        fetch_currency_rate("USD", start_date, end_date),
        fetch_currency_rate("EUR", start_date, end_date)
    ]

    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)