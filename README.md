# 상권별 트렌드의 변화

학과 | 학번 | 성명
---- | ---- | ---- 
통계학과 |201811524 |윤민지


## 프로젝트 개요
데이터의 변수나 관측치 등 전체적인 내용을 파악하고 필요한 변수만을 추출하여 분석을 한다. 변수들 중 경도, 위도 데이터와 ggplot의 산점도를 이용해 지도를 그려보고 데이터를 계속 분류하면서 2016년에서 2018년까지의 지도를 비교해봄으로써 변화를 파악한다.

## 사용한 공공데이터 
[데이터보기]https://www.data.go.kr/dataset/15012005/fileData.do

## 소스

* 코드 삽입

~~~python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from plotnine import *

shop_2016 = pd.read_csv('D:/2-1/pyfinal/201606_01.csv', encoding='cp949')

print(shop_2016.head(3))
print(shop_2016.tail(3))
print(shop_2016.columns)

shop_2016 = shop_2016[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명',
              '상권업종소분류명', '시도명', '시군구명',
              '행정동명', '법정동명', '지번주소','도로명주소', '경도', '위도']]


a=(ggplot(shop_2016[:1000])
 + aes(x='경도', y='위도')
 + geom_point())
print(a)

seoul_6 = shop_2016.loc[shop_2016['시도명']=='서울특별시']
pusan_6 = shop_2016.loc[shop_2016['시도명']=='부산광역시']
print(seoul_6.shape)
print(pusan_6.shape)


b=(ggplot(seoul_6)
 + aes(x='경도', y='위도')
 + geom_point(color='black', alpha=0.2, size=0.2)
)
print(b)

print(shop_2016['도로명주소'].head(3))
print(shop_2016.shape)
shop_2016['시도'] = shop_2016['도로명주소'].str.split(' ', expand=True)[0]
shop_2016['구군'] = shop_2016['도로명주소'].str.split(' ', expand=True)[1]
print(shop_2016.shape)
print(shop_2016.columns)

seoul_6 = shop_2016.loc[shop_2016['시도명']=='서울특별시']
pusan_6 = shop_2016.loc[shop_2016['시도명']=='부산광역시']

c=(ggplot(seoul_6)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(c)

print(seoul_6['상권업종대분류명'].value_counts())
print(seoul_6['상권업종중분류명'].value_counts())

d=(ggplot(shop_seoul_6)
 + aes(x='경도', y='위도', color='상권업종대분류명')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(d)

seoul_6_edu = seoul_6[seoul_6['상권업종대분류명'] == '학문/교육']

e=(ggplot(seoul_6_edu)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(e)

seoul_6_house = seoul_6[seoul_6['상권업종대분류명'] == '부동산']

f=(ggplot(seoul_6_house)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(f)

seoul_6_pc = seoul_6[seoul_6['상권업종중분류명'] == '학원-컴퓨터']

g=(ggplot(seoul_6_pc)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point()
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(g)

seoul_6_eat = seoul_6[seoul_6['상권업종중분류명'] == '커피점/카페']

h=(ggplot(seoul_6_eat)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(h)

i=(ggplot(pusan_6)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
)
print(i)
~~~
![Figure_1](https://user-images.githubusercontent.com/51190969/58798854-bf794180-863e-11e9-9d1c-1385ab2029d9.png)
![Figure_2-2](https://user-images.githubusercontent.com/51190969/58798869-ca33d680-863e-11e9-9fe1-fde7817467e9.png)
![Figure_3-2](https://user-images.githubusercontent.com/51190969/58798882-d1f37b00-863e-11e9-82b6-9fdd3441abc8.png)
![Figure_4-2](https://user-images.githubusercontent.com/51190969/58798889-d61f9880-863e-11e9-8f37-fa41b8ac897d.png)
![Figure_5-2](https://user-images.githubusercontent.com/51190969/58798890-d61f9880-863e-11e9-95d2-75ae669f0b9f.png)
![Figure_6-2](https://user-images.githubusercontent.com/51190969/58798891-d61f9880-863e-11e9-8255-75c3c6dfc738.png)
![Figure_7-2](https://user-images.githubusercontent.com/51190969/58798892-d6b82f00-863e-11e9-99b3-7de09f517c07.png)
![Figure_8-2](https://user-images.githubusercontent.com/51190969/58798895-d6b82f00-863e-11e9-94c9-55792f979552.png)
![Figure_9-2](https://user-images.githubusercontent.com/51190969/58798896-d6b82f00-863e-11e9-8ad3-c72a774390a7.png)
