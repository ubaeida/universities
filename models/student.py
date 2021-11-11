class Student:
    def __init__(self, _id, name, gender, email):
        self.sid = _id
        self.name = name
        self.gender = gender
        self.email = email

    def __str__(self):
        return f"{self.sid}, {self.name},{self.gender},{self.email}"
