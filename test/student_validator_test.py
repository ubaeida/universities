import unittest

from models.student import Student, Gender
from servcies.student_service import StudentService, Validator


class StudentValidatorTest(unittest.TestCase):
    def test_validate_email(self):
        validator = Validator()
        student = Student(1, "Muhammad", Gender.MALE, "mhd.durrah@gmail.cominfo")
        errors = validator.validate(student)
        self.assertEqual(errors, None)
