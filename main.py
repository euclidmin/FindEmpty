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
    # search_box = driver.find_element(by=By.NAME, value="q")
    # search_button = driver.find_element(by=By.NAME, value="btnK")
    # search_box.send_keys("Selenium")
    # search_button.click()
    #
    # search_box = driver.find_element(by=By.NAME, value="q")
    # value = search_box.get_attribute("value")
    # assert value == "Selenium"
    # print(value)


    # 옵션 첫번째 클래스 이름은 bd_3psJk
    # 모든 상품이 은 클래스 이름을 사용한다.
    driver.get("https://smartstore.naver.com/bigyellowtail/products/4837709503")
    # driver.get("https://smartstore.naver.com/bigyellowtail/products/6671966658")

    elements = driver.find_elements(By.CLASS_NAME, 'bd_3psJk')
    L1_element = elements[0]
    L1_element.click()
    L1_option_text = L1_element.text
    print(L1_option_text)

    L1_option_elements = driver.find_elements(By.CLASS_NAME, 'bd_1y1pd')
    L1_option1 = L1_option_elements[0]
    L1_option1.click()
    L1_option_text = L1_element.text
    print(L1_option_text)

    L2_element = elements[1]
    L2_element.click()
    L2_option_text = L2_element.text
    print(L2_option_text)

    search = '(품절)'
    option_list = L2_option_text.split(sep='\n')
    for option in option_list:
        if search in option:
            print(option)





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


