from models.student import Student


# class StudentStorage:
#     def save_student(self, student: Student):
#         pass


class SingletonMemoryStudentStorage:
    __instance = None

    @staticmethod
    def get_course_instance():
        if SingletonMemoryStudentStorage.__instance is None:
            SingletonMemoryStudentStorage()
        return SingletonMemoryStudentStorage.__instance

    def __init__(self):
        if SingletonMemoryStudentStorage.__instance is not None:
            raise Exception('Singleton already exists')
        else:
            self.students = []
            SingletonMemoryStudentStorage.__instance = self

    def save_student(self, student: Student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def search_student(self, mark_sid):
        for student in self.students:
            if student.sid == mark_sid:
                return student.sid
            else:
                return None


class DBStudentStorage:
    pass
