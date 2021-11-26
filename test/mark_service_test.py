import random
import unittest

from models.mark import Mark
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
        student_service.store_student(20, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(21, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        course_service.store_course(7, 'html', 100)
        course_service.store_course(8, 'css', 100)
        course_service.store_course(9, 'php', 100)
        course_service.store_course(10, 'java', 100)
        course_service.store_course(11, 'python', 100)
        course_service.store_course(12, 'c++', 100)
        course_service.store_course(13, 'delphi', 100)
        mark_service.store_mark(20, 7, 60)
        mark_service.store_mark(20, 8, 60)
        mark_service.store_mark(21, 10, 77)
        mark_service.store_mark(21, 11, 54)
        mark_service.store_mark(21, 12, 24)
        mark_service.store_mark(21, 13, 91)
        results = mark_service.student_GPA(21)
        print(results)
        # self.assertIsNotNone(results)
        # self.assertEqual(len(results), 1)

    def test_marks_calculation_withnostudnet(self):
        results = mark_service.student_GPA(22)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], 'Student not exist or has no marks')

    def test_course_average(self):
        student_service.store_student(24, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(25, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(26, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(27, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(28, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        student_service.store_student(29, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')
        course_service.store_course(7, 'html', 100)
        mark_service.store_mark(24, 7, 60)
        mark_service.store_mark(25, 7, 60)
        mark_service.store_mark(26, 7, 77)
        mark_service.store_mark(27, 7, 54)
        mark_service.store_mark(28, 7, 24)
        mark_service.store_mark(29, 7, 91)
        results = mark_service.get_course_avg(7)
        print(results)

    def test_mark_page(self):
        for idx in range(1, 10):
            student_service.store_student(idx, 'mike', 'MALE', 'ubaeida.alkayal@gmail.com')

        for idx in range(30, 40):
            course_service.store_course(idx, 'Course', 100)

        rand = random.Random()

        for i in range(1, 10):
            for j in range(30, 40):
                mark_service.store_mark(i, j, rand.randint(50, 99))
        mark_service.get_mark()
        for mark in mark_service.get_mark():
            print(mark)
        page1 = mark_service.get_marks_page(2, 5)
        print('------------------------------')
        m: Mark = page1[0]
        self.assertEqual(m.sid, 1)
        self.assertEqual(m.cid, 35)

        page1 = mark_service.get_marks_page(3, 17)
        print('------------------------------')
        m: Mark = page1[0]
        self.assertEqual(m.sid, 4)
        self.assertEqual(m.cid, 34)

    def test_lists(self):
        def page(page: int, limt: int, items):
            start_index = (page - 1) * limt
            end_index = start_index + limt
            print(start_index)
            print(end_index)
            print(items[start_index: end_index])

        l = [i for i in range(1, 16)]
        print(l)
        page(10, 5, l)
