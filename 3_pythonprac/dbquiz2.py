from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스와 같은 평점의 영화들 찾기
movie = db.movies.find_one({'title': '매트릭스'})
target_star = movie['star']

target_movies = list(db.movies.find({'star': target_star}, {'_id': False}))

for target in target_movies:
    print(target['title'])
