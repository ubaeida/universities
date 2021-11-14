from models.mark import Mark


class MemoryMarkStorage:
    def __init__(self):
        self.marks = []

    def save_mark(self, mark: Mark):
        self.marks.append(mark)

    def get_marks(self):
        return self.marks
