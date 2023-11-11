from time import perf_counter
import requests
import pandas as pd
import asyncio
#python -m pip install virtualenv
#python -m virtualenv -p C:\Program Files\Python311\python.exe .venv
#for py312 pip install aiohttp==3.9.0b0
#for py311 pip install aiohttp==3.8.2
import aiohttp 
from aiocsv import AsyncWriter
from aiocsv import AsyncDictWriter
import aiofiles
import csv

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'


def main_request(base_url, endpoint, page_number):
    r = requests.get(url = base_url + endpoint + f"?page={page_number}")
    return r.json()
    
def get_pages(response):
    pages = response['info']['pages']
    return pages

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode'])
        }
        charlist.append(char)
    return charlist

async def fetch(s, base_url, endpoint, page_number):
    async with s.get(url = base_url + endpoint + f"?page={page_number}") as r:
        if r.status != 200:
            r.raise_for_status()
        jsondata = await r.json() #awaiting for all jsons 
        return parse_json(jsondata)
    
async def fetch_all(s, base_url, endpoint, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, base_url, endpoint, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks) #awaiting for all tasks in list tasks
    return res



data = main_request(base_url, endpoint, 1)


async def main():
    urls = range(1, get_pages(data)+1)
    # urls = range(1, 3)
    async with aiohttp.ClientSession() as session, aiofiles.open('./open_REST_api_rickandmorty_pagination_and_data_extraction/async_characters.csv', 'w', encoding="utf-8", newline="") as f:
        jsons = await fetch_all(session, base_url, endpoint, urls)
        flat_list_jsons = [item for sublist in jsons for item in sublist]
        print(flat_list_jsons)
        writer = AsyncDictWriter(f, fieldnames= ['id','name','no_ep'], restval="NULL", quoting=csv.QUOTE_ALL) #https://pypi.org/project/aiocsv/
        await writer.writeheader()
        await writer.writerows(flat_list_jsons)
        print('Written to csv')

if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(main())
    stop = perf_counter()
    print('time taken:', stop - start) #time taken: 1.4714516999956686
