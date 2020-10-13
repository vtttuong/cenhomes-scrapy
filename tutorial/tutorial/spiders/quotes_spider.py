import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        frmdata = {"MaThuaDat":'267400010001'}
        url = "https://sqhkt-qlqh.tphcm.gov.vn/computing/930/api/v3.1/a-z/all"
        yield scrapy.FormRequest(url, method='POST', callback=self.parse, formdata=frmdata)

    def parse(self, response):
        filename = f'quotes.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')