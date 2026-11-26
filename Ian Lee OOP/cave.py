all_caves = []
class Cave:

    def __init__(self, name, description="", character=None, item=None, discovered=False):
        self.name = name
        self.description = description
        self.linked_caves = {}
        self.character = character
        self.item = item
        self.discovered = discovered
        self.x,self.y  = 0, 0



    def search(self):
        if self.item is None:
            print("You searched far and wide however the area was empty.")
        else:
            self.item.describe()

    def set_description(self, cave_description):
        self.description = cave_description

    def get_description(self):
        return self.description

    def set_name(self, cave_name):
        self.name = cave_name

    def get_name(self):
        return self.name


    def get_character(self):
        return self.character

    def set_character(self, new_character):
        self.character = new_character

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print("\n📍", self.name)
        print("-" * 25)
        print(self.description)

        print("\nExits:")

        for direction in self.linked_caves:
            cave = self.linked_caves[direction]

            if direction == "down":
                print("↓ Down  :", cave.get_name())

            elif direction == "up":
                print("↑ Up    :", cave.get_name())

            elif direction == "left":
                print("← Left  :", cave.get_name())

            elif direction == "right":
                print("→ Right :", cave.get_name())

        print("=" * 50)

    def move(self, direction):
        #gives the cave in direction if none sorry
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("sorry, you cannot go that way")
            return self


    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

def auto_connect(caves):
    for cave in caves:
        for other in caves:
            if cave == other:
                continue
            dx = other.x - cave.x
            dy = other.y - cave.y
            if dx == 1 and dy == 0:
                cave.link_cave(other, "right")
            elif dx == -1 and dy == 0:
                cave.link_cave(other, "left")
            elif dx == 0 and dy == 1:
                cave.link_cave(other, "up")
            elif dx == 0 and dy == -1:
                cave.link_cave(other, "down")

def create_cave(name, description, discovered=False, x=0, y=0):
    cave = Cave(name, description, discovered=discovered)
    cave.x = x
    cave.y = y
    all_caves.append(cave)
    return cave