# import scrapy
import json
import openpyxl
from scrapy import Request, Spider
from .constants import *  # Не совсем по PEP, но в данном случае это некритично


class CdekExpressSpider(Spider):
    name = "cdek_express"
    handle_httpstatus_list = [422]
    custom_settings = {
        'DOWNLOAD_TIMEOUT': 60,
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        'DOWNLOAD_DELAY': 0.5,
    }

    def start_requests(self):
        """Для каждого направления по каждому весу осуществляет запросы к API."""
        for row, destination in enumerate(DESTINATIONS, STARTING_ROW):
            for weight in WEIGHTS:
                body = DLV_DAYS_BODY.format(sender_city_id=destination[0],
                                            receivier_city_id=destination[1],
                                            height=weight[0], length=weight[1], width=weight[2], weight=weight[3])
                body = json.dumps(json.loads(body))
                yield Request(url=DLV_DAYS_API,
                              method='POST',
                              headers=DLV_DAYS_HEADERS,
                              body=body,
                              callback=self.parse,
                              meta={'passed_data': {'sender': destination[0], 'receiver': destination[1],
                                                    'height': weight[0], 'length': weight[1], 'width': weight[2],
                                                    'weight': weight[3], 'row': str(row),
                                                    'cells': weight[4]}},
                              dont_filter=True)

    def parse(self, response):
        """Получает данные с первого API url: UUID сервиса доставки и сроки доставки."""
        res = response.json()
        pd = response.meta['passed_data']
        # Цикл находит UUID первой попавшейся экспресс-доставки от двери до двери
        # Это необходимо, чтобы получить корректный UUID сервиса, поскольку не для всех направлений есть выбор времени
        # Для тех, у которых выбор времени есть, будет браться тот, где время наиболее раннее
        for tariff in res['data'][-1]['tariffs']:
            if tariff['mode'] == 'HOME-HOME':
                service_id = tariff['serviceId']
                min_days = tariff['durationMin']
                max_days = tariff['durationMax']
                break
        body = TRF_INFO_BODY.format(service_id=service_id,
                                    sender_city_id=pd['sender'],
                                    receivier_city_id=pd['receiver'],
                                    height=pd['height'], length=pd['length'], width=pd['width'], weight=pd['weight'])
        body = json.dumps(json.loads(body))
        yield Request(url=TRF_INFO_API,
                      method='POST',
                      headers=DLV_DAYS_HEADERS,
                      body=body,
                      callback=self.parse_tarriff,
                      meta={'row': pd['row'], 'cells': pd['cells'], 'min_days': min_days, 'max_days': max_days},
                      dont_filter=True)

    def parse_tarriff(self, response):
        """Получает данные со второго API url, а именно - цену, и записывает итоговые данные в excel таблицу."""
        res = response.json()
        row = response.meta['row']  # Получаем номер строки
        min_days = response.meta['min_days']  # Получаем минимальное кол-во дней
        max_days = response.meta['max_days']  # Получаем максимальное кол-во дней
        cells = response.meta['cells']  # Получаем буквенное обозначение столбцов
        price = res['data']['totalCost']
        workbook = openpyxl.load_workbook(FILE_PATH)
        sheet = workbook['Express']
        # Формируем ссылку на ячейки из номера строки и буквенных обозначений
        sheet[cells[0] + row] = price
        sheet[cells[1] + row] = min_days
        sheet[cells[2] + row] = max_days
        workbook.save(FILE_PATH)
        workbook.close()
