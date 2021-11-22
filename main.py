from servcies.student_service import StudentService
from servcies.course_service import CourseService
from servcies.mark_service import MarkService

student_service = StudentService()
course_service = CourseService()
mark_service = MarkService()


def add_student():
    student_input = input('Enter a student: <id>,<name>,<gender>,<email>\n')
    try:
        _id, name, gender, email = student_input.split(",")
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


def get_total():
    print(mark_service.calculate_student_marks())


def user_input():
    user_input = input(
        """
        select an option by using the option's number : 
        
        0- to exit 
        1- add student
        2- add course
        3- add mark
        4- get student 
        5- get course 
        6- get mark 
        7-get total
        \n --->""")
    user_input.strip()
    action_mapping = {
        '1': lambda: add_student(),
        '2': lambda: add_course(),
        '3': lambda: add_mark(),
        '4': lambda: get_students(),
        '5': lambda: get_course(),
        '6': lambda: get_mark(),
        '7': lambda: get_total()
    }

    while user_input != '0':
        if user_input in action_mapping.keys():
            action_mapping[user_input]()
            user_input = input('Enter the action number\n--->')
        else:
            print('You entered a wrong value, Please check the list again')
            user_input = input('Enter the action number\n--->')


if __name__ == "__main__":
    user_input()
