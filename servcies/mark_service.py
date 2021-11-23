from models.mark import Mark
from storge.MarkStorage import SingletonMemoryMarkStorage
from servcies.student_service import StudentService
from servcies.course_service import CourseService


class Validator:
    def validate(self, mark: Mark):
        errors = []
        if mark.sid == '':
            errors.append('student ID should not be empty')
        if mark.cid == '':
            errors.append('course id should not be empty')
        if mark.stu_mark < 0 or mark.stu_mark > 100:
            errors.append('student mark should be between 0 and 100')
        return errors


class FunctionalValidator:
    def __init__(self):
        self.course_service = CourseService()
        self.student_service = StudentService()
        self.mark_storage = SingletonMemoryMarkStorage.get_instance()

    def validate(self, mark: Mark):
        functional_errors = []
        student = self.student_service.search_student(mark.sid)
        if student is None:
            return ['Student is not exist']
        course = self.course_service.search_course(mark.cid)
        if course is None:
            return ['Course is not exist']
        mark = self.mark_storage.search_mark(mark.sid, mark.cid)
        if mark is not None:
            return ['These mark and student already exist']
        return functional_errors


class MarkService:
    def __init__(self):
        self.memory_mark_storage = SingletonMemoryMarkStorage.get_instance()
        self.data_validator = Validator()
        self.functional_validator = FunctionalValidator()

    def store_mark(self, sid: int, cid: int, stu_mark: int):
        mark = Mark(sid=int(sid), cid=int(cid), stu_mark=int(stu_mark))
        validation_error = self.data_validator.validate(mark)
        functional_errors = self.functional_validator.validate(mark)
        if len(validation_error) != 0:
            return None, validation_error
        if len(functional_errors) != 0:
            return None, functional_errors
        self.memory_mark_storage.save_mark(mark)
        return mark, None

    def calculate_student_marks(self, sid: int):
        marks = self.memory_mark_storage.get_marks()
        student_marks = []
        student_gpa = []
        for mark in marks:
            if mark.sid == sid:
                student_marks.append(mark.stu_mark)
        if len(student_marks) == 0:
            student_gpa.append('Student not exist or has no marks')
            return student_gpa
        else:
            total = sum(student_marks)
            avg = total / len(student_marks)
            if avg >= 50:
                student_gpa.append(f'the Student average is {format(avg, ".2f")}, and the student passed')
            else:
                student_gpa.append(f'the student average is {format(avg, ".2f")}, and the student fail')
            return student_gpa

    def get_mark(self):
        return self.memory_mark_storage.get_marks()
