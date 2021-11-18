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
        self.assertEqual(functional_error[0], 'Student is not exist')

    def test_student_search(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        student_service.store_student(2, 'moh', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(1, 'css', 100)
        mark, functional_error = mark_service.store_mark(3, 1, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'Student is not exist')

    def test_course_not_exist(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        mark, functional_error = mark_service.store_mark(1, 1, 50)
        self.assertEqual(functional_error[0], 'Course is not exist')

    def test_course_search(self):
        student_service.store_student(1, 'mike', 'MALE', 'ubaeida@gmail.com')
        course_service.store_course(1, 'css', 100)
        course_service.store_course(2, 'html', 100)
        mark, functional_error = mark_service.store_mark(1, 3, 50)
        self.assertIsNotNone(functional_error)
        self.assertEqual(len(functional_error), 1)
        self.assertEqual(functional_error[0], 'Course is not exist')
