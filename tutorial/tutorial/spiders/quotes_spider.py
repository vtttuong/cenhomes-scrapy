import scrapy
import json
from pandas import json_normalize
from json_excel_converter import Converter 
from json_excel_converter.xlsx import Writer
import time

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    objList = []
    def start_requests(self):
        #frmdata = {"MaThuaDat":'267400010001'}
        frmdata = {"MaThuaDat":'267370390093'}
                                
        url = "https://sqhkt-qlqh.tphcm.gov.vn/computing/930/api/v3.1/a-z/all"
        # https://sqhkt-qlqh.tphcm.gov.vn/api/qhpksdd/7580
        for i in range(10,11):
            frmdata["MaThuaDat"] = '2673703900' + str(i)
            yield scrapy.FormRequest(url, method='POST', callback=self.parse, formdata=frmdata)
            time.sleep(1)
            
        print(self.objList)    
        with open('objList.json', 'w') as json_file:
            json.dump(self.objList, json_file)

    def parse(self, response):
        filename = f'quyhoach.json'
        obj = {
            "MaThuaDat":"",
            "SoTo":"",
            "SoThua":"",
            "DiaChi":{
                "PhuongXa":"",
                "QuanHuyen":"",
                "TinhThanh":""
            },
            "DienTichLoDat":"",
            "ToaDo":{
                "Lat":"",
                "Long":""
            },
            "LoGioi":[
                {
                    "Duong":"",
                    "GiaTri":""
                },
                {
                    "Duong":"",
                    "GiaTri":""
                },
            ],
            "QHSuDungDat":[]
        }
        data_str = response.json()["QHPK"]
        data = json.loads(data_str)
        self.log(type(data))
        for x in data:
            y = {}
            y["ChucNang"] = x["properties"]["chucnang"]
            y["DienTich"] = x["properties"]["dientich"]
            obj["QHSuDungDat"].append(y)

        self.objList.append(obj)
    
        # with open('obj.json', 'w') as json_file:
        #     json.dump(obj, json_file)

        # conv = Converter()
        # conv.convert(obj, Writer(file='test.xlsx'))

        # data_str = response.json()["ThongTinChung"]
        # data = json.loads(data_str)
        # ranh = data["ranh"]
        # ranh = json.loads(ranh)
        # self.log(len(ranh[0][0]))
        # lat = 0
        # lon = 0
        # for x in ranh[0][0]:
        #     lat += x[0]
        #     lon += x[1]
        # self.log("lat = " + str(lat/len(ranh[0][0])))
        # self.log("lon = " + str(lon/len(ranh[0][0])))
        # self.log(str(lon/len(ranh[0][0]))+","+str(lat/len(ranh[0][0])))
        # self.log(type(data))
        # self.log(type(data["dsdoan"]))
        # self.log(data["dsdoan"][0])
        
        # data_str = response.json()["LoGioi"]
        # data = json.loads(data_str)
        # self.log(type(data))
        # # self.log(type(data["dsdoan"]))
        # self.log(data["dsdoan"][0])
        # json_str = json.dumps(data)   
        # resp = json.loads(json_str)
        #self.log(type(data))
        #self.log(len(data))
        # with open('1.txt', 'wb') as f1:
        #     f1.write(resp)
        
        # df = json_normalize(data)
        # # Writing Excel File:
        # df.to_excel('Airlines1.xlsx')

        with open(filename, 'wb') as f:
            f.write(data_str.encode())
        self.log(f'Saved file {filename}')

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')