import threading
import requests
import time

def download(url):
    print(f"Starting to Download {url}")
    resp = requests.get(url)
    print(f"Completed Downloading {url}, size: {len(resp.content)} byptes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url, )) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")

