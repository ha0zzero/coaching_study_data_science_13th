# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %config Completer.use_jedi = False

# + [markdown] id="0mlwJLwy6Lo5"
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/corazzon/boostcourse-ds-510/blob/master/open-data-analysis-input.ipynb)
#
#
# # 공공데이터 상권정보 분석해 보기
# * https://www.data.go.kr/dataset/15012005/fileData.do
# * 국가중점데이터인 상권정보를 살펴봅니다.
# * 처음으로 파일데이터에서 `상가(상권)정보_의료기관_201909`를 다운로드 받아봅니다.

# + [markdown] id="snpq_UMr6LpK"
# ## 필요한 라이브러리 불러오기

# + id="GR4Ilhlz6LpN"
import pandas as pd
import numpy as np
import seaborn as sns

# + [markdown] id="Ff3drSRO6LpP"
# ## 시각화를 위한 폰트 설정

# + id="fX6lP-DU6LpR"
# 한글폰트 사용을 위해 설치
# 아래 모듈을 설치하고 불러오면 별도의 한글폰트 설정이 필요 없습니다.
# # !pip install koreanize-matplotlib

# import koreanize_matplotlib

# + id="eQOPa9EA6LpV"
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
# Window 의 한글 폰트 설정
plt.rc('font',family='Malgun Gothic')
# Mac 의 한글 폰트 설정
# plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False)

# 폰트가 선명하게 보이기 위해 - 그래프에 retina display 적용
# retina 대신 svg 등의 설정을 할 수도 있으며
# 디스플레이(모니터)가 retina 를 지원해야만 선명한 차이를 볼 수 있습니다.
# %config InlineBackend.figure_format = 'retina'

# 그래프가 노트북 안에 보이게 하기 위해
# %matplotlib inline

# + [markdown] id="cwp1GpQg6LpX"
# ## 데이터 로드하기
# * 판다스에서 데이터를 로드할 때는 read_csv를 사용합니다.
# * 데이터를 로드해서 df라는 변수에 담습니다.
# * 그리고 shape 를 통해 데이터의 갯수를 찍습니다. 결과는 (행, 열) 순으로 출력됩니다.

