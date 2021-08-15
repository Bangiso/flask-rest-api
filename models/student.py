from json import JSONEncoder
from collections import namedtuple

class Student:
    def __init__(self,id,name,gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__