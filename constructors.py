class Person:
    def __init__(self,name,age):
        self.name = name
        self.years = age
    def talk(self):
        print('woooozy')


reg = Person('ajit', 45)
print(reg.name)
reg.talk()
print(reg.years)

data = Person('suvam', 16)
print(f'the person is {data.name} and the age is {data.years}')

base = Person('ramu', 33)
base.talk()
print(f"the name is {reg.name} and the age is {base.years}")
