from flask import Flask, request, abort
from flask_restful import Api
from services.StudentService import fetchAllStudents, save, fetchStudent

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "Index page!"
@app.route("/api/students")
def getStudents():
    return fetchAllStudents()
@app.route("/api/students/add", methods = ["POST"])
def saveStudent():
    return save(request.json)
@app.route("/api/students/<int:id>", methods = ["GET"])
def findById(id):
    return fetchStudent(id)