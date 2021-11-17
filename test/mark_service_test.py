import unittest
from servcies.mark_service import MarkService
from servcies.course_service import CourseService
from servcies.student_service import StudentService

mark_service = MarkService()
student_service = StudentService()
course_service = CourseService()


class TestMarkService(unittest.TestCase):
    def test_store_mark_valid(self):
        student, errors = mark_service.store_mark('1', '1', 50)
        self.assertEqual(errors, None)

    def test_store_mark_id_student_invalid(self):
        mark, errors = mark_service.store_mark('', '1', 50)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'student ID should not be empty')

    def test_store_mark_id_course_invalid(self):
        mark, errors = mark_service.store_mark(1, '', 50)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'course id should not be empty')

    def test_store_student_mark_student_invalid(self):
        mark, errors = mark_service.store_mark('1', '1', 101)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'student mark should be between 0 and 100')

    def test_student_not_exist(self):
        course_service.store_course(1, 'css', 100)
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertEqual(functional_error[0], 'student is not exist or student ID is wrong')

    def test_student_not_match(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(1, 'css', 100)
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'student is not exist or student ID is wrong')

    def test_course_not_exist(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertEqual(functional_error[0], 'course is not exist or student ID is wrong')

    def test_course_not_match(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(3, 'css', 100)
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'course is not exist or student ID is wrong')
