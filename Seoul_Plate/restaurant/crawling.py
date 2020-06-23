import requests
from bs4 import BeautifulSoup

from restaurant.models import Rest


class crawling:
    from selenium import webdriver

    # 망고플레이트 성수동 검색 결과 하단 다음페이지 모음
    search_paging_array = [
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=1',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=2',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=3',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=4',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=5',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=6',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=7',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=8',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=9',
        'https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99?keyword=%EC%84%B1%EC%88%98%EB%8F%99&page=10',
    ]

    driver = webdriver.Chrome('/Users/parkjuheoung/Downloads/chromedriver')
    driver.implicitly_wait(3)

    driver.get('https://www.mangoplate.com/search/%EC%84%B1%EC%88%98%EB%8F%99')

    # 식당 상세페이지 url get
    for page_index in range(len(search_paging_array)):
        driver.get(search_paging_array[page_index])
        for val in driver.find_elements_by_xpath(
                '/html/body/main/article/div[2]/div/div/section/div[3]/ul/li/div/figure/a'):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
            }
            url = val.get_attribute('href')
            print(url)
            html = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')
            if soup.find(class_='restaurant_name'):
                rest_name = soup.find(class_='restaurant_name').text.strip().replace('\n', '')
            else:
                rest_name = None
            if soup.find(class_='rate-point'):
                rest_star = soup.find(class_='rate-point').text.strip().replace('\n', '')
            else:
                rest_star = None
            if soup.select_one('.info>tbody>tr:nth-child(1)>td'):
                rest_address = soup.select_one('.info>tbody>tr:nth-child(1)>td').text.strip().replace('\n', ' ')
            else:
                rest_address = None
            if soup.select_one('.info>tbody>tr:nth-child(3)>td'):
                rest_food = soup.select_one('.info>tbody>tr:nth-child(3)>td').text.strip().replace('\n', ' ')
            else:
                rest_food = None
            if soup.select_one('.info>tbody>tr:nth-child(2)>td'):
                rest_phone_number = soup.select_one('.info>tbody>tr:nth-child(2)>td').text.strip().replace('\n', ' ')
            else:
                rest_phone_number = None
            if soup.select_one('.info>tbody>tr:nth-child(4)>td'):
                rest_sale = soup.select_one('.info>tbody>tr:nth-child(4)>td').text.strip().replace('\n', ' ')
            else:
                rest_sale = None
            if soup.select_one('.info>tbody>tr:nth-child(5)>td'):
                rest_park = soup.select_one('.info>tbody>tr:nth-child(5)>td').text.strip().replace('\n', ' ')
            else:
                rest_park = None
            if soup.select_one('.info>tbody>tr:nth-child(6)>td'):
                rest_time = soup.select_one('.info>tbody>tr:nth-child(6)>td').text.strip().replace('\n', ' ')
            else:
                rest_time = None

            Rest.objects.get_or_create(
                rest_name=rest_name,
                rest_star=rest_star,
                rest_address=rest_address,
                rest_food=rest_food,
                rest_phone_number=rest_phone_number,
                rest_sale=rest_sale,
                rest_park=rest_park,
                rest_time=rest_time,
            )


a = crawling()

a
