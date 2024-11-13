from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from forex_python.converter import CurrencyRates
import time
import pymysql
import re
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# MySQL 연결 설정
def connect_to_db():
    hostname = os.getenv("DB_HOST")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    dbname = os.getenv("DB_NAME")

    connection = pymysql.connect(
        host = hostname,
        user = username,
        password = password,
        db = dbname,
        charset = 'utf8'
    )

    return connection

# 가격 처리 함수
def clean_price(price_text):
    # '$', '\n' 제거 후 공백을 없앰
    cleaned_text = price_text.replace('$', '').replace('\n', '').strip()
    
    # 두 부분을 분리하여 소수점으로 합침
    if len(cleaned_text) > 2:
        dollars = cleaned_text[:-2]  # 마지막 두 자리를 제외한 부분 (달러)
        cents = cleaned_text[-2:]    # 마지막 두 자리 (센트)
        return f"{dollars}.{cents}"
    else:
        return cleaned_text

# 제품 데이터 수집 함수
def get_product_data(driver):
    products = driver.find_elements(By.XPATH, "//*[@id='ProductGrid-C9vh1r9haz']/div/div/div/div/ul/li")
    product_data = []
    hrefs = []

    for product in products:
        try:
            href = product.find_element(By.XPATH, "./div[1]/a").get_attribute("href")
            hrefs.append(href)
        except Exception as e:
            print(f"Error retrieving product data: {e}")

    for href in hrefs:
        try:
            # 상세 페이지에서 얻는 detail
            driver.get(href)
            print("href:", href)

            IDs = [
                "corePriceDisplay_desktop_feature_div",
                "detailBulletsWrapper_feature_div",
            ]

            # 페이지 로딩 대기
            for ID in IDs:
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, ID))
                    )
                except (NoSuchElementException, TimeoutException):
                    continue

            name = driver.find_element(By.XPATH, "//*[@id='productTitle']").text
            image_url = driver.find_element(By.XPATH, "//*[@id='landingImage']").get_attribute("src")

            # rank와 category parsing
            text = driver.find_element(By.XPATH, "//*[@id='detailBulletsWrapper_feature_div']/ul[1]/li/span").text
            rank_match = re.search(r'#([\d,]+) in', text)
            category_match = re.search(r'in (.*?) \(', text)

            category = category_match.group(1) if category_match else None
            rank = int(rank_match.group(1).replace(',', '')) if rank_match else None

            text = driver.find_element(By.XPATH, "//*[@id='detailBulletsWrapper_feature_div']/ul[1]/li/span/ul/li/span").text
            subrank_match = re.search(r'#(\d+) in', text)
            subcategory_match = re.search(r'in (.+)', text)
            subcategory = subcategory_match.group(1) if subcategory_match else None
            category_rank = int(subrank_match.group(1).replace(',', '')) if rank_match else None

            # 기타 세부 항목
            review_match = re.search(r'[\d,]+', driver.find_element(By.XPATH, "//*[@id='acrCustomerReviewText']").text)
            # TODO: 한번씩 price 값 못 가져오는 것 해결

            price = float(clean_price(driver.find_element(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]").text))
            review_cnt = int(review_match.group(0).replace(',', ''))
            rating = driver.find_element(By.XPATH, "//*[@id='acrPopover']/span[1]/a/span").text
            # TODO: get to know is_soldout
            store = "Amazon"
            # TODO: get keyword from reviews

            product_data.append({
                'name': name,
                'category': category,
                'subcategory': subcategory,
                'price': price,
                'review_cnt': review_cnt,
                'image_url': image_url,
                'rank': rank,
                'category_rank': category_rank,
                'rating': rating,
                'store': store
            })
        except Exception as e:
            print(f"Error retrieving product data: {e}")

    return product_data

# 데이터 저장 함수
def store_data(data):
    connection = connect_to_db()
    cursor = connection.cursor()

    for item in data:
        try:
            price = float(item['price']) if item['price'] else 0.0
            review_cnt = int(item['review_cnt']) if item['review_cnt'] else 0
            rating = float(item['rating']) if item['rating'] else 0.0
            cate_rank = int(item['rank']) if item['rank'] else 0
            subcate_rank = int(item['category_rank']) if item['category_rank'] else 0

            cursor.execute("""
            INSERT INTO product (name, category, subcategory, price, review_cnt
                , image_url, cate_rank, subcate_rank, rating, store)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            item['name'],
            item['category'],
            item['subcategory'],
            price,
            review_cnt,
            item['image_url'],
            cate_rank,
            subcate_rank,
            rating,
            item['store']
        ))
        except Exception as e:
            print(f"Error storing data: {e}")

    print("[완료]: 데이터 저장 완료")
    connection.commit()
    cursor.close()
    connection.close()

# SeleniumClient 클래스 정의
class SeleniumClient:
    def __init__(self, sleep_time=3, is_hide=True):
        self.t = sleep_time

        print('[진행중] Selenium 준비중...')

        options = webdriver.ChromeOptions()
        if is_hide:
            options.add_argument("headless")  # 창 숨기기
        options.add_argument("no-sandbox")
        options.add_argument("window-size=1920,1080")

        # 웹 드라이버 시작
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except:
            self.driver = webdriver.Chrome(options=options)
        
        print('[진행중] Selenium Chrome WebDriver 시작.. ')
        self.driver.implicitly_wait(self.t)

    def quit(self):
        self.driver.quit()

# Selenium 웹드라이버 설정 및 데이터 수집
def main():
    client = SeleniumClient(sleep_time=3, is_hide=True)  # 창을 보이게 하려면 False로 설정
    url = "https://www.amazon.com/stores/page/7340A8C9-7D87-4654-9DB9-8AA0C903F2C7"
    
    client.driver.get(url)
    time.sleep(3)  # 페이지 로딩 대기

    data = get_product_data(client.driver)
    store_data(data)  # 데이터 저장
    
    client.quit()

if __name__ == "__main__":
    main()