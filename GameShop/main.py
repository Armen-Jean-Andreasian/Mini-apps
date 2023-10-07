import os
import re
import shutil
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class Parser:
    URL = 'https://plati.market/seller/cyber-store/1063038/'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 ' \
                 'Safari/537.36'

    REQUEST_HEADER = {
        'User-Agent': USER_AGENT,
        'Accept-Language': 'en-US, en;q=0.5'
    }

    @staticmethod
    def parse_website():
        response = requests.get(url=Parser.URL, headers=Parser.REQUEST_HEADER)
        html = response.content

        if html:
            if os.path.isfile(os.path.join(os.curdir, 'parsed-html.txt')):
                current_time = str(datetime.now())[:-7]
                print('Making backup...')

                shutil.copyfile(src='parsed-html.txt',
                                dst=f'{current_time.replace(":", "-")}-backup.txt')

        with open(f'parsed-html.txt', 'wb') as file:
            file.write(html)

    @staticmethod
    def inspect_sales(parse=False):
        if parse:
            Parser.parse_website()

        with open('parsed-html.txt', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, features='html.parser')
            element = soup.find(name='div', class_="merchant-statistic")

        raw_statistics = str(element.find_all('li')[1:])
        values: list = re.findall(pattern=r'<li>(.*?)</li>', string=raw_statistics)

        for i in values:
            print(i)

    @staticmethod
    def inspect_feedback():
        with open('parsed-html.txt', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, features='html.parser')
            element = soup.find(name='div', class_="goods_reviews")

        raw_feedback = element.find(name='span', id="ResponsesBlock")
        reviews = str(raw_feedback.find_all(name='span', class_="review_info"))

        dates = re.findall(pattern=r'</i>(.*?)</span>', string=reviews)

        print(f"""Last Reviews: {str(dates)[1:-1].replace("'", '')}""")


def main():
    while True:
        main_menu = int(input('----------------\nPress: \n'
                              "1 - Parse the shop \n"
                              "2 - Get last sales \n"
                              "3 - Get last feedback \n"
                              "4 - Exit \n----------------\n> "))

        if main_menu == 1:
            question = input('Do you want to request the website? Y/N \n----------------\n> ').lower()
            if question == 'y':
                Parser.parse_website()
                Parser.inspect_sales()
                print('----------------')

        elif main_menu == 2:
            Parser.inspect_sales()
            print('----------------')

        elif main_menu == 3:
            Parser.inspect_feedback()
            print('----------------')

        elif main_menu == 4:
            break

        else:
            raise ValueError('Enter a valid number!')


if __name__ == '__main__':
    main()
    input("Press Enter to exit...")  # [fix] to keep the exe running
