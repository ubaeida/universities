import unittest

from servcies.student_service import StudentService


class TestStudentService(unittest.TestCase):
    def test_store_student_valid(self):
        student_service = StudentService()
        student, errors = student_service.store_student('', '', 'Male', 'durrah@gmail.com')
        self.assertEqual(errors, None)

    def test_store_student_email_invalid(self):
        student_service = StudentService()
        student, errors = student_service.store_student('', '', 'Male', 'durrah@mail.com')
        self.assertIsNotNone(errors)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'email is invalid')
