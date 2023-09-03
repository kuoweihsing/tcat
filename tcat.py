# import requests
# import pandas as pd
# import xml.etree.ElementTree as ET
# from datetime import datetime

# # formatted timestamp string like 20230725204944
# timestamp_format = '%Y%m%d%H%M%S'
# # target url
# url = "https://www.t-cat.com.tw/iPhone/TCatApp.aspx"
# # header information
# headers = {
# 'User-Agent': 'BlackCat/2.45.9 (iPhone; iOS 16.6; Scale/3.00)',
# 'Host': 'www.t-cat.com.tw',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
# 'Accept-Language': 'zh-Hant-TW;q=1, ko-TW;q=0.9, en-TW;q=0.8, en-GB;q=0.7, zh-Hans-TW;q=0.6',
# 'Content-Length': '128',
# 'Cookie': 'citrix_ns_id=AAI77SDzZDsvz9cGAAAAADuVBLGLdqo1FolMO1nYAJ4fuACu8TOQ4rtlBzq7Ec6hOw==qyPzZA==GocQE5z-6a3FdGMtayX8vSqVlK0=; ASP.NET_SessionId=wxwqk44fbeccxsk1mcdslb33'
# }
# # invoicenumbers
# invoices = ['901500031731', '901524884504', '901524884484']
# # main loop starts
# for inv in invoices:
#     # payload with invoicenumber
#     payload = "ConsignmentNo={}&f=5&isForeign=N&secret=efJ%2Btl5aYOJIfiwKlatJS5iJLRE8mvarz8tRhWq61M3dX3ewqDwp6Dy9XHH0NTO5&SVC=TCATAPP".format(inv)
#     # post request
#     response = requests.request("POST", url, headers=headers, data=payload)
#     # response text
#     data = response.text
#     # find content
#     root = ET.fromstring(data)
#     # find content items
#     items = root.find("Content").findall("Item")
#     rows = []
#     for ind, item in enumerate(items):
#         status = item.find("Status").text
#         time = item.find("Time").text
#         office = item.find("Office").text
#         sdid = item.find("SDID").text
#         last_update = datetime.strptime(item.find("LastUPDateTime").text, timestamp_format)
#         rows.append({"invoicenumber": inv, "currentstatus": status, "formatted_timestamp": time, "branch": office, "sdid": sdid, "dttm": last_update, "stage": ind})
#     # transform as dataframe
#     df = pd.DataFrame(rows)
#     print(df)
#     df.to_excel('data_{}.xlsx'.format(inv), index=False)

import aiohttp
import asyncio
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

timestamp_format = '%Y%m%d%H%M%S'
url = "https://www.t-cat.com.tw/iPhone/TCatApp.aspx"
headers = {
    'User-Agent': 'BlackCat/2.45.9 (iPhone; iOS 16.6; Scale/3.00)',
    'Host': 'www.t-cat.com.tw',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept-Language': 'zh-Hant-TW;q=1, ko-TW;q=0.9, en-TW;q=0.8, en-GB;q=0.7, zh-Hans-TW;q=0.6',
    'Content-Length': '128',
    'Cookie': 'YOUR_COOKIE_HERE'
}
invoices = ['901500031731', '901524884504', '901524884484']

async def fetch_invoice_data(inv):
    async with aiohttp.ClientSession() as session:
        payload = "ConsignmentNo={}&f=5&isForeign=N&secret=efJ%2Btl5aYOJIfiwKlatJS5iJLRE8mvarz8tRhWq61M3dX3ewqDwp6Dy9XHH0NTO5&SVC=TCATAPP".format(inv)
        async with session.post(url, headers=headers, data=payload) as response:
            data = await response.text()
            root = ET.fromstring(data)
            items = root.find("Content").findall("Item")
            rows = []
            for ind, item in enumerate(items):
                status = item.find("Status").text
                time = item.find("Time").text
                office = item.find("Office").text
                sdid = item.find("SDID").text
                last_update = datetime.strptime(item.find("LastUPDateTime").text, timestamp_format)
                rows.append({"invoicenumber": inv, "currentstatus": status, "formatted_timestamp": time, "branch": office, "sdid": sdid, "dttm": last_update, "stage": ind})
            df = pd.DataFrame(rows)
            print(df)

async def main():
    start_dttm = datetime.now()
    tasks = [fetch_invoice_data(inv) for inv in invoices]
    await asyncio.gather(*tasks)
    end_dttm = datetime.now()
    print(start_dttm)
    print(end_dttm)

if __name__ == '__main__':
    asyncio.run(main())
