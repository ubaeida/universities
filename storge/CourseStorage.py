from models.course import Course


class SingletonMemoryCourseStorage:
    __instance = None

    @staticmethod
    def get_instance():
        if SingletonMemoryCourseStorage.__instance is None:
            SingletonMemoryCourseStorage()
        return SingletonMemoryCourseStorage.__instance

    def __init__(self):
        if SingletonMemoryCourseStorage.__instance is not None:
            raise Exception('Singleton already exists')
        else:
            self.courses = []
            SingletonMemoryCourseStorage.__instance = self

    def save_course(self, course: Course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

    def search_course(self, cid):
        for course in self.courses:
            if course.cid == cid:
                return course
        return None
