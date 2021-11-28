import unittest
import random

from models.course import Course
from models.mark import Mark
from models.student import Student, Gender
from storge.CourseStorage import SingletonMemoryCourseStorage
from storge.MarkStorage import SingletonMemoryMarkStorage
from storge.StudentStorage import SingletonMemoryStudentStorage

mark_storage = SingletonMemoryMarkStorage.get_instance()
student_storage = SingletonMemoryStudentStorage.get_instance()
course_storage = SingletonMemoryCourseStorage.get_instance()


class TestMarkStorage(unittest.TestCase):
    def test_custom_filter_test(self):
        for idx in range(1, 10):
            student_storage.save_student(Student(idx, 'mike', Gender.MALE, 'ubaeida.alkayal@gmail.com'))

        for idx in range(30, 40):
            course_storage.save_course(Course(idx, 'Course', 100))

        rand = random.Random()

        for i in range(1, 10):
            for j in range(30, 40):
                mark_storage.save_mark(Mark(i, j, rand.randint(50, 99)))
        marks = mark_storage.get_marks()
        filtered = mark_storage.custom_filter(lambda _mark: _mark.stu_mark == 50)
        for mark in filtered:
            print(mark)

    def test_custom_filter_2(self):
        for idx in range(1, 10):
            student_storage.save_student(Student(idx, 'mike', Gender.MALE, 'ubaeida.alkayal@gmail.com'))

        for idx in range(30, 40):
            course_storage.save_course(Course(idx, 'Course', 100))

        rand = random.Random()

        for i in range(1, 10):
            for j in range(30, 40):
                mark_storage.save_mark(Mark(i, j, rand.randint(50, 99)))
        filtered = mark_storage.custom_filter_2(lambda _mark: _mark.cid == 34,
                                                lambda _mark: _mark.stu_mark > 50)
        for mark in filtered:
            print(mark)
