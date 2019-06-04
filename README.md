# 상권별 트렌드의 변화

학과 | 학번 | 성명
---- | ---- | ---- 
통계학과 |201811524 |윤민지


## 프로젝트 개요
1. pandas 패키지를 이용하여 데이터 불러오기
2. 데이터 내용 파악 & 불필요한 변수 삭제
3. plotnine 패키지를 이용하여 전체 데이터의 산점도를 그림
4. .loc 을 이용하여 서울특별시와 부산광역시를 나눔
5. 시도와 구군 변수 추가
6. 원하는 관측값 산점도 그림

## 사용한 공공데이터 
[데이터보기]https://www.data.go.kr/dataset/15012005/fileData.do

## 소스

* 코드 삽입

~~~python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from plotnine import *
~~~

## 데이터 불러오기 & 내용 파악
~~~python
shop_2016 = pd.read_csv('D:/2-1/pyfinal/201606_01.csv', encoding='cp949')

print(shop_2016.head(5))
print(shop_2016.tail(5))
print(shop_2016.columns)
~~~
![1](https://user-images.githubusercontent.com/51190969/58799201-a624c500-863f-11e9-8404-0848b1c013ca.png)

## 변수 제거
39개의 변수 중 13개의 변수만 가져옴
~~~python
shop_2016 = shop_2016[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명',
              '상권업종소분류명', '시도명', '시군구명',
              '행정동명', '법정동명', '지번주소','도로명주소', '경도', '위도']]
~~~

## shop_2016 산점도 그리기
데이터 크기가 너무 커서 1000개만 그림
~~~python
a=(ggplot(shop_2016[:1000])
 + aes(x='경도', y='위도')
 + geom_point())
print(a)
~~~
![Figure_1](https://user-images.githubusercontent.com/51190969/58798854-bf794180-863e-11e9-9d1c-1385ab2029d9.png)

## 서울과 부산으로 데이터 분류
~~~python
seoul_6 = shop_2016.loc[shop_2016['시도명']=='서울특별시']
pusan_6 = shop_2016.loc[shop_2016['시도명']=='부산광역시']
print(seoul_6.shape)
print(pusan_6.shape)
~~~
(493945, 13)
(158707, 13)
~~~python
b=(ggplot(seoul_6)
 + aes(x='경도', y='위도')
 + geom_point(color='black', alpha=0.2, size=0.2)
)
print(b)
~~~
![Figure_2-2](https://user-images.githubusercontent.com/51190969/58798869-ca33d680-863e-11e9-9fe1-fde7817467e9.png)

## 변수 추가 : 시도, 구군
~~~python
print(shop_2016['도로명주소'].head(3))
print(shop_2016.shape)
~~~
![2](https://user-images.githubusercontent.com/51190969/58800131-0caae280-8642-11e9-976a-61c46d29751b.PNG)
(652652,13)
~~~python
shop_2016['시도'] = shop_2016['도로명주소'].str.split(' ', expand=True)[0]
shop_2016['구군'] = shop_2016['도로명주소'].str.split(' ', expand=True)[1]
print(shop_2016.shape)
print(shop_2016.columns)
~~~
(652652, 15)
![3](https://user-images.githubusercontent.com/51190969/58800132-0caae280-8642-11e9-8c68-421a799b2e72.PNG)

## 분류된 구군 변수를 이용해 서울특별시 지도 생성
~~~python
seoul_6 = shop_2016.loc[shop_2016['시도명']=='서울특별시']
pusan_6 = shop_2016.loc[shop_2016['시도명']=='부산광역시']

c=(ggplot(seoul_6)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(c)
~~~
![Figure_3-2](https://user-images.githubusercontent.com/51190969/58798882-d1f37b00-863e-11e9-82b6-9fdd3441abc8.png)

~~~python
print(seoul_6['상권업종대분류명'].value_counts())
print(seoul_6['상권업종중분류명'].value_counts())
~~~
![4](https://user-images.githubusercontent.com/51190969/58800663-665fdc80-8643-11e9-9ba3-6197ece37707.PNG)
![5](https://user-images.githubusercontent.com/51190969/58800664-66f87300-8643-11e9-81a0-be8038f85dd1.PNG)

## 상권업종대분류 지도
~~~python
d=(ggplot(shop_seoul_6)
 + aes(x='경도', y='위도', color='상권업종대분류명')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(d)
~~~
![Figure_4-2](https://user-images.githubusercontent.com/51190969/58798889-d61f9880-863e-11e9-8f37-fa41b8ac897d.png)

## 학문/교육 지도
~~~python
seoul_6_edu = seoul_6[seoul_6['상권업종대분류명'] == '학문/교육']

e=(ggplot(seoul_6_edu)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(e)
~~~
![Figure_5-2](https://user-images.githubusercontent.com/51190969/58798890-d61f9880-863e-11e9-95d2-75ae669f0b9f.png)
![Figure_5-2](https://user-images.githubusercontent.com/51190969/58800895-0f0e3c00-8644-11e9-94c8-b6aac0b1a725.png)
![Figure_5-2](https://user-images.githubusercontent.com/51190969/58801046-6f9d7900-8644-11e9-8070-c5d4e5387095.png)

## 부동산 지도
~~~python
seoul_6_house = seoul_6[seoul_6['상권업종대분류명'] == '부동산']

f=(ggplot(seoul_6_house)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(f)
~~~
![Figure_6-2](https://user-images.githubusercontent.com/51190969/58798891-d61f9880-863e-11e9-8255-75c3c6dfc738.png)
![Figure_6-2](https://user-images.githubusercontent.com/51190969/58800898-0fa6d280-8644-11e9-8262-09272900587d.png)
![Figure_6-2](https://user-images.githubusercontent.com/51190969/58801048-70360f80-8644-11e9-84a9-db1d21642723.png)

## 컴퓨터 학원 지도
~~~python
seoul_6_pc = seoul_6[seoul_6['상권업종중분류명'] == '학원-컴퓨터']

g=(ggplot(seoul_6_pc)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point()
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(g)
~~~
![Figure_7-2](https://user-images.githubusercontent.com/51190969/58798892-d6b82f00-863e-11e9-99b3-7de09f517c07.png)
![Figure_7-2](https://user-images.githubusercontent.com/51190969/58800902-0fa6d280-8644-11e9-883c-8cbbc7d2a64f.png)
![Figure_7-2](https://user-images.githubusercontent.com/51190969/58801049-70360f80-8644-11e9-96e9-7e6193e56a01.png)

## 커피점/카페 지도
~~~python
seoul_6_eat = seoul_6[seoul_6['상권업종중분류명'] == '커피점/카페']

h=(ggplot(seoul_6_eat)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(h)
~~~
![Figure_8-2](https://user-images.githubusercontent.com/51190969/58798895-d6b82f00-863e-11e9-94c9-55792f979552.png)
![Figure_8-2](https://user-images.githubusercontent.com/51190969/58800906-10d7ff80-8644-11e9-9a8f-83eb668ced0d.png)
![Figure_8-2](https://user-images.githubusercontent.com/51190969/58801050-70360f80-8644-11e9-8107-838e586d1a15.png)

## 부산광역시 지도
~~~python
i=(ggplot(pusan_6)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
)
print(i)
~~~
![Figure_9-2](https://user-images.githubusercontent.com/51190969/58798896-d6b82f00-863e-11e9-8ad3-c72a774390a7.png)
