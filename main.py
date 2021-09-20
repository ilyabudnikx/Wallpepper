import math
class PiDoor:
    def __init__(self, w, h, name):
        self.w = w
        self.h = h
        self.name = name
    def __repr__(self):
        return f'{self.name} {self.w}*{self.h}'
    def windSquare(self):
        wind_squre = self.w * self.h
        return wind_squre
class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []
    def roomSquare(self):
        room_square = (self.x +self.y) * self.z * 2
        return room_square
    def addWD(self, new_windoor):
        self.wd.append(new_windoor)
    def workSurface(self):
        new_square = self.roomSquare()
        for i in self.wd:
            new_square -= i.windSquare()
        return new_square
class Wallpappers:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pappersValue(self):
        value = (self.x * self.y)
        return value
j = Room(13, 3, 3)
j.addWD(PiDoor(2, 3, 'asdasd'))
j.addWD(PiDoor(2.8, 1, 'asdad12'))
w = Wallpappers(9, 1)


j = Room(100, 50, 3)
j.addWD(PiDoor(2, 1, 'asdasd'))
j.addWD(PiDoor(2.2, 0.8, 'asdad12'))
j.addWD(PiDoor(32, 1.5, 'asde121'))
print('Square room', j.roomSquare())
print('Work Space', j.workSurface())
print('Count  Wallpapper', math. ceil(j.workSurface()/w.pappersValue()))