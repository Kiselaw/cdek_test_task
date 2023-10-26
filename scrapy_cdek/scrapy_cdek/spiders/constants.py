# UUID всех городов
CITY_IDS = {
    'Москва': '01581370-81f3-4322-9a28-3418adfabd97',
    'Санкт-Петербург': '901944f4-dbd1-4308-9cc7-d1fbbd858804',
    'Краснодар': 'f6a3a644-972c-45da-936c-10c42e78ba88',
    'Екатеринбург': '29e2321a-5c89-42ac-962e-b68d4c3e192d',
    'Новосибирск': 'c7d193aa-2716-452a-ac09-ea37dc2b3328',
    'Ростов-на-Дону': '5822adf9-43c9-4dda-96bc-219bc3776c53',
    'Владивосток': '13898ade-be5f-49b6-bbb4-6aa5f7ed8e1b',
    'Нижний Новгород': 'b7af1c1b-b82c-464d-b744-e12ce0ff5f98',
    'Казань': '6e546849-b0ac-471a-8ee2-59def7562cc6',
    'Воронеж': '1826d574-0f45-42be-9aa3-d9b19f3c72d0',
    'Сочи': '03f6c4dd-b410-4f1f-817a-444894bc58f8',
    'Хабаровск': 'fd4be918-59c5-4856-bd16-907ce76d15a7',
    'Калининград': '3d4b35fd-8f18-4fa6-a701-2b420257b1ab',
    'Самара': '40bddac8-c015-4a1f-bf2e-98061a4baef5',
    'Челябинск': '386b1029-a3b1-47d6-8831-e615136e4018',
    'Красноярск': 'ea2843de-9a17-4826-933c-f763b2e152f8',
}

# Все требуемые направления для посылок
DESTINATIONS = [
    (CITY_IDS['Москва'], CITY_IDS['Москва']),
    (CITY_IDS['Москва'], CITY_IDS['Санкт-Петербург']),
    (CITY_IDS['Санкт-Петербург'], CITY_IDS['Москва']),
    (CITY_IDS['Санкт-Петербург'], CITY_IDS['Санкт-Петербург']),
    (CITY_IDS['Москва'], CITY_IDS['Краснодар']),
    (CITY_IDS['Москва'], CITY_IDS['Екатеринбург']),
    (CITY_IDS['Москва'], CITY_IDS['Новосибирск']),
    (CITY_IDS['Москва'], CITY_IDS['Ростов-на-Дону']),
    (CITY_IDS['Москва'], CITY_IDS['Владивосток']),
    (CITY_IDS['Москва'], CITY_IDS['Нижний Новгород']),
    (CITY_IDS['Новосибирск'], CITY_IDS['Москва']),
    (CITY_IDS['Москва'], CITY_IDS['Казань']),
    (CITY_IDS['Екатеринбург'], CITY_IDS['Москва']),
    (CITY_IDS['Москва'], CITY_IDS['Воронеж']),
    (CITY_IDS['Москва'], CITY_IDS['Сочи']),
    (CITY_IDS['Москва'], CITY_IDS['Хабаровск']),
    (CITY_IDS['Краснодар'], CITY_IDS['Москва']),
    (CITY_IDS['Москва'], CITY_IDS['Калининград']),
    (CITY_IDS['Москва'], CITY_IDS['Самара']),
    (CITY_IDS['Москва'], CITY_IDS['Челябинск']),
    (CITY_IDS['Москва'], CITY_IDS['Красноярск']),
]

# Параметры посылки и вес, а также буквенные обозначения ячеек в excel документе
# Их таким образом удобно привязять к запросу по весу, что упрощает заполнение таблице в результате
WEIGHTS = [
    (10, 10, 10, 0.5, ('C', 'D', 'E')),
    (10, 10, 10, 1, ('F', 'G', 'H')),
    (10, 10, 10, 2, ('I', 'J', 'K')),
    (15, 15, 15, 3, ('L', 'M', 'N')),
    (15, 15, 15, 4, ('O', 'P', 'Q')),
    (15, 15, 15, 5, ('R', 'S', 'T')),
    (20, 20, 20, 20, ('U', 'V', 'W')),
]

# Строка, с которой начинается заполнение excel таблицы
STARTING_ROW = 5

# API для получения срока доставки
DLV_DAYS_API = 'https://www.cdek.ru/api-lkfl/estimateV2/'

# API для получения информации по тарифам (цены)
TRF_INFO_API = 'https://www.cdek.ru/api-lkfl/getTariffInfo/'

# Длину специально под PEP не подстраивал, дабы форматирование не помешало осуществлению запросов
# Тело POST запроса для получения UUID типа доставки и ее сроков
DLV_DAYS_BODY = '{{"payerType":"sender","currencyMark":"RUB","senderCityId":"{sender_city_id}","receiverCityId":"{receivier_city_id}","packages":[{{"height":{height},"length":{length},"width":{width},"weight":{weight}}}]}}'

# Тело POST запроса для получения информации по тарифу, можно увидеть настройки по дополнитльным сервисам
TRF_INFO_BODY = '{{"withoutAdditionalServices":0,"serviceId":"{service_id}","mode":"HOME-HOME","payerType":"sender","currencyMark":"RUB","senderCityId":"{sender_city_id}","receiverCityId":"{receivier_city_id}","packages":[{{"height":{height},"length":{length},"width":{width},"weight":{weight}}}],"additionalServices":[{{"alias":"insurance","arguments":[{{"name":"insurance_declaredCost","type":"money","title":"Объявленная стоимость","placeholder":"Введите сумму","minValue":999,"maxValue":null,"value":"5000"}}]}},{{"alias":"greenEnvelopeCdek","arguments":[{{"name":"greenEnvelopeCdekcount","type":"integer","title":"Количество","placeholder":"шт.","minValue":null,"maxValue":null,"value":1}}]}},{{"alias":"bubbleWrap","arguments":[{{"name":"bubbleWrap_length","type":"double","title":"Количество метров","placeholder":"метры","minValue":null,"maxValue":null,"value":1}}]}}]}}'

# Заголовки, которые нужны для осуществления POST запросов
DLV_DAYS_HEADERS = headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
}
# Путь до файла с результатом
FILE_PATH = '..//res_doc.xlsx'
