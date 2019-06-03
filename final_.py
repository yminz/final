'''
pip install missingno
pip install plotnine
pip install –upgrade pandas
'''
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

##################################################################################################################################

shop_2017 = pd.read_csv('D:/2-1/pyfinal/201706_01.csv', encoding='cp949')

print(shop_2017.head(3))
print(shop_2017.tail(3))
print(shop_2017.columns)

shop_2017 = shop_2017[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명',
              '상권업종소분류명', '시도명', '시군구명',
              '행정동명', '법정동명', '지번주소','도로명주소', '경도', '위도']]


a2=(ggplot(shop_2017[:1000])
 + aes(x='경도', y='위도')
 + geom_point())
print(a2)

seoul_7 = shop_2017.loc[shop_2017['시도명']=='서울특별시']
pusan_7 = shop_2017.loc[shop_2017['시도명']=='부산광역시']
print(seoul_7.shape)
print(pusan_7.shape)


b2=(ggplot(seoul_7)
 + aes(x='경도', y='위도')
 + geom_point(color='black', alpha=0.2, size=0.2)
)
print(b2)

print(shop_2017['도로명주소'].head(3))

print(shop_2017.shape)
shop_2017['시도'] = shop_2017['도로명주소'].str.split(' ', expand=True)[0]
shop_2017['구군'] = shop_2017['도로명주소'].str.split(' ', expand=True)[1]
print(shop_2017.shape)
print(shop_2017.columns)

seoul_7 = shop_2017.loc[shop_2017['시도명']=='서울특별시']
pusan_7 = shop_2017.loc[shop_2017['시도명']=='부산광역시']

c2=(ggplot(seoul_7)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(c2)

print(seoul_7['상권업종대분류명'].value_counts())
print(seoul_7['상권업종중분류명'].value_counts())

d2=(ggplot(shop_seoul_7)
 + aes(x='경도', y='위도', color='상권업종대분류명')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(d2)

seoul_7_edu = seoul_7[seoul_7['상권업종대분류명'] == '학문/교육']

e2=(ggplot(seoul_7_edu)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(e2)

seoul_7_house = seoul_7[seoul_7['상권업종대분류명'] == '부동산']

f2=(ggplot(seoul_7_house)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(f2)

seoul_7_pc = seoul_7[seoul_7['상권업종중분류명'] == '학원-컴퓨터']

g2=(ggplot(seoul_7_pc)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point()
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(g2)

seoul_7_eat = seoul_7[seoul_7['상권업종중분류명'] == '커피점/카페']

h2=(ggplot(seoul_7_eat)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(h2)

i2=(ggplot(pusan_7)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
)
print(i2)

##################################################################################################################################

shop_2018 = pd.read_csv('D:/2-1/pyfinal/201806_01.csv', encoding='cp949')

print(shop_2018.head(3))
print(shop_2018.tail(3))
print(shop_2018.columns)

shop_2018 = shop_2018[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명',
              '상권업종소분류명', '시도명', '시군구명',
              '행정동명', '법정동명', '지번주소','도로명주소', '경도', '위도']]


a3=(ggplot(shop_2018[:1000])
 + aes(x='경도', y='위도')
 + geom_point())
print(a3)

seoul_8 = shop_2018.loc[shop_2018['시도명']=='서울특별시']
pusan_8 = shop_2018.loc[shop_2018['시도명']=='부산광역시']
print(seoul_8.shape)
print(pusan_8.shape)


b2=(ggplot(seoul_7)
 + aes(x='경도', y='위도')
 + geom_point(color='black', alpha=0.2, size=0.2)
)
print(b2)

print(shop_2017['도로명주소'].head(3))

print(shop_2017.shape)
shop_2017['시도'] = shop_2017['도로명주소'].str.split(' ', expand=True)[0]
shop_2017['구군'] = shop_2017['도로명주소'].str.split(' ', expand=True)[1]
print(shop_2017.shape)
print(shop_2017.columns)

seoul_7 = shop_2017.loc[shop_2017['시도명']=='서울특별시']
pusan_7 = shop_2017.loc[shop_2017['시도명']=='부산광역시']

c2=(ggplot(seoul_7)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(c2)

print(seoul_7['상권업종대분류명'].value_counts())
print(seoul_7['상권업종중분류명'].value_counts())

d2=(ggplot(shop_seoul_7)
 + aes(x='경도', y='위도', color='상권업종대분류명')
 + geom_point(alpha=0.2, size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(d2)

seoul_7_edu = seoul_7[seoul_7['상권업종대분류명'] == '학문/교육']

e2=(ggplot(seoul_7_edu)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(e2)

seoul_7_house = seoul_7[seoul_7['상권업종대분류명'] == '부동산']

f2=(ggplot(seoul_7_house)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point(size=0.2)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(f2)

seoul_7_pc = seoul_7[seoul_7['상권업종중분류명'] == '학원-컴퓨터']

g2=(ggplot(seoul_7_pc)
 + aes(x='경도', y='위도', color='상권업종중분류명')
 + geom_point()
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(g2)

seoul_7_eat = seoul_7[seoul_7['상권업종중분류명'] == '커피점/카페']

h2=(ggplot(seoul_7_eat)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
 + scale_fill_gradient(low = 'blue', high = 'green')
)
print(h2)

i2=(ggplot(pusan_7)
 + aes(x='경도', y='위도', color='구군')
 + geom_point(size=0.7)
)
print(i2)