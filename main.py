class Post:
    name = ''
    position = ''
    scale = ''
    type = ''
    def __init__(self):
        print(f"created objects of car:")
        self.name = "TOYOTA Springs"
        self.position = 'Danila Galickiy street'
        self.scale = 'big'
        self.type = 'free'
    def ShowOn(self):
        print(f"name: {self.name} \nposition: {self.position} \nscale: {self.scale} \ntype: {self.type}")
    def __del__(self):
        print("deleted objects of car")
if __name__ == '__main__':
    post = Post()
    post.ShowOn()
    del post