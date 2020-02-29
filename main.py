from bs4 import BeautifulSoup
from request import get_html
from saver import save
import os, time

user = input('Введите имя пользователя ПК:\n')
URL = 'https://finance.ua/ru/currency'
PATH = 'C:/Users/'+user+'/Desktop/vaults.csv'

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print('='*50)
        print('[+]Соединение установлено.')
        print('=' * 50)
        print('Курс валют получен.')
        print("Записываю в файл.")
        vaults = content(html.text)
        try:
            save(vaults, PATH)
            os.startfile(PATH)
            print('=' * 50)
            print('[+]Информация сохранена на рабочий стол.')
            print('=' * 50)
            time.sleep(1.5)
        except:
            print("Неверно введено имя пользователя.")
    else:
        print('=' * 50)
        print('[-]Ошибка.')
        print('=' * 50)

def content(html):
    soup = BeautifulSoup(html, 'html.parser')
    vaults = []
    vaults_row = soup.find_all('tr', class_='major')
    for vault in vaults_row:
        vaults.append({
            'name': vault.find('td', class_='c1').get_text(),
            'buy': vault.find('td', class_='c2').get_text(),
            'sell': vault.find('td', class_='c3').get_text(),
        })
    lenght = len(vaults)
    lenght = int(lenght/2)
    return vaults[:lenght]

parse()