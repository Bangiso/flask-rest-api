import mysql.connector
from models.student import Student
from mysql.connector.errors import IntegrityError
from flask import abort

db = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user",
  database="StudentDB"
)

def fetchAll():
    students = []
    cursor = db.cursor()
    cursor.execute("SELECT id, name, gpa from students")
    for id, name, gpa in cursor.fetchall():
        students.append(Student(id,name, gpa))
    cursor.close()
    return students
def fetchStudentById(id):
    cursor = db.cursor()
    student = None
    cursor.execute(f"SELECT id, name, gpa from students where id = {id}")
    for id, name, gpa in cursor.fetchall():
        student = Student(id,name, gpa)
    cursor.close()
    return student

def addStudent(student):
    try:
        cursor = db.cursor()
        values = (student.id, student.name, student.gpa)
        cursor.execute(f"INSERT INTO students(id, name, gpa ) values (%s, %s, %s)", values)
        db.commit()
        print(cursor.lastrowid)
    except IntegrityError:
        abort(422, description=f"Student with {student.id} exits")
    except:
        abort(422, description=f"Something went wrong")
    return cursor.lastrowid
