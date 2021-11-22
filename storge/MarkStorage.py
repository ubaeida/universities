from models.mark import Mark


class SingletonMemoryMarkStorage:
    __instance = None

    @staticmethod
    def get_instance():
        if SingletonMemoryMarkStorage.__instance is None:
            SingletonMemoryMarkStorage()
        return SingletonMemoryMarkStorage.__instance

    def __init__(self):
        if SingletonMemoryMarkStorage.__instance is not None:
            raise Exception('Singleton already exists')
        else:
            self.marks = []
            SingletonMemoryMarkStorage.__instance = self

    def save_mark(self, mark: Mark):
        self.marks.append(mark)

    def __str__(self):
        return f'{self.marks}'

    def get_marks(self):
        str(self.marks)
        return self.marks

    def search_mark(self, sid, cid):
        for mark in self.marks:
            if mark.sid == sid and mark.cid == cid:
                return mark
        return None


