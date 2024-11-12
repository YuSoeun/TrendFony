from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import jaydebeapi
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# PostgreSQL 연결 설정
def connect_to_db():
    db_name = os.getenv("DB_NAME")
    jdbc_url = f"jdbc:h2:~/{db_name};AUTO_SERVER=TRUE"
    driver = "org.h2.Driver"

     # H2 JDBC 드라이버의 경로를 지정해야 합니다.
    h2_jar_path = "~/Desktop/project/h2/bin/h2-2.1.214.jar"  # H2 JDBC 드라이버 JAR 파일의 경로

    # JayDeBeApi를 사용하여 H2 데이터베이스 연결
    connection = jaydebeapi.connect(
        driver, 
        jdbc_url, 
        [os.getenv("DB_USER"), os.getenv("DB_PASSWORD")],
        h2_jar_path
    )

# 제품 데이터 수집 함수
def get_product_data(driver):
    products = driver.find_elements(By.XPATH, "//div[@class='s-product-container']")
    product_data = []

    for product in products:
        try:
            name = product.find_element(By.XPATH, ".//h2").text
            price = product.find_element(By.XPATH, ".//span[contains(@class,'a-price')]").text
            rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
            reviews = product.find_element(By.XPATH, ".//span[@class='a-size-base']").text
            
            product_data.append({
                'name': name,
                'price': price,
                'rating': rating,
                'reviews': reviews
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
            cursor.execute("""
                INSERT INTO products (name, price, rating, reviews)
                VALUES (%s, %s, %s, %s)
            """, (item['name'], item['price'], item['rating'], item['reviews']))
        except Exception as e:
            print(f"Error storing data: {e}")

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