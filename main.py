from servcies.student_service import StudentService

StudentService = StudentService()


def get_student():
    StudentService.store_students(sid=input("Enter the student's ID:"),
                                  name=input("Enter the student's name:").strip().capitalize(),
                                  gender=input("Male or Female? ").strip().capitalize(),
                                  email=input("Write the student's email;").strip().capitalize())


if __name__ == "__main__":
    get_student()
