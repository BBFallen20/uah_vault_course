from bs4 import BeautifulSoup
from request import get_html
from saver import save
import os, time

URL = 'https://finance.ua/ru/currency'

def save_file(vaults, path):
    try:
        save(vaults, path)
        os.startfile(path)
        print('=' * 50)
        print('[+]Info saved to your desktop.')
        print('=' * 50)
    except Exception:
        print("Error with saving.Try to re-enter username.")


def parse(mode):
    html = get_html(URL)
    if html.status_code == 200:
        print('='*50)
        print('[+]Connected.')
        print('=' * 50)
        print('Vault course has been taken.')
        vaults = content(html.text)
        if mode == '1':
            user = input('Enter PC username:\n')
            PATH = 'C:/Users/' + user + '/Desktop/vaults.csv'
            save_file(vaults, PATH)
            time.sleep(1.5)
        elif mode == '2':
            print('=' * 50)
            print('[V]Results:')
            print('=' * 50)
            for item in vaults:
                print("Vault: "+str(item['name'])+' Buy: ' +str(item['buy'])+' Sell: '+str(item['sell']))
            time.sleep(1.5)
    else:
        print('=' * 50)
        print('[-]Error with connection.')
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
    return vaults

print("="*50)
print("\t\t\tUAH course parser v2.0")
print("="*50)
while True:
    mode = input('''Choose what to do:
1.Save result to desktop.
2.Show result to the console.
3.Exit.\n''')
    if mode == '1':
        parse(mode)
    elif mode == '2':
        parse(mode)
    elif mode == '3':
        exit()
    else:
        print("Unknown command.")
        continue