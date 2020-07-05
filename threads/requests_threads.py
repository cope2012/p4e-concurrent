import requests
import codetiming
import concurrent.futures


URLS = ['https://www.foxnews.com/',
        'https://www.cnn.com/',
        'https://www.yahoo.com/',
        'https://www.bbc.co.uk/',
        'https://www.aws.com/']


def load_url(url):
    r = requests.get(url)
    return r.content

# Single threaded program
# with codetiming.Timer():
#     for url in URLS:
#         res = load_url(url)
#         print(f'{url} page is {len(res)} bytes')


# Multi-threaded program
with codetiming.Timer():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print(f'generated exception in url: {url}, error: {e}')
            else:
                print(f'{url} page is {len(data)} bytes')
