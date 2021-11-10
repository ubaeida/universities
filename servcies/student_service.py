from models.student import Student


class StudentService:

    def store_students(self, sid, name, gender, email):

        student = {'id': sid, 'name': name, 'gender': gender, 'email': email}
        print(student)
