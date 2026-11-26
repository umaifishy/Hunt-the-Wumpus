import random




class Character:

    def __init__(self, char_name, char_description, greeting=""):
        self.name = char_name
        self.description = char_description
        self.conversation = []
        self.health = 100
        self.greeting = greeting
        self.flags = {}
        self.inventory = []

    # define dialogue
    def dialogue(self):
        print(f"\n{self.name}:")
        print(self.get_greeting())
        if len(self.conversation) == 0:
            if isinstance(self, Enemy):
                print("\nThe creature growls at you instead of speaking.")
            else:
                print("\nThey don't seem interested in talking.")
            return None
        while True:
            print()
            options = list(self.conversation.keys())
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            choice = input("> ")

            if not choice.isdigit():
                print("Choose a number.")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(options):
                print("Invalid option.")
                continue

            selected = options[choice - 1]

            data = self.conversation[selected]

            print("\nYou:")
            print(selected)

            if data["action"] == "exit":
                print("You ended the conversation.")
                break

            print(f"\n{self.name}:")
            print(data["reply"])

            if data["action"] in ("fight","fortune", "money", "trade","trade_veg", "pineapple", "davidmoney","gamble_heads","gkingsword" ,"pgive", "gamble_dice", "oil", "farmjob", "givekey","figure"):
                return data["action"]

        return None

    def set_greeting(self, greeting):
        self.greeting = greeting

    def get_greeting(self):
        return self.greeting

    def describe(self):
        print("\n👤", "You find " + self.name)
        print(self.description)

    def set_conversation(self, convo):
        self.conversation = convo



    def fight(self, combat_item):
        print(self.name + " does not want to fight with you")
        return True

    def get_health(self):
        return self.health
# Enemy is a SUBCLASS or CHILD CLASS of Character, by puting the Class Name in ( )
class Enemy(Character):

    # creates the Enemy constrctor method.
    def __init__(self, char_name, char_description, greeting, weakness=None, health=100, damage = 10):
        super().__init__(char_name, char_description, greeting)
        self.weakness = weakness
        self.health = health
        self.max_health = health
        self.money_drop = 0
        self.damage = damage



    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        damage = random.randint(10, 30)
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " attacks you and deals "+str(damage)+" damage!")
            return False

    def is_defeated(self):
        return self.health <= 0

    def take_damage(self, item):
        if self.weakness and item.get_name().lower() == self.weakness.lower():
            print(self.name + " can't stand the " + item.get_name() + "!")
            self.health = 0
            return

        if callable(item.damage):
            damage = item.damage()
        else:
            damage = item.damage

        self.health -= damage

        if self.health < 0:
            self.health = 0

    def attack(self):
            return random.randint(self.damage - 5, self.damage + 5)

    def add_drop(self, item):
        self.inventory.append(item)

    def steal(self):
        print("You steal from " + self.name + "....they are completely clueless!")


# Friend class is also a SUBCLASS of Character, which is the superclass
class Friend(Character):
    def __init__(self, char_name, char_description, greeting):
        super().__init__(char_name, char_description, greeting)
        self.feeling = None

    def pat(self):
        print(self.name + " pats you back!")

    def hug(self):
        print (self.name + " gives you a warm hug! You feel much better now.")


class Merchant(Character):
    def __init__(self, char_name, char_description, greeting="Welcome!"):
        super().__init__(char_name, char_description, greeting)
        self.stock = []
        self.prices = {}

    def add_item(self, item, price):
        self.stock.append(item)
        self.prices[item] = price

    def get_price(self, item):
        return self.prices.get(item, 0)