# FindEmpty
# JiggingPro 판매 아이템의 품절 세부 품목을 확인한다.
# 자동으로 정기적으로 Data로 수집해서 excel로 저장하고
# 특이점이 있을때는 메일로 자동 전송 하는 것

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def main():
    service = Service(executable_path="C:\dev\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    title = driver.title
    print(title)
    driver.implicitly_wait(0.5)

    #구글 검색어로 selenium입력해서 서치 클릭
    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")
    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"
    print(value)

    c_url = driver.current_url
    print(c_url)
    driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")
    # time.sleep(1)
    # driver.get("http://www.naver.com")
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)
    # driver.forward()
    # time.sleep(1)
    # driver.refresh()
    # time.sleep(1)
    # driver.find_element(By.LINK_TEXT, "See an example alert").click()
    # alert = wait.until()

    # driver.get("https://smartstore.naver.com/bigyellowtail/products/6245277566")
    # e = driver.find_element(By.CLASS_NAME, "bd_3psJk")
    # e.click()
    # t = e.text
    # print(t)

    # 옵션 첫번째 클래스 이름은 bd_3psJk
    # 모든 상품이 은 클래스 이름을 사용한다.
    driver.get("https://smartstore.naver.com/bigyellowtail/products/4837709503")
    e = driver.find_element(By.CLASS_NAME, "bd_3psJk")
    e.click()
    t = e.text
    print(t)

    e = driver.find_element(By.CLASS_NAME, "bd_3psJk")
    e.click()
    t = e.text
    print(t)




    time.sleep(3)
    # while True:
    #     pass

    driver.quit()








def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.

# main 함수 호출
if __name__ == '__main__':
    main()


