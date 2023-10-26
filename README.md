# Тестовое задание в CDEK Digital

# Cтек

- Python 3.11.1
- Scrapy 2.11.0

## Запуск и проверка

Для проверки задания необходимо создать виртуальное окружение и установить зависимости с помощью следующих команд:

**Создание виртуального окружения и его активация (необходимо находиться в директории с окружением)**: 

Windows:
```bash
py -3 -m venv env 
```
```bash
. venv/Scripts/activate
```
macOS/Linux:
```bash
python3 -m venv .venv
```
```bash
source env/bin/activate
```
**Установка зависимостей**:
```bash
pip install -r requirements.txt
```
**Запуск паука и парсинг данных**:
```bash
scrapy crawl cdek_express
```

## Справка

В директории задания лежит файл - rec_doc.xlsx, это подготовленный мной файл-шаблон для заполнения данными.
После отработки парсера данные появятся там. 

Для каждого веса настройки по дополнительным сервисам такие: 

- Объявленная цена - 5000 руб. 
- Упаковка -> Почтовые пакеты и конверты -> Конверт зеленый CDEK, 1 шт.
- Дополнительные упаковочные материалы -> Воздушно-пузырчатая пленка (10мм, 1,2х50м), 1 шт.

Все размеры посылок указаны в констаннте WEIGHTS. 

P.S. Базовые файлы сопутствующие созданию scrapy проекта специально не убрал, вдруг еще придется использовать :) 
