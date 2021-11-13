from servcies.student_service import StudentService
from servcies.course_service import CourseService

student_service = StudentService()
course_service = CourseService()


def add_student():
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


def add_course():
    course_input = input('Enter a course: <id>, <name>, <max mark>')
    try:
        _id, name, max_mark = course_input.split(",")
        course = course_service.store_course(_id, name, max_mark)
    except ValueError:
        print("input should match : <Id>, <name>, <max mark>")


if __name__ == "__main__":
    add_student()
    get_students()
    add_course()
