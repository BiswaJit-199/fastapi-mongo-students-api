from .database import *
from .schemas import Student
from bson import ObjectId



#std_helper(): converts a MOngoDB doc to a dictionary.
def std_helper(student) -> dict:
    return {
        "name": student["name"],
        "roll_no": student["roll_no"],
        "age": student["age"],
        "std_class": student["std_class"],
        "id": str(student["_id"])
    }

async def retrieve_student(id: str):
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        return std_helper(student)
    return None

async def retrieve_students():
    students = []
    async for student in collection.find():
        students.append(std_helper(student))
    return students

async def add_student(student_data: dict):
    student = await collection.insert_one(student_data)
    new_student = await collection.find_one({"_id": student.inserted_id})
    return std_helper(new_student)

async def delete_student(id: str):
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    return False

async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return await retrieve_student(id)
    return False
