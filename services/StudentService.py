from models.student import Student, StudentEncoder
from daos.StudentDAO import fetchAll, fetchStudentById, addStudent
from flask import abort
import json

def fetchAllStudents():
    return json.dumps(fetchAll(), cls=StudentEncoder)

def fetchStudent(id):
    result = fetchStudentById(id)
    if(result is None):
        abort(404, description=f"No student found with id {id}")
    return json.dumps(result, cls=StudentEncoder)

def save(jsvalue):
    res = addStudent(Student(jsvalue["id"], jsvalue["name"], jsvalue["gpa"]))
    return "Student created"

