import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "cenhome"
    
    def start_requests(self):
        url = 'https://gapi.cenhomes.vn/g-data-collection/v1/api/dia-chi-cu-the/get-info/540030'

        headers = {
            "authority": "gapi.cenhomes.vn",
            "accept": "application/json, text/plain, */*",
            "authorization": "Finger PT5uQ3M9Qj9AQj5Ec0VxPUY+QT5vRHM+bkJCQEM+b0NuQUVEcW9xcj5xbz9B",
            "datetime": "10/13/2020, 3:34:04 PM",
            "finger": "PT5uQ3M9Qj9AQj5Ec0VxPUY+QT5vRHM+bkJCQEM+b0NuQUVEcW9xcj5xbz9B",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "origin": "https://gianhadat.cenhomes.vn",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://gianhadat.cenhomes.vn/",
            "accept-language": "en-US,en;q=0.9"
        }

        yield scrapy.Request(
            url=url,
            method='GET',
            dont_filter=True,
            headers=headers,
        )

    def parse(self, response):
        filename = f'cenhome.json'
        #data = json.loads(response.body)
        data = response.json()["payload"]["data"]
        self.log(data["batDongSanDTO"]["id"])
        with open(filename, 'wb') as f:
            f.write(data)
        self.log(type(response))
        self.log(f'Saved file {filename}')

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')