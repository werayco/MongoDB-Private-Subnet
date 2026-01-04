from pymongo import MongoClient

MONGO = "mongodb://[::1]:27018/?directConnection=true"
client = MongoClient(MONGO)

with client.start_session() as session:
    with session.start_transaction():
        db = client.test_db
        db.accounts.insert_one({"name": "test", "balance": 100}, session=session)
        print("Transaction successful!")

client.close()