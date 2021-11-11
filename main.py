from servcies.student_service import StudentService

student_service = StudentService()


def add_student():
    # student_service.store_student(sid=input("Enter the student's ID:"),
    #                               name=input("Enter the student's name:").strip().capitalize(),
    #                               gender=input("Male or Female? ").strip().capitalize(),
    #                               email=input("Write the student's email;").strip().capitalize())
    user_input = input('Enter a student: <id>,<name>,<gender>,<email> ')
    try:
        _id, name, gender, email = user_input.split(",")
        student, errors = student_service.store_student(_id, name, gender, email)
        if errors is None:
            print(student)
        else:
            print(errors)
    except ValueError:
        print("input should match <id>,<name>,<gender>,<email>")


def get_students():
    print(str(student_service.get_students()))


if __name__ == "__main__":
    add_student()
    get_students()
