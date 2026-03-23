from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
collection = db["chats"]

def save_chat(order_id, messages):
    collection.update_one(
        {"order_id": order_id},
        {"$set": {"messages": messages}},
        upsert=True
    )

def load_chat(order_id):
    data = collection.find_one({"order_id": order_id})
    return data["messages"] if data else []