# + id="nrN0mu0c6LpY"
df = pd.read_csv('./소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)
df.shape # 행, 열 순임

# + [markdown] id="VqZNfRXe6Lpb"
# ## 데이터 미리보기
# * head, tail 을 통해 데이터를 미리 볼 수 있습니다.

# + id="NlXqiKeI6Lpe"
# head 로 데이터를 미리보기 합니다.
df.head(1)

# + id="o7nh49Yl6Lpg"
# tail 로 마지막 부분에 있는 데이터를 불러옵니다.
df.tail(1)

# + id="0xG9o8K76Lph"
# sample 로 미리보기를 합니다.
df.sample()

# + [markdown] id="fiUqpb8i6Lpi"
# ## 데이터 요약하기

# + [markdown] id="Vr46j5tl6Lpj"
# ### 요약정보

# + id="L2UhKgJa6Lpk"
# info로 데이터의 요약을 봅니다.
df.info()

# + [markdown] id="2ndF9jUE6Lpl"
# ### 컬럼명 보기

# + id="0D8j35-A6Lpl"
# 컬럼명만 출력해 봅니다.
df.columns


# + [markdown] id="h-zPZT6a6Lpm"
# ### 데이터 타입

# + id="UlnY-0jb6Lpm"
# 데이터 타입만 출력합니다.
df.dtypes


# + [markdown] id="hqhUsmpV6Lpn"
# ## 결측치
# -

#python
True == 1

# + id="nafsoihK6Lpo"
null_count = df.isnull().sum()
null_count


# + id="Elh4UC6f6Lpo"
# 위에서 구한 결측치를 .plot.bar 를 통해 막대그래프로 표현합니다.
null_count.plot.barh(figsize=(5, 7))


# + id="eK6JzoO06Lpp"
# 위에서 계산한 결측치 수를 reset_index 를 통해 데이터프레임으로 만들어 줍니다.
# df_null_count 변수에 결과를 담아서 head 로 미리보기를 합니다.

df_null_count = null_count.reset_index()
df_null_count.head(1)


# + [markdown] id="Ci1F_GiE6Lpq"
# ## 컬럼명 변경하기

# + id="os2eLKZl6Lpr"
# df_null_count 변수에 담겨있는 컬럼의 이름을 "컬럼명", "결측치수"로 변경해 줍니다.
df_null_count.columns = ["컬럼명", "결측치수"]
df_null_count.head(1)


# + [markdown] id="KCjhPs0b6Lpr"
# ## 정렬하기

# + id="SobxGLlh6Lps"
# df_null_count 데이터프레임에 있는 결측치수 컬럼을 sort_values 를 통해 정렬해서
# 결측치가 많은 순으로 상위 10개만 출력합니다.
df_null_count_top = df_null_count.sort_values(by="결측치수", ascending=False).head(10)
df_null_count_top


# + [markdown] id="8eCKXo2N6Lps"
# ## 특정 컬럼만 불러오기

# + id="FGKqTLh_6Lpt"
# 지점명 컬럼을 불러옵니다.
# NaN == Not a Number 의 약자. 즉, 결측치.
df["지점명"].head()


# + id="UTHz8dy76Lpt"
# "컬럼명" 이라는 컬럼의 값만 가져와서 drop_columns 라는 변수에 담습니다.
drop_columns = df_null_count_top["컬럼명"].tolist()
drop_columns


# + id="qyiDMaoR6Lpu"
# drop_columns 변수로 해당 컬럼 정보만 데이터프레임에서 가져옵니다.
df[drop_columns].head()


# + [markdown] id="fyX62k-46Lpu"
# ## 제거하기

# + id="miQcWeHh6Lpv"
print(df.shape)
df = df.drop(drop_columns, axis = 1)
print(df.shape)


# + id="sAkWqMpb6Lpv"
df.info()


# + [markdown] id="EVYgbst16Lpw"
# ## 기초 통계값 보기

# + [markdown] id="AR2Ew7IB6Lpw"
# ### 기초 통계 수치

# + id="yCHoU4Uq6Lpx"
# 평균값
df["위도"].mean()


# + id="VK03_HWt6Lpx"
# 중앙값
df["위도"].median()


# + id="HCf2TcZp6Lpy"
# 최댓값
df["위도"].max()


# + id="XuEtesR26LqY"
# 최솟값
df["위도"].min()


# + id="Y9qVLMdq6LqZ"
# 개수
df["위도"].count()


# + [markdown] id="tokOoXxO6Lqa"
# ### 기초통계값 요약하기 - describe
#
# describe 를 사용하면 데이터를 요약해 볼 수 있습니다.
# 기본적으로 수치형 데이터를 요약해서 보여줍니다.
# 데이터의 갯수, 평균, 표준편차, 최솟값,
# 1사분위수(25%), 2사분위수(50%), 3사분위수(75%), 최댓값을 볼 수 있습니다.

# + id="r5_r5Mbv6Lqb"
# 위도를 describe로 요약해 봅니다.
df["위도"].describe()


# + id="uifDHvz06Lqd"
# 2개의 컬럼을 describe 로 요약합니다.
df[["위도", "경도"]].describe()


# + id="wsarkAE86Lqe"
# describe로 문자열 데이터타입의 요약을 봅니다.

df.describe(include="object")


# + [markdown] id="5o6RLIwf6Lqf"
# ### 중복제거한 값 보기
# * unique 로 중복을 제거한 값을 보고 nunique 로 갯수를 세어봅니다.

# + id="VEGav34G6Lqg"
# "상권업종대분류명"
df["상권업종대분류명"].unique()


# + id="2Zwk0Bg76Lqg"
df["상권업종대분류명"].nunique()


# + id="IRskVfNC6Lqh"
# "상권업종중분류명"
df["상권업종중분류명"].unique()


# + id="IB5w3Of46Lqi"
df["상권업종중분류명"].nunique()


# + id="90JglxJc6Lqj"
# "상권업종소분류명"
df["상권업종소분류명"].unique()


# + id="Agjf9VG26Lqk"
df["상권업종소분류명"].nunique()


# + id="dFTGgT4F6Lql"
# nunique 대신 len 을 사용할 수도 있습니다.
len(df["상권업종소분류명"].unique())


# + [markdown] id="Y3E2Av-_6Lqm"
# ### 그룹화된 요약값 보기 - value_counts
# * value_counts 를 사용하면 카테고리 형태의 데이터 갯수를 세어볼 수 있습니다.

# + id="kFBk7Riv6Lqm"
# value_counts 를 사용하면 카테고리 형태의 데이터 갯수를 세어볼 수 있습니다.
# 시도코드를 세어봅니다.
df["시도명"].head()


# + id="wSxPIcqJ6Lqn"
# 시도명을 세어봅니다.
city = df["시도명"].value_counts()
city


# + id="QYFSOI-l6Lqn"
# normalize=True 옵션을 사용하면 비율을 구할 수 있습니다.
city_normalize = df["시도명"].value_counts(normalize=True)
city_normalize


# + id="SZIyIipM6Lqo"
# Pandas 에는 plot기능을 내장하고 있습니다.
# 위에서 분석한 시도명 수를 막대그래프로 표현해 봅니다.
city.plot.barh()
# -


# 파이차트는 보기가 불편함.

# + id="9sMZ5M5Q6Lqp"
# 판다스의 plot.pie()를 사용해서 파이그래프를 그려봅니다.
city_normalize.plot.pie(figsize=(7, 7))


# + id="4pbWg6076Lqq"
# seaborn 의 countplot 으로 그려봅니다.
# 씨본을 사용하면 좀 더 예쁘게 시각화할 수 있음
c = sns.countplot(data=df, y="시도명")


# + id="CnVeHCwX6Lqq"
# "상권업종대분류명"으로 갯수를 세어봅니다.
df["상권업종대분류명"].value_counts()


# + id="03HQSMD26Lqr"
# "상권업종중분류명"으로 갯수를 세어봅니다.
c= df["상권업종중분류명"].value_counts()
c


# + id="CI2ygfJO6Lqr"
# normalize=True 를 사용해 비율을 구해봅니다.
n = df["상권업종중분류명"].value_counts(normalize=True)
n


# + id="hamEKUro6Lqs"
# 판다스의 plot.bar()를 사용해서 막대그래프를 그려봅니다.
c.plot.bar(rot = 0)


# + id="xXFk625J6Lqt"
# 판다스의 plot.pie()를 사용해서 파이그래프를 그려봅니다.
n.plot.pie()


# + id="wS8AcvBE6Lqu"
# "상권업종소분류명" 에 대한 그룹화 된 값을 카운트 합니다.
c = df["상권업종소분류명"].value_counts()


# + id="Zfy3XZE46Lqv"
# "상권업종소분류명"으로 갯수를 세어봅니다.
# 판다스의 plot.bar()를 사용해서 막대그래프를 그려봅니다.
c.plot.barh(figsize=(7, 8), grid=True)


# + [markdown] id="BkhwCAow6Lqw"
# ## 데이터 색인하기
# * 특정 데이터만 모아서 따로 봅니다.

# + id="ofF6RubX6Lqw"
# "상권업종중분류명"이 "약국/한약방"인 데이터만 가져와서
# df_medical 이라는 변수에 담아봅니다.
# 그리고 head()를 통해 미리보기를 합니다.
df_medical = df[df["상권업종중분류명"] == "약국/한약방"].copy()
df_medical.head(1)


# + id="PAjM7d1x6Lqx"
# "상권업종대분류명" 에서 "의료"만 가져옵니다.
# df.loc를 사용하면 행,열을 함께 가져올 수 있습니다.
# 이 기능을 통해 "상권업종중분류명" 만 가져옵니다.
# 그리고 가져온 결과를 value_counts 를 통해 중분류의 갯수를 세어봅니다.
# shop_type
df.loc[df["상권업종대분류명"] == "의료","상권업종중분류명"].value_counts()


# + id="2HPk27V_6Lqy"
# 위와 똑같은 기능을 수행하는 코드입니다. 아래와 같이 한 줄에 표현할 수도 있습니다.
# df.loc[df["상권업종대분류명"] == "의료", "상권업종중분류명"].value_counts()
m = df["상권업종대분류명"] == "의료"
df.loc[m, "상권업종중분류명"].value_counts()

# + id="f9DIlXcJ6Lqz"
# 유사의료업만 따로 모아봅니다.
df_medi = df[df["상권업종중분류명"] == "유사의료업"]
df_medi.shape


# + id="I7biIH7b6Lqz"
# 상호명을 그룹화해서 갯수를 세어봅니다.
# value_counts 를 사용해서 상위 10개를 출력합니다.
df["상호명"].value_counts().head(10)


# + id="4ENPz-W56Lq0"
# 유사의료업만 df_medi 변수에 담겨져 있습니다.
# df_medi 변수에서 상호명으로 갯수를 세어봅니다.
# 가장 많은 상호 상위 10개를 출력해 봅니다.
df_medi["상호명"].value_counts().head(10)


# + [markdown] id="s_mzuRIi6Lq1"
# ### 여러 조건으로 색인하기

# + id="uWS8dQIN6Lq1"
# "상권업종소분류명"이 "약국" 인 것과
# "시도명" 이 "서울특별시"인 데이터만 가져옵니다.
# df_seoul_drug
df_seoul_drug = df[(df["상권업종소분류명"] == "약국") & (df["시도명"] == "서울특별시")]
print(df_seoul_drug.shape)
df_seoul_drug.head()

# + [markdown] id="BADEGXlp6Lq2"
# ### 구별로 보기

# + id="Uy-ZA0RJ6Lq2"
# 위에서 색인한 데이터로 "시군구명"으로 그룹화 해서 갯수를 세어봅니다.
# 구별로 약국이 몇개가 있는지 확인해 봅니다.
c = df_seoul_drug["시군구명"].value_counts()
c.head()


# + id="5Ju2rQg-6Lq3"
# normalize=True 를 통해 비율을 구해봅니다.
n = df_seoul_drug["시군구명"].value_counts(normalize=True)
n.head()


# + id="JTcqWel-6Lq4"
# 위에서 구한 결과를 판다스의 plot.bar()를 활용해 막대그래프로 그립니다.
c.plot.bar(rot = 60)


# + id="i2VY1UeP6Lq4"
# "상권업종소분류명"이 "종합병원" 인 것과
# "시도명" 이 "서울특별시"인 데이터만 가져옵니다.
# df_seoul_hospital
df_seoul_hospital = df[(df["상권업종소분류명"] == "종합병원") & (df["시도명"]=="서울특별시")].copy()
df_seoul_hospital

# + id="hFB2pHay6Lq5"
# "시군구명" 으로 그룹화 해서 구별로 종합병원의 수를 세어봅니다.
df_seoul_hospital["시군구명"].value_counts()


# + [markdown] id="4ADiLacV6Lq6"
# ### 텍스트 데이터 색인하기

# + id="u0Jtq9En6Lq6"
# str.contains 를 사용해서 "상호명"에 "대학병원"이 들어가는 것을 가져와서 head()로 미리보기 합니다.
df_seoul_hospital.loc[~df_seoul_hospital["상호명"].str.contains("종합병원"), "상호명"].unique()
# -


df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달")]

df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기")]

drop_row = df_seoul_hospital[
    df_seoul_hospital["상호명"].str.contains("꽃배달|의료기|장례식장|상담소|어린이집")].index
drop_row = drop_row.tolist()
drop_row

drop_row2 = df_seoul_hospital[
    df_seoul_hospital["상호명"].str.endswith("의원")].index
drop_row2 = drop_row2.tolist()
drop_row2

drop_row = drop_row + drop_row2
len(drop_row)

print(df_seoul_hospital.shape)
df_seoul_hospital= df_seoul_hospital.drop(drop_row, axis=0)
print(df_seoul_hospital.shape)

df_seoul_hospital["시군구명"].value_counts().plot.bar()

plt.figure(figsize=(15, 4))
sns.countplot(data=df_seoul_hospital, x="시군구명", 
              order=df_seoul_hospital["시군구명"].value_counts().index)

df_seoul_hospital["상호명"].unique()

# + [markdown] id="iSEfus-A6Lq8"
# ### 특정 지역만 보기

# + id="-9Hn1udR6Lq9"
# 서울에 있는 데이터의 위도와 경도를 봅니다.
# 결과를 df_seoul 이라는 데이터프레임에 저장합니다.
# 새로운 변수에 데이터프레임을 저장시 copy()를 사용합니다.
# df_seoul
df_seoul = df[df["시도명"] == "서울특별시"].copy()
df_seoul.shape


# + id="rSKG78296Lq9"
# seaborn 의 countplot 을 사용해서 위에서 만든 df_seoul 데이터프레임의
# 시군구명을 시각화 합니다.
# plt.figure(figsize=(9, 6))
df_seoul["시군구명"].value_counts().plot.bar(figsize=(10,4), rot=30)
# -


plt.figure(figsize=(15, 4))
sns.countplot(data=df_seoul, x="시군구명")

# + id="cSIUGWlk6Lq-"
# Pandas 의 plot.scatter 를 통해 경도와 위도를 표시해 봅니다.
df_seoul[["경도", "위도", "시군구명"]].plot.scatter(x="경도", y="위도", figsize=(8, 7), grid=True)


# + id="KY5QtbNJ6Lq_"
# seaborn의 scatterplot 을 통해 구별 경도와 위도를 표시해 봅니다.
plt.figure(figsize=(9,8))
sns.scatterplot(data=df_seoul, x="경도", y="위도", hue="시군구명")


# + id="snyOtXVt6LrA"
# seaborn의 scatterplot 을 통해 "상권업종중분류명" 경도와 위도를 표시해 봅니다.
plt.figure(figsize=(9,8))
sns.scatterplot(data=df_seoul, x="경도", y="위도", hue="상권업종중분류명")


# + id="nhjzDLZD6LrA"
# seaborn의 scatterplot 을 통해 전국 데이터(df)로 구별 경도와 위도를 표시해 봅니다.
plt.figure(figsize=(16,12))
sns.scatterplot(data=df, x="경도", y="위도", hue="시도명")


# + [markdown] id="HVffG2cU6LrB"
#
# ## Folium 으로 지도 활용하기
# * 다음의 프롬프트 창을 열어 conda 명령어로 설치합니다.
# <img src="https://t1.daumcdn.net/cfile/tistory/99576B4A5B751DC902">
#
# 검은색 프롬프트 창에 아래 명령어를 통해 folium 을 설치합니다.
#
#
# `conda install -c conda-forge folium`
#
# ### Folium 사용예제
# http://nbviewer.jupyter.org/github/python-visualization/folium/tree/main/examples/
#

# + id="wLjqDfda6LrC"
# 아나콘다에서 folium 을 사용하기 위해서는 별도의 설치가 필요
# https://anaconda.org/conda-forge/folium
# conda install -c conda-forge folium
# 지도 시각화를 위한 라이브러리
import folium
# -


df_seoul_hospital["위도"].mean()

df_seoul_hospital["경도"].mean()

df_seoul_hospital.head(1)

df_seoul_hospital.tail(1)

# +
map = folium.Map(location=[df_seoul_hospital["위도"].mean(), df_seoul_hospital["경도"].mean()],
                    zoom_start=12)

for n in df_seoul_hospital.index:
    name = df_seoul_hospital.loc[n, "상호명"]
    address = df_seoul_hospital.loc[n, "도로명"]
    popup = f"{name}-{address}"
    location = [df_seoul_hospital.loc[n, "위도"],df_seoul_hospital.loc[n, "경도"]]
    folium.Marker(
        location = location,
        popup = popup,
    ).add_to(map)
map
