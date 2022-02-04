from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

from bs4 import BeautifulSoup

import requests

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    rank = movie.select_one('td:nth-child(1) > img')
    rate = movie.select_one('td.point')
    
    if rank is not None:
        rank = rank['alt']
        title = a_tag.text
        star = rate.text

# 내 풀이

# findRate = db.movies.find_one({'title':'매트릭스'})
# # print(findRate['star'])
# findStar = findRate
# find_sameRate = db.movies.find({'star': findStar})
# print(find_sameRate)

target_movie = db.movies.find_one({'title': '매트릭스'})
target_star = target_movie['star']

t_movies = list(db.movies.find({'star': target_star}))

# for movie in t_movies:
#     print((movie['title']))

# 내 풀이와 다른점

    # 내 접근 방식
    
        # 매트릭스라는 제목을 가진 데이터를 하나 찾는다
        # 해당 데이터['star']를 이용해 새로운 데이터들을 찾아
        # 출력한다

    # 정답풀이 접근 방식(내 해석)

        # 매트릭스라는 제목을 가진 데이터를 find
        # 해당 데이터의 star 값을 새로운 변수화
        # 특정 데이터의 list-find에 새로운 변수를 조건으로 넣는다
        # 반복문을 통해 title만 출력


# 매트릭스 영화 평점을 0으로 만들기

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
