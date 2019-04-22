#ex1

import pymongo

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db = client.c4e

#ex2

my_post = {
    "title":"Không trượt phát lào!",
    "author":"DuyLan",
    "content":'''Nếu dòng code này xuất hiện ở đây, tức là code của tớ không lỗi.
                Hãy như tớ!'''     
}

db.posts.insert_one(my_post)