class Animal():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def eat(self):
        print(self.name+'正在吃')

    def sleep(self):
        print(self.name+'正在睡')

    def introduction(self):
        print('大家好！ 我是 '+self.id+'号 '+self.name+'.')

