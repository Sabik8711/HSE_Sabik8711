import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class ParcerCBRF:
    def__init__(self,url):
    self.url=url

    def start(self):
    response=requests.get(self.url)
    soup=BeautifulSoup (response.content, 'html.parser')
    table=soup.find("table", {'class:data'})
    rows=table.find.all('tr')[1:]

    data={}
    for row in rows:
     cols=row.find.all('td')
     cols=[col.text.strip() for col in cols]
     iso_date=datetime.strptime(cols(0), '%d, %m, %Y'), date().isoformat()
     cols[0]=iso_date
     date[iso_date]=cols[1]

     with open('data_1_json', 'w', encoding='utf-8') as outfile:
         json.dump(data, outfile, indent=2, ensure_ascii=False)

         print("Data written to data_1.json file.")

parser=ParserCBRF("https://www.cbr.ru/hd_base/ostat_base/?UniDbQuery.Posted=True&UniDbQuery.From=22.02.2022&UniDbQuery.To=02.10.2023")
parser.start()


class OstatData

    def__init__(self, filename):
    self.filename=filename
    with open(filename, 'r' encoding='utf-8') as infile:
        self.data=json.load(infile)

def ostat_base_by_date(self, date):
    return self.data.get(date)

def ostat_base_by_today(self):
    last_date=max(self.data.keys())
    return self.data[last_date]

def range_dates(self, from_date, to_date):
    filtered_data={}
    for key, value in self.data.items():
        date_obj=datetime.strptime(key, '%Y-%m-%d').date()
        if from_date<=date_obj<=to_date:
            filtered_data[key]=value
    sorted_data=sorted(filtered_data.items())
    return sorted_data


ostat_data=OstatData('data_1.json')
print("Данные за определенную дату: "+ostat_base_by_date('2023-09-02')) #введите дату для проверки

ostat_data=OstatData('data_1.json')
print("Данные за последнюю доступную дату:"+ostat_base_by_today())

ostat_data=OstatData('data_1.json')
range_data=ostat_data.range_dates(datetime(2022, 2, 22).date(),
                                  datetime(2023, 10, 02).date())
print("Данные за определенный период: ")
for data in range_data:
    print(data)