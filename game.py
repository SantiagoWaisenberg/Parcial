from os import device_encoding
from room import Room
from item import Item, Comestible, Mision, Transportador
from player import Player
from stack import Stack, inverse
from parser import Parser
from npc import noPlayer


class Game:

    def __init__(self):
        self.createRooms()
        self.player = Player('jugador 1', 20)
        self.parser = Parser()
        self.stack = Stack()

    def createRooms(self):
        outside = Room("outside the main entrance of the university")
        theater = Room("in a lecture theater")
        pub = Room("in the campus pub")
        lab = Room("in a computing lab")
        office = Room("in the computing admin office")
        basement = Room("in the basement")
        playground = Room("in the playground")

        outside.setExits(None, theater, lab, pub, None, None, playground)
        theater.setExits(None, None, None, outside, None, basement, None)
        pub.setExits(None, outside, None, None, None, None, None)
        lab.setExits(outside, office, None, None, None, None, None)
        office.setExits(None, None, None, lab, None, None, None)
        basement.setExits(None, None, None, None, theater, None, None)

        sword = Item('sword', 'this is a rusty sword', 19)
        redBull = Comestible('red bull', 'this is an energy drink', 0.1, 5, 'max_weight')
        rice = Comestible('rice', 'this is a plate of rice', 0.25, 20, 'agility')
        apple = Comestible('apple', 'this is a green apple', 0.15, 7, 'strength')
        shoes = Item('shoes', 'this is an old shoes', 2.87)
        chair = Item('chair', 'you can take a break in this chair', 2)
        wardrobe = Item('wardrobe', 'this is a old wardtibe', 15, picked_up=False)
        cd = Item("CD", "this is a CD of The Beatles", 0.2)
        pendrive = Item("pendrive", "you should not open this in your PC", 0.3)
        transportador = Transportador("transportador", "hola", 0.1)
        mision = Mision("mision", "encuentra la llave antigua que tiene Lucca", 0.1)
        mision = Item("mision", "encuentra la llave antigua que tiene Lucca", 0.1)
        lucca = noPlayer("Lucca")
        andres = noPlayer("Andes")

        outside.setItem(sword)
        outside.setItem(redBull)
        outside.setItem(rice)
        outside.setItem(apple)
        outside.setItem(shoes)
        outside.setItem(wardrobe)
        theater.setItem(chair)
        lab.setItem(cd)
        lab.setItem(pendrive)
        outside.setItem(transportador)
        outside.setItem(mision)
        lab.setnoPlayer(lucca)
        outside.setnoPlayer(andres)

        self.currentRoom = outside

        return

    def play(self):
        self.printWelcome()

        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")

    def printWelcome(self):
        print()
        print("Welcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.")
        print("")
        self.currentRoom.print_location_information()
        print()

    def processCommand(self, command):
        wantToQuit = False

        if(command.isUnknown()):
            print("I don't know what you mean...")
            return False

        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)
        elif(commandWord == "look"):
            self.look_items()
        elif(commandWord == "bag"):
            self.bag_items()
        elif(commandWord == "back"):
            self.goBack()
        elif(commandWord == "take"):
            self.takeItem(command)
        elif(commandWord == "drop"):
            self.dropItem(command)
        elif(commandWord == "eat"):
            self.eatItem(command)
        elif(commandWord == "weight"):
            self.weightBag()
        elif(commandWord == "open"):
            self.llamadoOpen(command)
        elif(commandWord == "activate"):
            self.llamadoActivate(command)
        elif(commandWord == "talk"):
            self.talk(command)
        return wantToQuit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.")
        print()
        print("Your command words are:")
        print("   go quit help")

    def goRoom(self, command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return

        direction = command.getSecondWord()
        nextRoom = self.currentRoom.get_exit(direction)
       
        if(nextRoom is None):
            print("There is no door!")
        else:
            self.currentRoom = nextRoom
            self.currentRoom.print_location_information()
            self.stack.push(direction)
            print()
    
    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return

        item_name = command.getSecondWord()
        item = self.currentRoom.getItem(item_name)
       
        if(item is None):
            print("There is not item in the room with this name!")
        else:
            if(item.picked_up):
                if(self.player.can_picked_up_new_item(item.weight)):
                    self.player.setItem(item)
                    self.player.print_items_information
                else:
                    print('no puedes levantar tanto peso...')
                    self.currentRoom.setItem(item)
            else:
                print('ese item no puede ser levantado')
                self.currentRoom.setItem(item)

    def dropItem(self, command):
        if(not command.hasSecondWord()):
            print("Drop what?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
       
        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            self.currentRoom.setItem(item)

    def eatItem(self, command):
        if(not command.hasSecondWord()):
            print("Eat what?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
       
        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Comestible)):
                response = item.comer(self.player)
                if(not response):
                    self.player.setItem(item)
            else:
                print('este item no es comestible')
                self.player.setItem(item)

    def llamadoActivate(self, command):
        if(not command.hasSecondWord()):
            print("There is not second word")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
        
        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Transportador)):
                if(item.is_activate()):
                    print("teletransportandome")
                    self.currentRoom = item.room_back
                    self.currentRoom.print_location_information()
                else:
                    print("el transportador no fue activado")
                    self.player.setItem(item)
            else:
                print('este item no es un transportador y no se puede activar')
                self.player.setItem(item)
    
        

    def llamadoOpen(self, command):
        if(not command.hasSecondWord()):
            print("There is not second word")
            return
    

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)

        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Transportador)):
                print("room set to back is", self.currentRoom.description)
                item.room_back = self.currentRoom
            else:
                print("este item no es un transportador y no se puede abrir")
            self.player.setItem(item)        

    def weightBag(self):
        self.player.how_many_weight_i_carry()

    def look_items(self):
        self.currentRoom.print_items_information()

    def bag_items(self):
        self.player.print_items_information()
        
    def goBack(self):
        direction = self.stack.pop()
        if(direction):
            nextRoom = self.currentRoom.get_exit(direction)
       
            if(nextRoom is None):
                print("There is no door! to go", direction)
                self.stack.push(inverse[direction])
            else:
                self.currentRoom = nextRoom
                self.currentRoom.print_location_information()
                print()
        else:
            print('you are in the initial position, can not go back')

    def talk(self, command):
        if(not command.hasSecondWord()):
            print("Whit who do you like to talk?")
            return 

        noPlayer_name = command.getSecondWord()
        noPlayer = self.currentRoom.estanoPlayer(noPlayer_name)

        if(noPlayer == "andres"):
            print("Do you hace a fernecito?")
        elif(noPlayer_name == "lucca"):
            print("You complete the quess")



    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True

g = Game()
g.play() 