class Phone:
    name = ''
    memory = ''
    ram = 0
    d = ''
    type = ''
    iphone = ''
    def __init__(self):
        print(f"created objects of phone:")
        self.name = "iPhone 12"
        self.memory = '128GB'
        self.ram = 4
        self.d = '6,1'
        self.type = 'smartphone'
    def ShowOn(self):
        print(f"name: {self.name} \nmemory: {self.memory} \ndiagonal: {self.d} \ntype: {self.type} \nRAM: {self.ram}")
    def __del__(self):
        print("deleted objects of phone")
if __name__ == '__main__':
    phone = Phone()
    phone.ShowOn()
    del phone