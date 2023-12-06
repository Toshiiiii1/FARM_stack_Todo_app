from model import Todo
import motor.motor_asyncio

# connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.FARM_todo
collection = database.todo

async def get_one(title):
    document = await collection.find_one({"title": title})
    return document

async def get_all():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update(title, desc):
    await collection.update_one(
        filter={"title": title},
        update={"$set": {
            "description": desc
        }}
    )
    document = await collection.find_one({"title": title})
    return document

async def delete(title):
    await collection.delete_one(filter={"title": title})
    return True

