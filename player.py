

from os import times
from command import Command
from item import Item, Mision




class Player():

    def __init__(self, name, max_weight):
        self.name = name
        self.max_weight = max_weight
        self.items = {}
        self.strength = 1
        self.defese = 1
        self.equipment = {'helmet': None, 'weapon': None, 'armor': None}


        

    def setItem(self, item):
        self.items[item.name] = item

    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)

    def can_picked_up_new_item(self, weight):
        peso_total = 0
        for item in self.items.values():
            peso_total += item.weight
        peso_total += weight
        print("You take a item")
        if(peso_total == 0.1):
            print("encuentra la llave antigua que tiene Lucca")
        return peso_total <= self.max_weight 

    def how_many_weight_i_carry(self):
        peso_total = 0
        for item in self.items.values():
            peso_total += item.weight
        print(peso_total)

    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None
