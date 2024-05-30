from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
database = client.get_database("fastapi_database")
collection = database.get_collection("students")
