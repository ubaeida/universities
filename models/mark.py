class Mark:
    def __init__(self, sid, cid, stu_mark):
        self.sid = sid
        self.cid = cid
        self.stu_mark = stu_mark

    def __str__(self):
        return f'{self.sid}, {self.cid}, {self.stu_mark}'