# AI_SPARK
#### 제3회 연구개발특구 AI SPARK 챌린지
<br>

-------


## MSG(만족시키자 손님! 고객!) : 배달 리뷰 분석 서비스

<br><br>

## 활용한 인공지능 학습용 데이터
1. 카페 배달리뷰 데이터 셋 https://nanum.etri.re.kr/share/mn99134/deliverysales?lang=ko_KR
2. 카페 배달 매출 데이터 (코로나 현황과 날씨 데이터 연동) https://nanum.etri.re.kr/share/mn99134/deliveryreview?lang=ko_KR
3. 요기요 배달 리뷰 

<br><br><br>

## 상세내용 및 소스코드
#### yogiyo_data_crawling_1.py
- 요기요 사이트 
```
<업체명, 별점, 리뷰 수, 사장님 리뷰, 배달소요시간> 크롤링
```
- 레퍼런스
1. https://scaredev.tistory.com/3 (요기요 음식점 크롤링하기)
2. https://wkdtjsgur100.github.io/selenium-xpath/ (selenium에서 xpath로 크롤링하기)
3. https://hello-bryan.tistory.com/194 (selenium 웹페이지 스크롤하기)

![image](https://user-images.githubusercontent.com/57982899/159743870-1c89ca9c-9da3-4913-86a2-640c0d52bfbe.png)
![image](https://user-images.githubusercontent.com/57982899/159744068-ac454b83-3820-4ef2-a558-eab6832da786.png)
![image](https://user-images.githubusercontent.com/57982899/160955025-3341121e-56a1-46c2-8ba6-7afe479a4b1d.png)

+ 날짜 tag 추가 추출 성공

<br><br>

#### yogiyo_review_data_crawling.py
```
상세리뷰데이터 크롤링
```
- 레퍼런스
1. https://projectlog-eraser.tistory.com/7 (네이버 뉴스 댓글 크롤러)

![image](https://user-images.githubusercontent.com/57982899/159855283-f6926d2f-e34a-4c11-972f-9dea9b9db0c6.png)

<br><br>

#### yogiyo_review_data_crawling_all.py
```
상세리뷰데이터 전체 크롤링
```
- 파일은 카테고리별(한식, 중식, 양식, 디저트/카페)로 df0~df40을 concatenate한 파일입니다.

![image](https://user-images.githubusercontent.com/57982899/160058186-320abff3-0a8c-4784-b8f9-c331fafe20a7.png)

![image](https://user-images.githubusercontent.com/57982899/160058218-b3d484e7-c002-4570-b00d-063ae43447c1.png)

<br><br>



