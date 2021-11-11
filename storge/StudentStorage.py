from models.student import Student


class StudentStorage:
    def save_student(self, student: Student):
        pass


class MemoryStudentStorage(StudentStorage):
    def __init__(self):
        self.students = []

    def save_student(self, student: Student):
        self.students.append(student)

    def get_students(self):
        return self.students


class DBStudentStorage(StudentStorage):
    pass
