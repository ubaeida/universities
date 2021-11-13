class Course:
    def __init__(self, _id, name, max_mark):
        self.cid = _id
        self.name = name
        self.max_mark = max_mark

    def __str__(self):
        return f"{self.cid}, {self.name}, {self.max_mark}"
