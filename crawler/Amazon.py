from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymysql
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

# 제품 데이터 수집 함수
def get_product_data(driver):
    products = driver.find_elements(By.XPATH, "//*[@id='ProductGrid-C9vh1r9haz']/div/div/div/div/ul/li")
    product_data = []
    hrefs = []

    for product in products:
        try:
            name = product.find_element(By.XPATH, "./div[2]/div[4]/div[1]/div[1]/a").text
            image_url = product.find_element(By.XPATH, ".//./div[2]/div[3]/div[1]/div[2]/img").get_attribute("src")
            href = product.find_element(By.XPATH, "./div[1]/a").get_attribute("href")
            
            hrefs.append(href)
            
            print("product name:", name)
            print("href:", href)
            break
        except Exception as e:
            print(f"Error retrieving product data: {e}")

    for href in hrefs:
        try:
            # 상세 페이지에서 얻는 detail
            driver.get(href)
            # 페이지 로딩 대기
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "detailBulletsWrapper_feature_div"))
            )
            category = driver.find_element(By.XPATH, "//*[@id='detailBulletsWrapper_feature_div']/ul[1]/li/span").text
            subcategory = driver.find_element(By.XPATH, "//*[@id='detailBulletsWrapper_feature_div']/ul[1]/li/span/ul/li/span").text
            print("category:", category)
            print("subcategory:", subcategory)
            # # TODO: category rank parsing
            rank = category
            # # TODO: subcategory rank parsing
            category_rank = subcategory

            price = driver.find_element(By.XPATH, "//*[@id='detailBulletsWrapper_feature_div']/ul[1]/li/span/span").get_attribute('data-testid')
            review_cnt = driver.find_element(By.XPATH, "//*[@id='acrCustomerReviewText']").text
            rating = driver.find_element(By.XPATH, "//*[@id='acrPopover']/span[1]/a/span").text
            # # TODO: get to know is_soldout
            store = "Amazon"
            # # TODO: get keyword from reviews

            product_data.append({
                'name': name,
                'category': category,
                'subcategory': subcategory,
                'price': price,
                'review_cnt': review_cnt,
                'image_url': image_url,
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
            # 'name': name,
            #     'category': category,
            #     'subcategory': subcategory,
            #     'price': price,
            #     'review_cnt': review_cnt,
            #     'image_url': image_url,
            #     'rating': rating,
            #     'store': store
            cursor.execute("""
                INSERT INTO product (name, category, subcategory,
                    price, review_cnt, image_url, rating, store)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (item['name'], item['category'], item['subcategory']
                , item['price'], item['review_cnt'], item['image_url']
                , item['rating'], item['store']))
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