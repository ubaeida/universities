from models.course import Course


class MemoryCourseStorage:
    def __init__(self):
        self.courses = []

    def save_course(self, course: Course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses
