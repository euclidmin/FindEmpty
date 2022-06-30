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
    # driver.get("https://www.google.com")
    # title = driver.title
    # print(title)
    # driver.implicitly_wait(0.5)

    # 옵션 첫번째 클래스 이름은 bd_3psJk
    # 모든 상품이 은 클래스 이름을 사용한다.
    # driver.get("https://smartstore.naver.com/bigyellowtail/products/4837709503")
    #
    # 상품 옵션이 두가지로  구성된 경우
    # elements = driver.find_elements(By.CLASS_NAME, 'bd_3psJk')
    # L1_element = elements[0]
    # L1_element.click()
    # L1_option_text = L1_element.text
    # print(L1_option_text)
    #
    # L1_option_elements = driver.find_elements(By.CLASS_NAME, 'bd_1y1pd')
    # L1_option1 = L1_option_elements[0]
    # L1_option1.click()
    # L1_option_text = L1_element.text
    # print(L1_option_text)
    #
    # L2_element = elements[1]
    # L2_element.click()
    # L2_option_text = L2_element.text
    # print(L2_option_text)
    #
    # search = '(품절)'
    # option_list = L2_option_text.split(sep='\n')
    # for option in option_list:
    #     if search in option:
    #         print(option)

    # 상품 옵션이 하나로 구성된 경우
    driver.get("https://smartstore.naver.com/bigyellowtail/products/6647035187")
    elements = driver.find_elements(By.CLASS_NAME, 'bd_3psJk')
    option_cnt = len(elements)
    print(option_cnt)

    if option_cnt == 1 :
        L1_element = elements[0]
        L1_element.click()
        L1_option_text = L1_element.text
        print(L1_option_text)
    elif option_cnt >= 2 :
        # 상품 옵션이 두가지로  구성된 경우
        L1_element = elements[0]
        L1_element.click()
        L1_option_text = L1_element.text
        print(L1_option_text)

        L1_option_elements = driver.find_elements(By.CLASS_NAME, 'bd_1y1pd')
        # L1_option_cnt = len(L1_option_elements)
        # for option_idx in range(0, L1_option_cnt):
        for L1_option_element in L1_option_elements:
            L1_option_element.click() # click 하는 순간 elements 객체가 날라 간다. 루푸 사용이 불가능
            # 객체 카피를 해서 저장 해야 한다.
            # print(L1_option_element.text)

            L2_element = elements[1]
            L2_element.click()
            L2_option_text = L2_element.text
            print(L2_option_text)

            L1_element = elements[0]
            L1_element.click()
            L1_option_text = L1_element.text
            print(L1_option_text)








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


