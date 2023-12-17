import time
from zipfile import ZipFile
import requests
from os import remove


def main():
    base_url = 'https://sistema.lksh.ru/static/upload/entrance-exam-pdfs/{data}.pdf'
    print('Начать парсинг ссылки https://sistema.lksh.ru/static/upload/entrance-exam-pdfs/{data}.pdf? \n 1.Да\n 2.Выход')
    print('Введите 1 или 2:')
    answer = input()

    if answer not in ('1', '2'):
        print('Неверная команда')
        return main()

    if answer == '2':
        return

    if answer == '1':
        return parser(base_url)


def parser(base_url):
    for i in range(1, 1000):
        answer = requests.get(base_url.format(data=i))
        if answer.status_code != 200:
            pass
        else:
            with open(f'file_{i}.pdf', 'wb') as f:
                f.write(answer.content)
            f.close()
            with ZipFile("files.zip", "a") as myzip:
                myzip.write(f'file_{i}.pdf')
            myzip.close()
            remove(f"file_{i}.pdf")
        time.sleep(1)


if __name__ == '__main__':
    main()
