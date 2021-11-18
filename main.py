from servcies.student_service import StudentService
from servcies.course_service import CourseService
from servcies.mark_service import MarkService

student_service = StudentService()
course_service = CourseService()
mark_service = MarkService()


def add_student():
    user_input = input('Enter a student: <id>,<name>,<gender>,<email>\n')
    try:
        _id, name, gender, email = user_input.split(",")
        student, errors = student_service.store_student(_id.strip(), name.capitalize().strip(), gender.upper(),
                                                        email.strip())
        if errors is None:
            print('student has been saved')
        else:
            print(errors)
    except ValueError:
        print("input should match <id>,<name>,<gender>,<email>")


def get_students():
    print(str(student_service.get_students()))


def add_course():
    course_input = input('Enter a course: <id>, <name>, <max_mark>\n')
    try:
        _id, name, max_mark = course_input.split(",")
        course, errors = course_service.store_course(_id.strip(), name.strip().capitalize(), max_mark.strip())
        if errors is None:
            print('Course has been saved')
        else:
            print(errors)
    except ValueError:
        print("input should match : <Id>, <name>, <max_mark>")


def get_course():
    print(str(course_service.get_courses()))


def add_mark():
    mark_input = input('Enter a student mark: <student id>, <course id>, <student mark>\n')
    try:
        sid, cid, stu_mark = mark_input.split(',')
        mark, errors = mark_service.store_mark(sid.strip(), cid.strip(), stu_mark.strip())
        if errors is None:
            print('student mark has been saved')
        else:
            print(errors)
    except ValueError:
        print('input should match: <student id>, <course id>, <student mark>')


def get_mark():
    print(str(mark_service.get_mark()))


if __name__ == "__main__":
    add_student()
    add_student()
    get_students()
    # add_course()
    # get_course()
    add_mark()
    get_mark()
