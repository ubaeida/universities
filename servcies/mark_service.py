from models.mark import Mark
from storge.MarkStorage import MemoryMarkStorage


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
    """
    check student and course existence
    """

    def __init__(self, student_service):
        self.student_service = student_service

    def validate(self, student_id, course_id):
        pass


class MarkService:
    def __init__(self):
        self.memory_mark_storage = MemoryMarkStorage()
        self.data_validator = Validator()

    def store_mark(self, sid, cid, stu_mark):
        mark = Mark(sid=sid, cid=cid, stu_mark=int(stu_mark))
        validation_error = self.data_validator.validate(mark)
        if len(validation_error) != 0:
            return None, validation_error
        self.memory_mark_storage.save_mark(mark)
        return mark, None

    def get_mark(self):
        return self.memory_mark_storage.get_marks()
