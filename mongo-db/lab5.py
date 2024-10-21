# Import
from pymongo import MongoClient
from datetime import datetime

# Bước 1: Kết nối đến MongoDB
client = MongoClient('mongodb://localhost:27017/')
client.drop_database('facebook_data')
db = client['facebook_data'] # Chọn csdl facebook

# Bước 2: Tạo các collections
users_collection = db['users']
posts_collection = db['posts']

# Bước 3: Thêm dữ liệu người dùng
users_data = [
    {'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25},
    {'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30},
    {'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22}
]
users_collection.insert_many(users_data)

# Bước 4: Thêm dữ liệu về video
posts_data = [
    {'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024,10,1)},
    {'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024,10,2)},
    {'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024,10,3)}
]
posts_collection.insert_many(posts_data) # Thêm dữ liệu video

# Bước 5: Truy vấn dữ liệu
# 5.1: Xem tất cả người dùng
print("Tất cả người dùng")
for user in users_collection.find():
    print(user)

# 5.2: Tìm video có nhiều người xem nhất
print("Video có nhiều người xem nhất")
mosted_viewed_post = posts_collection.find().sort('view', -1).limit(1)
for user in mosted_viewed_post:
    print(user)

# 5.3: Tìm tất cả video của người dùng có username là "user1"
print("\nTất cả video của người dùng 'user1':")
user_posts = posts_collection.find({'user_id':1})
for post in user_posts:
    print(post)

# Bước 6: Cập nhật dữ liệu
# Cập nhật số người theo dõi của người dùng với 'user_id' là 1 lên 2000
users_collection.update_one({'user_id': 1}, {'$set': {'followers':2000}})

# Bước 7: Xóa video có 'video_id' là 3
posts_collection.delete_one({'post_id': 3})

# Bước 8: Xem lại dữ liệu sau khi cập nhật và xóa
print("\nDữ liệu người dùng sau khi cập nhật:")
for user in users_collection.find():
    print(user)

print("\nDữ liệu video sau khi xóa:")
for post in posts_collection.find():
    print(post)

# Đóng kết nối
client.close()