from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

KAKAO_LOGIN_PAGE = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fis_popup%3Dfalse%26ka%3Dsdk%252F1.43.0%2520os%252Fjavascript%2520sdk_type%252Fjavascript%2520lang%252Fen-US%2520device%252FMacIntel%2520origin%252Fhttps%25253A%25252F%25252Fwww.tistory.com%26auth_tran_id%3Dn11fn9p740o3e6ddd834b023f24221217e370daed18l9ms8up0%26response_type%3Dcode%26state%3DaHR0cHM6Ly93d3cudGlzdG9yeS5jb20v%26redirect_uri%3Dhttps%253A%252F%252Fwww.tistory.com%252Fauth%252Fkakao%252Fredirect%26through_account%3Dtrue%26client_id%3D3e6ddd834b023f24221217e370daed18&talk_login=hidden'


class SeleniumClient:
    def __init__(self, sleep_time=3, is_hide=True):
        self.t = sleep_time

        print('[진행중] Selenium 준비중...')

        options = webdriver.ChromeOptions()
        if is_hide:
            # options.add_argument("headless")  # 창 숨기기
            options.add_argument("no-sandbox")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")  # for google 로그인 화면

        options.add_argument("window-size=1920,1080")
        
        # web driver 시작
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
