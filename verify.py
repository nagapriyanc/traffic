import requests
import time


link = "https://www.google.in"
headers = {
            'User-Agent': 'Mozilla/6.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '

        }

resp = requests.get(link)

print(resp.url)
print(resp.status_code)
