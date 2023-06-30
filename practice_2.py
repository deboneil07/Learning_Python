class Dinner:

    def __init__(self, diet):
        self.diet = diet
        diet = input('are you dieting? or do you want a restricted menu? ')


    def eggs(self, type):
        self.type = type
        print(f'{type} eggs have been added to the list! ')
    def fish(self, specie):
        self.specie = specie
        print(specie)
        

class Lunch(Dinner):
    pass
    
#cake = Dinner()
#recipe = cake.eggs('duck')


buy = Dinner('yes')
curry = buy.fish('salmon')
curry = buy.fish('shark')

#note = Lunch()
#food = note.fish('dolphin')