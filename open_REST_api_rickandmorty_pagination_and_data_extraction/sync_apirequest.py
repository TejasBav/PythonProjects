from time import perf_counter
import requests
import pandas as pd

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

start = perf_counter()

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


data = main_request(base_url, endpoint, 1)

main_list = []



for x in range(1,get_pages(data)+1):
    main_list.extend(parse_json(main_request(base_url, endpoint, x)))

final = pd.DataFrame(main_list)


print(final.head(), final.tail())

final.to_csv('./open_REST_api_rickandmorty_pagination_and_data_extraction/sync_characters.csv', index=False)

stop = perf_counter()

print('time taken:', stop - start) #Time taken: 20.450044099998195

#open_REST_api_rickandmorty_pagination_and_data_extraction