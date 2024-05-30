from fastapi import APIRouter, HTTPException
from ..schemas import Student, StudentsInDB, DeleteResponse
from ..crud import (
    retrieve_student,
    retrieve_students,
    add_student,
    delete_student,
    update_student
)

router = APIRouter()

@router.post("/student/create", response_model=StudentsInDB)
async def s_create(student: Student):
    student_data = student.dict()
    new_student = await add_student(student_data)
    return new_student

@router.get("/student/{id}", response_model=StudentsInDB)
async def get_student(id: str):
    student = await retrieve_student(id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student Not Found!")

@router.get("/students", response_model=list[StudentsInDB])
async def list_students():
    students = await retrieve_students()
    return students

@router.put("/student/{id}", response_model=StudentsInDB)
async def s_update(id: str, student: Student):
    updated_student = await update_student(id, student.dict())
    if updated_student:
        return updated_student
    raise HTTPException(status_code=404, detail="Student Not Found!")

@router.delete("/student/{id}", response_model=DeleteResponse)
async def s_delete(id: str):
    deleted = await delete_student(id)
    if deleted:
        return {"status": "Student Deleted!"}
    raise HTTPException(status_code=404, detail="Student Not Found!")
