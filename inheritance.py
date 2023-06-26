class Register:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
    def stats(self,ID):
        self.ID = ID
        print(ID)

class data(Register):
    pass

ajit = data('ajit', 21, 6001120442)
rohan = Register('Rohan', 43, 7002345672)

print(ajit.name)
print(rohan.age)
ajit.stats(4556715)

mohit = data('mohit', 66, 9843537372)
mohit.stats(5632)
print(mohit.name)
