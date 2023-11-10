from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
import requests
import pandas as pd
import threading
import csv

csv_writer_lock = threading.Lock()

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

start = perf_counter()

def main_request(url):
    r = requests.get(url)
    return r.json()

def get_pages(response):
    pages = response['info']['pages']
    return pages

def parse_json(url):
    response = main_request(url)
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode'])
        }
        charlist.append(char)
    return charlist


data = main_request(f"{base_url}{endpoint}?page=1")
urls = get_pages(data)

# for x in range(1,get_pages(data)+1):
#     list_jsons.extend(parse_json(main_request(base_url, endpoint, x)))

# with ThreadPoolExecutor() as executor:
#     for i in range(1,urls):
#         list_jsons = (parse_json(main_request(base_url, endpoint, i)))
#         with csv_writer_lock:
#             with open('./open_REST_api_rickandmorty_pagination_and_data_extraction/thread_characters.csv', mode='a', encoding="utf-8", newline="") as f:
#                 writer = csv.DictWriter(f,['id','name','no_ep'])
#                 writer.writeheader()
#                 writer.writerows(list_jsons)
#Time taken: 20.450044099998195

list_urls = [f"{base_url}{endpoint}?page={i}" for i in range(1,urls+1)]
# print(list_urls)

list_jsons = []

with ThreadPoolExecutor() as executor:
    list_jsons = list(executor.map(parse_json,list_urls))

'''flattening file'''
flat_list_jsons = [item for sublist in list_jsons for item in sublist]


final = pd.DataFrame(flat_list_jsons)

print(final.head(), final.tail())

final.to_csv('./open_REST_api_rickandmorty_pagination_and_data_extraction/thread_characters.csv', index=False)     


stop = perf_counter()

print('Time taken:',stop-start) #Time taken: 2.9112066000016057