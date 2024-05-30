from pydantic import BaseModel

class Student(BaseModel):
    name: str
    roll_no: int
    age: int
    std_class: str

class StudentsInDB(Student):
    id: str

# REsponse model for delete OPeration
class DeleteResponse(BaseModel):
    status: str
