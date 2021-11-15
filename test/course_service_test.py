import unittest

from servcies.course_service import CourseService


class TestCourseService(unittest.TestCase):
    def test_store_course_valid(self):
        course_service = CourseService()
        course, errors = course_service.store_course('1', 'Css', 100)
        self.assertEqual(errors, None)

    def test_store_course_MaxMark_invalid(self):
        course_service = CourseService()
        course, errors = course_service.store_course('1', 'Css', '80')
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Course should not be less 100')

    def test_store_course_id_is_null(self):
        course_service = CourseService()
        course, errors = course_service.store_course('', 'css', 100)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'ID should not be empty')

    def test_store_course_name_is_null(self):
        course_service = CourseService()
        course, errors = course_service.store_course('2', '', 100)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Course name should not be empty')

    def test_store_course_name_is_fake(self):
        course_service = CourseService()
        course, errors = course_service.store_course('2', '  ', 100)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Course name should not be empty')
