# Автотесты для effective-mobile.ru

## Установка
pip install -r dependencies.txt
playwright install

## Запуск тестов
pytest --alluredir=allure-results

## Docker
Сборка:
docker build -t effective-tests .

Запуск:
docker run --rm effective-tests

## Технологии
Python 3.10
Playwright
Pytest
Allure
Docker
