from models.mark import Mark
from storge.MarkStorage import MemoryMarkStorage
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
        self.course = CourseService()
        self.student = StudentService()

    def validate(self, mark: Mark):
        functional_errors = []
        student = self.student.search_course(mark.sid)
        if student is None:
            functional_errors.append('Student is not exist')
        course = self.course.search_course(mark.cid)
        if course is None:
            functional_errors.append('Course is not exist')
        return functional_errors


class MarkService:
    def __init__(self):
        self.memory_mark_storage = MemoryMarkStorage()
        self.data_validator = Validator()
        self.functional_validator = FunctionalValidator()

    def store_mark(self, sid, cid, stu_mark):
        mark = Mark(sid=int(sid), cid=int(cid), stu_mark=int(stu_mark))
        validation_error = self.data_validator.validate(mark)
        functional_errors = self.functional_validator.validate(mark)
        if len(validation_error) != 0:
            return None, validation_error
        if len(functional_errors) != 0:
            return None, functional_errors
        self.memory_mark_storage.save_mark(mark)
        return mark, None

    def get_mark(self):
        return self.memory_mark_storage.get_marks()
