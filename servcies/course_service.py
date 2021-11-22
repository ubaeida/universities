from models.course import Course
from storge.CourseStorage import SingletonMemoryCourseStorage


class Validator:
    def validate(self, course: Course):
        errors = []
        if course.cid == '':
            errors.append('ID should not be empty')
        if course.name is None:
            errors.append('Course name should not be empty')
        if course.max_mark != 100:
            errors.append('Course should not be less 100')
        return errors


class CourseService:
    def __init__(self):
        self.validator = Validator()
        self.memory_course_storage = SingletonMemoryCourseStorage.get_instance()

    def store_course(self, cid, name, max_mark):
        course = Course(_id=int(cid), name=str(name), max_mark=int(max_mark))
        validation_errors = self.validator.validate(course)
        if len(validation_errors) != 0:
            return None, validation_errors
        self.memory_course_storage.save_course(course)
        return course, None

    def get_courses(self):
        return self.memory_course_storage.get_courses()

    def search_course(self, cid):
        return self.memory_course_storage.search_course(cid)
