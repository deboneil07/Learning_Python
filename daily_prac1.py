class Dinner:
    def eggs(self, type):
        self.type = type
        print(f'{type} eggs have been added to the list! ')
    def fish(self, specie):
        self.specie = specie
        

class Lunch(Dinner):
    pass
    
cake = Dinner()
recipe = cake.eggs('duck')


buy = Dinner()
curry = buy.fish('salmon')
curry = buy.fish('shark')

note = Lunch()
food = note.fish('dolphin')