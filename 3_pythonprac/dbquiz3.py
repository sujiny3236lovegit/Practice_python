from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스의 평점을 0점으로 만들기
db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})  # 0을 문자열로 통일해서 넣기위해 '0'으로 넣음=> 어떤 형식으로 들어있는지도 중요하다.
