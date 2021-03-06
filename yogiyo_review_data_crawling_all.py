from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.by import By



chinese = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/232318/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/450579/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/388655/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/386894/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/482892/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/511898/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1052353/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/449385/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/420905/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1016508/']

korean = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/232899/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/224438/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/364216/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/254924/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/261695/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/447499/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/524436/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/54603/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/247216/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/215476/',]

western = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/56041/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/450128/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/442348/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/375222/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/445730/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/280344/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/293756/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/553158/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/484080/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/555610/']


desert = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/505362/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1021611/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/452419/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/525247/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1001529/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/441376/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/490133/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/492680/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1005655/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1007287/']


categories = []
# categories.append(chinese)
# categories.append(korean)
# categories.append(western)
categories.append(desert)

csv_num = 33

for category in categories:
    for url in category:
        driver = webdriver.Chrome('C:\\sockshopping\\chromedriver.exe')  # ?????????????????? ?????? ??????
        driver.get(url)  # ????????? ??????

        # ???????????? ??????
        review_xpath = '''//*[@id="content"]/div[2]/div[1]/ul/li[2]/a'''
        driver.find_element(by=By.XPATH, value=review_xpath).click()
        time.sleep(3)

        # ?????????
        while True:
            try:
                css_selector = '#review > li.list-group-item.btn-more > a'
                more_reviews = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
                more_reviews.click()
                time.sleep(2)
            except:
                break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # ???????????? ?????? ????????? ?????????
        time.sleep(2)
        pre_height = driver.execute_script("return document.body.scrollHeight")  # ?????? ????????? ?????? ??????

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # ???????????? ?????? ????????? ?????????
            time.sleep(1)
            cur_height = driver.execute_script("return document.body.scrollHeight")  # ?????? ???????????? ????????????.
            # ????????? ?????? ??? ????????? ?????? ?????? ?????????
            if pre_height == cur_height:
                break
            # pre_height == cur_height
            pre_height = cur_height

        time.sleep(3)

        # ????????? ?????? ??????
        html = driver.page_source
        html_source = BeautifulSoup(html, 'html.parser')

        # print(html_source)

        # ????????? ??????
        restaurant_name = html_source.find("span", class_="restaurant-name ng-binding")  # ?????????
        review_taste = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_taste > 0"})  # ??????-???
        review_quantity = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_quantity > 0"})  # ??????-???
        review_delivery = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_delivery > 0"})  # ??????-??????
        order_menu = html_source.find_all("div", class_="order-items default ng-binding")  # ?????? ??????
        customer_review = html_source.find_all("p", attrs={"class": "ng-binding",
                                                                "ng-show": "review.comment"})  # ??????

        # csv ?????? ????????? ?????? list ??????
        tastes = []
        quantitys = []
        deliverys = []
        menus = []
        reviews = []

        # ????????? ??????
        for i, j, l, m, n in zip(review_taste, review_quantity, review_delivery, order_menu, customer_review):
            tastes.append(i.string)
            quantitys.append(j.string)
            deliverys.append(l.string)
            menus.append(m.string)
            reviews.append(n.string)

        time.sleep(20) # ????????? ???????????? ?????? ??????
        # driver.close()  # ?????????????????? ??????


        '''
        csv ????????? ????????????
        '''
        reviews = pd.DataFrame({'?????????':restaurant_name, '???':tastes,'???':quantitys,
                                '??????':deliverys,'????????????':menus, '????????????':reviews})
        print(reviews)

        # while True:
        #     try:
        #         reviews.to_csv("C:\pythonProject\crawl_data\review " + '.csv', encoding='cp949')
        #         break
        #     except Exception as e: # ????????? ?????? ????????????
        #         error_character = str(e).split(' ')[5].replace('\'', '')
        #         reviews = reviews.replace(u'{}'.format(error_character), u'', regex=True)

        reviews.to_csv("C:\\pythonProject\\crawl_data\\reviews\\detail_review{}.csv".format(csv_num), index=False, encoding="utf-8-sig")
        csv_num += 1


# ????????? dataframe concatenate
lists_tmp=[]
concat_df_num=0

for i in range(40):
    globals()['df_{}'.format(i)] = pd.read_csv('C:\\pythonProject\\crawl_data\\reviews\\detail_review{}.csv'.format(i))
    # csv?????? ????????? ???????????? 9???????????? ??????????????? ?????????.
    lists_tmp.append(globals()['df_{}'.format(i)])
    if i % 10 == 9:
        globals()['concat_df{}'.format(concat_df_num)]=pd.concat(lists_tmp)
        lists_tmp.clear()
        concat_df_num+=1

# concatenate??? ?????? ??????
concat_df0.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_chinese.csv", index=False, encoding="utf-8-sig")
concat_df1.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_korean.csv", index=False, encoding="utf-8-sig")
concat_df2.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_western.csv", index=False, encoding="utf-8-sig")
concat_df3.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_dessert.csv", index=False, encoding="utf-8-sig")
