from pymongo import MongoClient
from datetime import datetime
#b1 conntct db
client = MongoClient('mongodb://localhost:27017/')
db = client['facebookData1'] #chon csdl facebook

users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

users_data= [
    { 'user_id': 1, 'name': "Nguyen Van A", 'name': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'name': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'name': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)

posts_data= [
    { 'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024,10,1)},
    { 'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024,10,2)},
    { 'post_id': 3, 'user_id': 3, 'content' :"Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024,10,3)}
]
posts_collection.insert_many(posts_data)

comments_data=[
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024,10,1)},
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024,10,2)},
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024,10,3)}
]
comments_collection.insert_many(comments_data)

user_ = users_collection.find()
for users in user_:
    print(users)

com = comments_collection.find({ 'post_id': 1 })
for cm in com:
    print(complex)