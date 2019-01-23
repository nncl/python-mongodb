from pymongo import MongoClient

# print("Hello World")

client = MongoClient('mongodb://localhost:27017/')
db = client['py-training']
news_col = db.news

news = {
		"title": "Armed Robbery"
	}

news_id = news_col.insert_one(news).inserted_id

print(news_id)
