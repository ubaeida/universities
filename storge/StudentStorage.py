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

    def get_single_student(self):
        for student in self.students:
            return student.sid
        return None


class DBStudentStorage:
    pass
