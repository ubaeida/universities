from models.student import Student, Gender
from storge.StudentStorage import SingletonMemoryStudentStorage
import re

memory_student_storage = SingletonMemoryStudentStorage()


class Validator:
    def validate(self, student: Student):
        errors = []
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        match = re.match(regex, student.email)
        if match is None:
            errors.append('email is invalid')
        if student.gender not in list(Gender):
            errors.append('Gender is invalid')
        if student.name == '':
            errors.append('Name should not be empty')
        if student.sid == '':
            errors.append('ID should not be empty')
        return errors


class StudentService:

    def __init__(self):
        self.validator = Validator()

    def store_student(self, sid, name, gender, email):
        gender_enum = Gender[gender]
        student = Student(sid=int(sid), name=str(name), gender=gender_enum, email=str(email))
        validation_errors = self.validator.validate(student)
        if len(validation_errors) != 0:
            return None, validation_errors
        memory_student_storage.save_student(student)
        return student, None

    def get_students(self):
        return memory_student_storage.get_students()

    def get_single_student(self):
        return memory_student_storage.get_single_student()
