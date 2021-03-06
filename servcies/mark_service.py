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

    def student_GPA(self, sid: int):
        marks = self.memory_mark_storage.get_student_marks(sid)
        if len(marks) == 0:
            return 'student has no marks', None
        mark_values = list(map(lambda mark: mark.stu_mark, marks))
        total = sum(mark_values)
        avg = total / len(mark_values)
        return None, avg

    def get_course_avg(self, cid: int):
        courses = self.memory_mark_storage.get_course_marks(cid)
        if len(courses) == 0:
            return 'course has no marks', None
        courses_mark = list(map(lambda mark: mark.stu_mark, courses))
        total = sum(courses_mark)
        avg = total / len(courses_mark)
        return None, avg

    def get_marks_page(self, page_no: int, page_size=None):
        if page_no <= 0:
            page_no = 1
        if page_size is None or page_size <= 0:
            page_size = 10
        offset = (page_no - 1) * page_size
        limit = offset + page_size
        return self.memory_mark_storage.get_marks_page(offset, limit)

    def get_marks(self):
        return self.memory_mark_storage.get_marks()

    def custom_filter(self, cid, op, value: int):
        if cid is None:
            return None, ['Course id is invalid']
        if op not in ['<', '=', '>'] or op is None:
            return None, ['Operation invalid ']
        if value not in range(0, 100) or value is None:
            return None, ['Value invalid']
        operation_mapping = {
            '>': lambda mark: mark.cid == cid and mark.stu_mark > value,
            '=': lambda mark: mark.cid == cid and mark.stu_mark == value,
            '<': lambda mark: mark.cid == cid and mark.stu_mark < value
        }
        fun = operation_mapping[op]
        return self.memory_mark_storage.custom_filter(fun)
