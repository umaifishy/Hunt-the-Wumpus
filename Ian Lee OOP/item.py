import random
class Item:

    def __init__(self,name):

        self.name = name
        self.description = ""
        self.damage = 0
        self.healing = 0
        self.value = 0
        self.usable = False
        

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def describe(self):
        print("\n🎒", self.name)
        print(self.description)


