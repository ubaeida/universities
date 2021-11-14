from servcies.student_service import StudentService
from servcies.course_service import CourseService
from servcies.mark_service import MarkService

student_service = StudentService()
course_service = CourseService()
mark_service = MarkService()


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
    course_input = input('Enter a course: <id>, <name>, <max mark> ')
    try:
        _id, name, max_mark = course_input.split(",")
        course, errors = course_service.store_course(_id, name, max_mark)
        if errors is None:
            print(course)
        else:
            print(errors)
    except ValueError:
        print("input should match : <Id>, <name>, <max mark>")


def get_course():
    print(str(course_service.get_course()))


def add_mark():
    mark_input = input('Enter a student mark: <student id>, <course id>, <student mark> ')
    try:
        sid, cid, stu_mark = mark_input.split(',')
        mark = mark_service.store_mark(sid, cid, stu_mark)
        print(mark)
    except ValueError:
        print('input should match: <student id>, <course id>, <student mark>')


def get_mark():
    print(str(course_service.get_course()))


if __name__ == "__main__":
    add_student()
    get_students()
    # add_course()
    # get_course()
    # add_mark()
    # get_mark()
