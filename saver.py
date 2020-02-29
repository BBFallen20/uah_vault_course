import csv


def save(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Валюта', 'Покупка', 'Продажа'])
        for item in items:
            writer.writerow([item['name'], item['buy'], item['sell']])