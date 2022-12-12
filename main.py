class Car:
    name = ''
    engine = ''
    wheel_drive = ''
    hp = 0
    h = 0
    w = 0
    type = ''
    def __init__(self):
        print(f"created objects of car")
        self.name = "BMW M5 E60"
        self.engine = 'V10'
        self.wheel_drive = 'rear'
        self.hp = 507
        self.h = 1470
        self.w = 1850
        self.type = 'sports sedan'
    def ShowOn(self):
        print(f"name: {self.name}, \nengine: {self.engine}, \nwheel drive: {self.wheel_drive},"
              f" \nHP: {self.hp}, \nHigh: {self.h}, \nweight: {self.w}, \ntype: {self.type}")
    def __del__(self):
        print("deleted objects of car")
if __name__ == '__main__':
    car = Car()
    car.ShowOn()
    del car