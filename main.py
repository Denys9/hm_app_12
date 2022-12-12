class Musical:
    brand = ''
    category = ''
    strings = 0


    def __init__(self):
        print(f"сreated objects of musical instrument:")
        self.brand = "Yamaha"
        self.category = '6 string guitar'
        self.strings = 6

    def ShowOn(self):
        print(f"brand: {self.brand} \ncategory: {self.category} \nstrings: {self.strings}")
    def __del__(self):
        print("вeleted objects of musical instrument")
if __name__ == '__main__':
    profession = Musical()
    profession.ShowOn()
    del Musical