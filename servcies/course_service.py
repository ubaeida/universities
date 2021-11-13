from models.course import Course
from storge.CourseStorage import MemoryCourseStorage


class CourseService:
    def __init__(self):
        self.memory_course_storage = MemoryCourseStorage()

    def store_course(self, cid, name, max_mark):
        course = Course(_id=cid, name=name, max_mark=max_mark)
        self.memory_course_storage.save_course(course)
        return course
