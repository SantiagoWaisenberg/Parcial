
class Room:
    def __init__(self, description):
        self.description = description
        self.exits = {}  
        self.items = {}
        self.npcs = {}


    def setExits(self, north, east, south, west, up, down, window):
        if(north != None):
            self.exits['north'] = north
        if(east != None):
            self.exits['east'] = east
        if(south != None):
            self.exits['south'] = south
        if(west != None):
            self.exits['west'] = west
        if(up != None):
            self.exits['up'] = up
        if(down != None):
            self.exits['down'] = down
        if(window != None):
            self.exits['window'] = window
        return

    def setItem(self, item):
        self.items[item.name] = item
    
    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None

    def getDescription(self):
        return self.description

    def print_location_information(self):
        print("You are " + self.getDescription())
        print("Exits: ")
        exits = ''
        for direction in self.exits.keys():
            exits += direction + ' '
        print(exits)
        self.print_items_information()
         #self.print_npcs()
    
    def get_exit(self, direction):
        if(direction in self.exits):
            return self.exits[direction]
        else:
            return None

    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)

    def setnoPlayer(self, noPlayer):
       self.npcs[noPlayer.name] = noPlayer
       
    def estanoPlayer(self, noPlayer):
        if(noPlayer in self.npcs):
            print("Here is a player")
            return True
        else:
            False
            


    
        
        