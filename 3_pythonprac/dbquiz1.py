from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화제목 '매트릭스'의 평점 가져오기
movie = db.movies.find_one({'title': '매트릭스'})
print(movie['star'])
