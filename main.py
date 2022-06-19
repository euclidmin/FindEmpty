# FindEmpty
# JiggingPro 판매 아이템의 품절 세부 품목을 확인한다.
# 자동으로 정기적으로 Data로 수집해서 excel로 저장하고
# 특이점이 있을때는 메일로 자동 전송 하는 것

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

    driver.quit()








def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.

# main 함수 호출
if __name__ == '__main__':
    main()


