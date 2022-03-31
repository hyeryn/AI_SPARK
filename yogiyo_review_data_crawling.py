from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\sockshopping\\chromedriver.exe')  # 크롬드라이버 경로 설정
url = "https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/232318/"  # 사이트 입력
driver.get(url)  # 사이트 오픈
time.sleep(1)

# 리뷰버튼 클릭
review_xpath = '''//*[@id="content"]/div[2]/div[1]/ul/li[2]/a'''
driver.find_element(by=By.XPATH, value=review_xpath).click()
time.sleep(1)

# 더보기
while True:
    try:
        css_selector = '#review > li.list-group-item.btn-more > a'
        more_reviews = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
        more_reviews.click()
        time.sleep(1)
    except:
        break

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
# time.sleep(2)
# pre_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤 위치 저장
#
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
#     time.sleep(1)
#     cur_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤을 저장한다.
#     # 스크롤 다운 후 스크롤 높이 다시 가져옴
#     if pre_height == cur_height:
#         break
#     # pre_height == cur_height
#     pre_height = cur_height

time.sleep(3)

# 페이지 소스 출력
html = driver.page_source
html_source = BeautifulSoup(html, 'html.parser')

# print(html_source)

# 데이터 추출
restaurant_name = html_source.find("span", class_="restaurant-name ng-binding")  # 업체명
review_taste = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                        "ng-show": "review.rating_taste > 0"})  # 별점-맛
review_quantity = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                        "ng-show": "review.rating_quantity > 0"})  # 별점-양
review_delivery = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                        "ng-show": "review.rating_delivery > 0"})  # 별점-배달
order_menu = html_source.find_all("div", class_="order-items default ng-binding")  # 주문 메뉴
customer_review = html_source.find_all("p", attrs={"class": "ng-binding",
                                                        "ng-show": "review.comment"})  # 리뷰
review_date = html_source.find_all("span", attrs={"class": "review-time ng-binding",
                                                        "ng-bind": "review.time|since"})  # 날짜

# csv 파일 만들기 위한 list 설정
tastes = []
quantitys = []
deliverys = []
menus = []
reviews = []
dates = []

# 데이터 배열
for i, j, l, m, n, o in zip(review_taste, review_quantity, review_delivery, order_menu, customer_review, review_date):
    tastes.append(i.string)
    quantitys.append(j.string)
    deliverys.append(l.string)
    menus.append(m.string)
    reviews.append(n.string)
    dates.append(o.string)

time.sleep(5) # 크롤링 소요시간 임의 설정
# driver.close()  # 크롬드라이버 종료


'''
csv 파일로 저장하기
'''
reviews = pd.DataFrame({'업체명':restaurant_name, '날짜':dates, '맛':tastes,'양':quantitys,
                        '배달':deliverys,'주문메뉴':menus, '상세리뷰':reviews})
print(reviews)

# while True:
#     try:
#         reviews.to_csv("C:\pythonProject\crawl_data\review " + '.csv', encoding='cp949')
#         break
#     except Exception as e: # 인코딩 에러 예외처리
#         error_character = str(e).split(' ')[5].replace('\'', '')
#         reviews = reviews.replace(u'{}'.format(error_character), u'', regex=True)

reviews.to_csv("C:\\pythonProject\\crawl_data\\detail_review_example.csv", index=False, encoding="utf-8-sig")