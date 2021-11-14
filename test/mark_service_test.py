import unittest

from servcies.mark_service import MarkService


class TestMarkService(unittest.TestCase):
    def test_store_mark_valid(self):
        mark_service = MarkService()
        student, errors = mark_service.store_mark('1', '1', 50)
        self.assertEqual(errors, None)

    def test_store_mark_id_student_invalid(self):
        mark_service = MarkService()
        mark, errors = mark_service.store_mark('', '1', 50)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'student ID should not be empty')

    def test_store_mark_id_course_invalid(self):
        mark_service = MarkService()
        mark, errors = mark_service.store_mark('1', '', 50)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'course id should not be empty')

    def test_store_student_mark_student_invalid(self):
        mark_service = MarkService()
        mark, errors = mark_service.store_mark('1', '1', 200)
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'student mark should be between 0 and 100')
