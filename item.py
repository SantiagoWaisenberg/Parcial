

class Item:

    def __init__(self, name, description, weight, picked_up=True):
        self.name = name
        self.description = description
        self.weight = weight
        self.picked_up = picked_up

class Comestible(Item):
    
    def __init__(self, name, description, weight, incremet, atribute, picked_up=True):
        super().__init__(name, description, weight, picked_up)
        self.increment = incremet
        self.atribute = atribute
    
    def comer(self, player):
        if(self.atribute in player.__dict__):
            print('current', self.atribute, player.__dict__[self.atribute])
            print('the player eats:', self.name)
            player.__dict__[self.atribute] += self.increment
            print('new', self.atribute, player.__dict__[self.atribute])
            return True
        else:
            print('the player do not have attribute', self.atribute)
            return False
    


class Transportador(Item):

    def __init__(self, name, description, weight, picked_up=True):
        super().__init__(name, description, weight, picked_up=picked_up)
        self.room_back = None

    def is_activate(self):
        return self.room_back

class Equipamineto(Item):
    
    def __init__(self, name, description, weight, type, incremento, picked_up=True):
        super().__init__(name, description, weight, picked_up=picked_up)

class Mision(Item):
    
    def __init__(self, name, description, weight, picked_up=True):
        super().__init__(name, description, weight, picked_up=picked_up)