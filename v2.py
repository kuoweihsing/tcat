import requests
import json

url = "https://api.ship24.com/api/parcels/901524884504?lang=en"

payload = json.dumps({
  "userAgent": "",
  "os": "Mac",
  "browser": "Chrome",
  "device": "Macintosh",
  "os_version": "mac-os-x-15",
  "browser_version": "115.0.0.0",
  "deviceType": "desktop",
  "orientation": "portrait",
  "uL": "zh-TW",
  "to_check": [
    "t-cat"
  ]
})
headers = {
  'authority': 'api.ship24.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://www.ship24.com',
  'referer': 'https://www.ship24.com/',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
  'x-ship24-token': '225,150,128,44,49,54,57,52,48,57,52,52,56,54,55,48,52,44,225,150,130'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
