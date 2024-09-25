import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = 'name'
        self.password = hash(password)
        self.age = int(age)

class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = 'title'
        self.duration = int(time.time(duration))
        self.time_now = 0
        self.adult_mode = adult_mode
        