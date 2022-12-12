class Profession:
    name = ''
    category = ''
    salary = ''
    work_hours = ''

    def __init__(self):
        print(f"created objects of profession:")
        self.name = "Ukrainian military"
        self.category = 'military'
        self.salary = "Ukraine + Glory"
        self.work_hours = '24/7'
    def ShowOn(self):
        print(f"Name: {self.name} \nCategory: {self.category} \nSalary: {self.salary} \nWork_hours: {self.work_hours}")
    def __del__(self):
        print("deleted objects of profession")
if __name__ == '__main__':
    profession = Profession()
    profession.ShowOn()
    del profession