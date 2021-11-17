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

    def get_single_course(self):
        for course in self.courses:
            return course.cid
        return None
