class Roll:
    def move(self):
        print("moved! ")
    def call(self):
        print("called! ")
    def calc(self,x,y):
        result = x + y
        print(result)


Roll1 = Roll() 
Roll1.surname = 'das'
print(Roll1.surname)

Roll2 = Roll()
Roll2.name = 'abhishek'
print(Roll2.name)
Roll2.calc(45,78)          