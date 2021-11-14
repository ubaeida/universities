from models.student import Student
from storge.StudentStorage import MemoryStudentStorage


class Validator:
    def validate(self, student: Student):
        errors = []
        if '@gmail.com' not in student.email:
            errors.append('email is invalid')
        if student.gender not in ['Male', 'Female']:
            errors.append('Gender is invalid')
        if student.name == '':
            errors.append('Name should not be empty')
        if student.sid == '':
            errors.append('ID should not be empty')
        return errors


class StudentService:

    def __init__(self):
        self.memory_student_storage = MemoryStudentStorage()
        self.validator = Validator()

    def store_student(self, sid, name, gender, email):
        student = Student(_id=sid, name=name, gender=gender, email=email)
        validation_errors = self.validator.validate(student)
        if len(validation_errors) != 0:
            return None, validation_errors
        self.memory_student_storage.save_student(student)
        return student, None

    def get_students(self):
        return self.memory_student_storage.get_students()
