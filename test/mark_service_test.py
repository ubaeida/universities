import unittest
from servcies.mark_service import MarkService
from servcies.course_service import CourseService
from servcies.student_service import StudentService

mark_service = MarkService()
student_service = StudentService()
course_service = CourseService()


class TestMarkService(unittest.TestCase):

    def test_store_student_mark_student_invalid(self):
        mark, errors = mark_service.store_mark(1, 1, 101)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'student mark should be between 0 and 100')

    def test_student_not_exist(self):
        course_service.store_course(1, 'css', 100)
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertEqual(functional_error[0], 'Student is not exist')

    def test_student_search(self):
        student_service.store_student(3, 'mike', 'MALE', 'ubaeida@gmail.com')
        student_service.store_student(4, 'moh', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(2, 'css', 100)
        mark, functional_error = mark_service.store_mark(5, 2, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'Student is not exist')

    def test_course_not_exist(self):
        student_service.store_student(6, 'mike', 'MALE', 'ubaeida@gmail.com')
        mark, functional_error = mark_service.store_mark(6, 1, 50)
        print(mark, functional_error)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'Course is not exist')

    def test_course_search(self):
        student_service.store_student(7, 'mike', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(4, 'css', 100)
        course_service.store_course(5, 'html', 100)
        mark, functional_error = mark_service.store_mark(7, 3, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'Course is not exist')

    def test_mark_search(self):
        student_service.store_student(8, 'mike', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(6, 'css', 100)
        mark_service.store_mark(8, 6, 50)
        mark, functional_error = mark_service.store_mark(8, 6, 50)

        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'These mark and student already exist')

    def test_marks_calculation(self):
        student_service.store_student(20, 'mike', 'MALE', 'Mike@gmail.com')
        course_service.store_course(7, 'html', 100)
        course_service.store_course(8, 'css', 100)
        course_service.store_course(9, 'php', 100)
        course_service.store_course(10, 'java', 100)
        course_service.store_course(11, 'python', 100)
        course_service.store_course(12, 'c++', 100)
        course_service.store_course(13, 'delphi', 100)
        mark_service.store_mark(20, 7, 35)
        mark_service.store_mark(20, 8, 60)
        mark_service.store_mark(20, 9, 80)
        mark_service.store_mark(20, 10, 77)
        mark_service.store_mark(20, 11, 54)
        mark_service.store_mark(20, 12, 24)
        mark = mark_service.store_mark(20, 13, 91)
        print(mark)

        print(mark_service.calculate_marks())
