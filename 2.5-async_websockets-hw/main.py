import platform
import aiohttp
import asyncio
import sys

from pprint import pprint
from datetime import datetime, timedelta


def convert_int_to_dates(days_count: int):
    dates = list()
    date = datetime.today() - timedelta(days=days_count)
    while date != datetime.today():
        days_count -= 1
        date = datetime.today() - timedelta(days=days_count)
        dates.append(date.strftime("%d.%m.%Y"))
    return dates

async def get_exchange_rate(session, date):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error status: {response.status} for {url}")
    except aiohttp.ClientConnectorError as err:
        print(f'Connection error: {url}', str(err))

async def main(days: int):
    dates_list = convert_int_to_dates(days)
    responses = list()
    for date in dates_list:
        async with aiohttp.ClientSession() as session:
            result = await get_exchange_rate(session, date)
            responses.append(result)
    return responses


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    if len(sys.argv) > 1:
        days_count = int(sys.argv[1])
        if days_count > 10:
            days_count = 10
    else:
        days_count = 1

    res = asyncio.run(main(days=days_count))
    for r in res:
        pprint(r)
