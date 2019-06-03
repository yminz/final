# 상권별 트렌드의 변화

학과 | 학번 | 성명
---- | ---- | ---- 
통계학과 |201811524 |윤민지


## 프로젝트 개요
본인의 프로젝트 개요에 대하여 작성합니다.

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)

## 소스

* 코드 삽입

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
