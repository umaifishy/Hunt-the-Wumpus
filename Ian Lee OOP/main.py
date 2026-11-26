
from cave import Cave, auto_connect, create_cave, all_caves
from character import Character, Enemy, Friend, Merchant
from item import Item
import random

# ============ CAVE CREATION ============
# Caves placed on coordinate grid and auto-linked by position
cavern = create_cave("Cavern","An eerie, ice-cold breeze gushes from the abyss, whispering your name in the dark.",True,0,1)
grotto = create_cave("Grotto","An eerie, damp breeze gushes from the flooded tunnels, carrying the sound of weeping water.",True,-1,0)
dungeon = create_cave("Dungeon","An eerie breeze gushes down the endless, winding tunnel, making the distant, flickering wall torches sputter in the damp gloom. A forgotten map may be hidden somewhere here...",True,0,0)
mt = create_cave("Mountain","The mountain exhales a bitter, howling draft that nearly throws you off balance in the narrow pass.",True,1,0)
ncp = create_cave("Narrow cliff path","A suffocatingly narrow rock ledge where the howling wind tries to pull you into the endless depths.",False,2,0)
mcom = create_cave("Magic city of Masadora","A wondrous, game-spawned city nestled in a rocky canyon, its strange pink spires radiating raw magical energy into the desert air.",False,3,0)
sanctuary = create_cave("Sanctuary","A quiet, glowing chamber washed in a soothing magical light that washes away all danger.",False,3,-1)
temple = create_cave("Temple","Shadows stretch across ancient stone columns under the silent gaze of towering statues.",False,2,-1)
mp = create_cave("Market_place","A loud, crowded maze of colorful tents, shouting merchants, and flashing gold.",False,1,-1)
ccol = create_cave("Capital City of Limeiro","Towering stone walls enclose a grand, bustling kingdom of white marble and banners fluttering in the wind.",False,0,-1)
ocean = create_cave("Ocean Path","path on ocean",False,-2,0)
island = create_cave("Whale Island","Whale shaped island",False,-3,0)
town = create_cave("Town","small town",False,-1,-1)
river = create_cave("River","river",False,-2,-1)
forest = create_cave("Forest","dark forest",False,-3,-1)
pcave = create_cave("Phophiang's cave","Stinky",False,-3,-2)
dalley = create_cave("Dark Alley","The narrow path makes your ",False,-2,-2)
farm = create_cave("Farmland","Plots of vegetables",False,-1,-2)
grave = create_cave("Graveyard","Haunting presence",False,0,-2)
casino = create_cave("Casino","Large words plastered saying WIN BIG TODAY!!",False,1,-2)
dhouse = create_cave("David's Home","Weirdly shaped house",False,2,-2)
zland = create_cave("Zainland","Private island",False,3,-2)
rground = create_cave("Resting Grounds","Statues fill the room, many names carved on the stone pillar ahead",False,0,-3)
castle = create_cave("Castle","A huge dark presence lurks within",False,0,-4)

all_caves = [cavern, dungeon, grotto, mt, ncp, mcom, sanctuary, temple, mp, ccol,
             town, river, forest, pcave, dalley, farm, grave, casino, dhouse, zland,
             rground, castle, ocean, island]
auto_connect(all_caves)

# ============ DAMAGE FUNCTIONS ============
def calculate_damage():
    # Coin is rigged - only 1/3 chance to deal damage to balance
    roll = random.randint(1, 3)
    if roll == 1:
        return 60
    else:
        return 0

def calculate_fishing_damage():
    # Fishing rod deals random damage each hit
    return random.randint(10, 20)

# ============ ITEM CREATION ============
# All items created and placed in starting locations
map_item = Item("map"); map_item.set_description("A detailed map showing the surrounding caves."); dungeon.set_item(map_item)
vegemite = Item("vegemite"); vegemite.set_description("A wumpus would hate this")
torch = Item("torch"); torch.set_description("A small torch. It can burn enemies for 0-10 damage."); torch.damage = lambda: random.randint(0,10); torch.usable = True; mt.set_item(torch)
apple = Item("apple"); apple.set_description("A fresh apple."); apple.healing = 20; apple.usable = True; farm.set_item(apple)
sword = Item("sword"); sword.set_description("The real king sword??, deals 45-55 damage"); sword.damage = lambda: random.randint(45,55); sword.usable = True
potion = Item("potion"); potion.set_description("A bubbling healing potion, heals 50 hp"); potion.healing = 50; potion.usable = True
tpcard = Item("tpcard"); tpcard.set_description("Teleports you back to any location you've already discovered."); tpcard.usable = True; sanctuary.set_item(tpcard)
mark_potion = Item("big potion"); mark_potion.set_description("A bubbling healing potion, heals 80 hp"); mark_potion.healing = 80; mark_potion.usable = True
fishing_rod = Item("fishingrod"); fishing_rod.set_description("A fishing rod, deals 10-20 damage"); fishing_rod.damage = calculate_fishing_damage; fishing_rod.usable = True; island.set_item(fishing_rod)
coin = Item("coin"); coin.set_description("Flip a coin for a chance to deal 60 damage or 0 damage"); coin.damage = calculate_damage; coin.usable = True; casino.set_item(coin)
oil = Item("oil"); oil.set_description("A bottle of slippery oil. Deals 30 damage"); oil.damage = 30; oil.usable = True
herb = Item("healing herb"); herb.set_description("A rare plant used for healing."); herb.healing = 30; herb.usable = True; forest.set_item(herb)
mega_potion = Item("mega potion"); mega_potion.set_description("Restores 100 HP."); mega_potion.healing = 100; mega_potion.usable = True
vine = Item("vine"); vine.set_description("Spiky vine whip, deals 20 damage."); vine.damage = lambda: random.randint(20,23); vine.usable = True; grotto.set_item(vine)
magic_scroll = Item("magic scroll"); magic_scroll.set_description("A magical scroll that reveals the entire world map."); magic_scroll.usable = True
weakness_scroll = Item("weakness scroll"); weakness_scroll.set_description("A forbidden scroll that reveals enemy weaknesses forever."); weakness_scroll.usable = True
ryoshu_figurine = Item("ryoshu_figurine"); ryoshu_figurine.set_description("Phopiang's figurine, deals 10-30 damage"); ryoshu_figurine.damage = lambda: random.randint(10,30); ryoshu_figurine.usable = True
kingsword = Item("kingsword"); kingsword.set_description("A rusty old sword, deals 0 to 30 damage"); kingsword.damage = lambda: random.randint(0,30); kingsword.usable = True
pineapple = Item("pineapple"); pineapple.set_description("A pineapple, maybe feed it to the ???")
fruit = Item("fruit"); fruit.set_description("A rare fruit that heals 100 hp, allows overheal.");fruit.healing = 100; fruit.usable = True;ncp.set_item(fruit)
castle_key = Item("Castle Key"); castle_key.set_description("An old iron key. It might open something important.")
trident = Item("trident");trident.set_description("An ancient trident belonging to the almighty sea king, damage increases by 1.5x after each hit.");trident.current_damage = 5;trident.usable = True
water_scroll = Item("waterscroll");water_scroll.set_description("A magical scroll blessed by the Sea King. Casts a water shield reducing damage by 30% and deals 5 damage. Infinite uses.");water_scroll.damage = lambda: 5;water_scroll.usable = True
def trident_damage():
    damage = int(trident.current_damage)
    trident.current_damage = max(1, int(trident.current_damage * 1.5))
    return damage

trident.damage = trident_damage
# ============ CHARACTER CREATION ============
# River monster - defeated by fishingrod
rivmon = Enemy("River monster","Large snake like creature slithering along the river, white scales reflecting the bright sunlight","Hissss.....","fishingrod",50,10)
rivmon.set_conversation({
    "What do you hate?": {"reply": "Fishing rods for sure!!", "action": None},
    "I hate you": {"reply": "Okay then,,,,", "action": "fight"},
    "Goodbye": {"reply": "", "action": "exit"}
})
rivmon.money_drop = 40
river.set_character(rivmon)

# ??? - mystery enemy, defeated by pineapple
mark = Enemy("???","Scary looking ?????","?????I... hate.... pineapples","pineapple",999,15)
mark.set_conversation({
    "I love pineapples": {"reply": "NOOOOOOOOOOOOOOOOOO", "action": "fight"},
    "Why do you hate pineapples?": {"reply": "Zac....he appears in my nightmares", "action": None},
    "Goodbye": {"reply": "", "action": "exit"}
})
mark.money_drop = 100
mark.add_drop(mark_potion)
temple.set_character(mark)

sking=Enemy("Sea King", "King of the Ocean", "Greetings adventurer", "kingsword",150, 20)
sking.money_drop = 100
sking.set_conversation({
    "I want your trident": {"reply": "No you shall not take my trident!!", "action": "fight"},
    "Can I have something?": {"reply": "", "action": "pgive"},
    "Goodbye": {"reply": "", "action": "exit"}
})
sking.add_drop(trident)
ocean.set_character(sking)
# Harry the Wumpus - main boss, defeated by vegemite
harry = Enemy("Harry","The sickening odor of decay hits you instantly—the hulking Wumpus is right here in the dark, just feet away.","The wumpus growls at you..","vegemite",200,30)
harry.set_conversation({
    "Fight me!": {"reply": "Very well...", "action": "fight"},
    "Why are you here?": {"reply": "Because I am always hungry.", "action": None},
    "Goodbye": {"reply": "", "action": "exit"}
})
castle.set_character(harry)



# Thief - defeated by coin
thief = Enemy("Thief","A hooded figure lurks in the shadows.","Hand over your money!","coin",70,18)
thief.set_conversation({
    "I dont want to": {"reply": "", "action": "fight"},
    "Goodbye": {"reply": "You ain't getting away from me!", "action": "fight"}
})
thief.money_drop = 50
dalley.set_character(thief)

# Skeleton - defeated by torch
skeleton = Enemy("Skeleton","Bones rattle as the hollow figure approaches slowly.","...","torch",90,20)
skeleton.money_drop = 60
grave.set_character(skeleton)

# Fortune teller in sanctuary
fortune = Friend("Fortune Teller","An old woman surrounded by glowing crystal balls.","The future is always changing...")
fortune.set_conversation({
    "Tell me my fortune": {"reply": "", "action": "fortune"},
    "Goodbye": {"reply": "", "action": "exit"}
})
sanctuary.set_character(fortune)

# Phophiang in his cave
phop = Friend("Phophiang","Cool cool guy","I want a girlfriend 😔")
phop.set_conversation({
    "Why not a boyfriend?": {"reply": "cuz i want a girlfriend?", "action": None},
    "Gimme something": {"reply": "", "action": "figure"},
    "Goodbye": {"reply": "", "action": "exit"}
})
pcave.set_character(phop)

# Zain on his island
zain = Friend("Zain","Zain","I like fish")
zain.set_conversation({
    "How's your island?": {"reply": "I love it", "action": None},
    "Gimme something": {"reply": "", "action": "oil"},
    "Goodbye": {"reply": "", "action": "exit"}
})
zland.set_character(zain)

# David at his home
david = Friend("David","David","David")
david.set_conversation({
    "Who are you?": {"reply": "David", "action": None},
    "Can I have money?": {"reply": "David", "action": "davidmoney"},
    "Goodbye": {"reply": "David", "action": "exit"}
})
dhouse.set_character(david)

# Farmer Bob at the farm
farmer = Friend("Farmer Bob","A hardworking farmer covered in dirt.","The crops won't harvest themselves!")
farmer.set_conversation({
    "Work on the farm": {"reply": "Sure! Help me harvest today's crops.", "action": "farmjob"},
    "Goodbye": {"reply": "", "action": "exit"}
})
farm.set_character(farmer)

# Zac at the casino
zac = Friend("Zac","Casino guy","I like pineapples")
zac.set_conversation({
    "I wanna gamble!": {"reply": "Pick a game below and I'll set you up!", "action": None},
    "I want to play heads or tails!": {"reply": "Let us begin", "action": "gamble_heads"},
    "Can we play roll the dice?": {"reply": "Here we go", "action": "gamble_dice"},
    "Can I have a pineapple?": {"reply": "", "action": "pineapple"},
    "Goodbye": {"reply": "", "action": "exit"}
})
casino.set_character(zac)

# Josephine the bat in grotto
josephine = Friend("Josephine","A bat","Hello there traveller...")
josephine.set_conversation({
    "Who are you?": {"reply": "I'm Josephine. I've lived in these caves for years.", "action": None},
    "Any advice?": {"reply": "I heard the Wumpus can't stand Vegemite.", "action": None},
    "Goodbye": {"reply": "", "action": "exit"}
})
grotto.set_character(josephine)

# King Aldric in Capital City - gives castle key
king = Friend("King Aldric","The ruler of Limeiro, dressed in shining royal armour.","Welcome, traveller.")
king.set_conversation({
    "Why is the castle locked?": {"reply": "The Wumpus has taken the castle. We sealed it until someone worthy appeared.", "action": None},
    "I'll take him down.": {"reply": "Perhaps you truly are the hero we've been waiting for.", "action": "givekey"},
    "Can I have a weapon?": {"reply": "", "action": "gkingsword"},
    "Goodbye": {"reply": "", "action": "exit"}
})
ccol.set_character(king)

# Zepile the merchant at marketplace
zepile = Merchant("Zepile","A traveling merchant with a cart full of gear.","Welcome, welcome! Take a look at my wares.")
zepile.set_conversation({
    "Show me your wares": {"reply": "Take your pick!", "action": "trade"},
    "Goodbye": {"reply": "Safe travels!", "action": "exit"}
})
zepile.add_item(sword, 120)
zepile.add_item(potion, 20)
zepile.add_item(potion, 20)
zepile.add_item(potion, 20)
zepile.add_item(potion, 20)
mp.set_character(zepile)

# Frieren the mage merchant in Masadora
mage = Merchant("Frieren","An elf mage surrounded by glowing potions.","Magic is beautiful.")
mage.set_conversation({
    "What do you have?": {"reply": "All the best stuff", "action": "trade"},
    "Goodbye": {"reply": "", "action": "exit"}
})
mage.add_item(mega_potion, 80)
mage.add_item(magic_scroll, 10)
mage.add_item(weakness_scroll, 50)
mcom.set_character(mage)


townsman = Friend("Townsman", "A nervous looking man.", "I have something... but I need help first.")
townsman.set_conversation({
    "Do you have vegemite?!": {"reply": "Vegemite. But I'll only trade it for a coin from the Casino.", "action": None},
    "Here's a coin": {"reply": "", "action": "trade_veg"},
    "Goodbye": {"reply": "Please hurry...", "action": "exit"}
})
townsman.flags["traded"] = False
town.set_character(townsman)

# ============ HELPER FUNCTIONS ============
def display_map():
    """Displays discovered caves on a coordinate grid map"""
    print("\n🗺️ MAP\n")
    min_x = min(cave.x for cave in all_caves)
    max_x = max(cave.x for cave in all_caves)
    min_y = max(cave.y for cave in all_caves)
    max_y = min(cave.y for cave in all_caves)
    for y in range(min_y, max_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            cave_here = None
            for cave in all_caves:
                if cave.x == x and cave.y == y:
                    cave_here = cave
                    break
            if cave_here is None:
                row += " " * 18
            elif cave_here.discovered:
                short_name = " ".join(cave_here.get_name().split()[:2])
                if cave_here == current_cave:
                    short_name = f"📍>{short_name}"
                row += f"{short_name:<18}"
            else:
                if cave_here == current_cave:
                    row += f"{'📍>?':<18}"
                else:
                    row += f"{'?':<18}"
        print(row)

def find_item(name):
    """Searches player bag for item by name"""
    for i in bag:
        if i.get_name().lower() == name:
            return i
    return None

def show_bag():
    """Shows contents of player bag"""
    if len(bag) == 0:
        print("Your bag is empty...")
    else:
        print("You are carrying:", ", ".join(i.get_name() for i in bag))
        print("Type examine to examine specific items")

def show_stats():
    """Displays player HP, money and inventory"""
    print("\n===== PLAYER STATS =====")
    if player_hp > player_max_hp:#for fruit overheal
        print(f"HP: {player_hp}/{player_max_hp} 💚 (Overhealed!)")
    else:
        print(f"HP: {player_hp}/{player_max_hp}")
    print(f"Money: ${player_money}")
    print("Inventory: Empty" if len(bag) == 0 else "Inventory: " + ", ".join(i.get_name() for i in bag))
    print("=" * 24)

def teleport_menu():
    """Lets player teleport to any discovered cave"""
    global current_cave
    discovered = [c for c in all_caves if c.discovered]
    print("Choose a discovered location to teleport to (or 'cancel'):")
    for c in discovered:
        print(" -", c.get_name())
    choice = input("> ").strip().lower()
    if choice == "cancel":
        print("Teleport cancelled.")
        return
    for c in discovered:
        if c.get_name().lower() == choice:
            current_cave = c
            print("You teleport to " + c.get_name() + "!")
            return
    print("You haven't discovered that location yet.")

def examine_item():
    """Lets player read description of an item in their bag"""
    print("What item do you wanna examine?")
    look_for = input("> ").strip().lower()
    target = find_item(look_for)
    if target is not None:
        target.describe()
    else:
        print("You don't have a [" + look_for + "] in your bag.")

# ============ GAME FUNCTIONS ============
def farming_game():
    """Mini game where player harvests crops for money"""
    global player_money
    print("\n🌱 Farmer Bob's Farm")
    print("Farmer Bob: Welcome! The crops won't harvest themselves.")
    print("Type 'harvest' to collect crops, or 'leave' to stop working.")
    crops_harvested = 0
    while True:
        action = input("> ").strip().lower()
        if action == "leave":
            print(f"Farmer Bob: Good work! You harvested {crops_harvested} crops today.")
            print("You earned $" + str(crops_harvested * 5))
            player_money += crops_harvested * 5
            return
        elif action == "harvest":
            event = random.randint(1, 10)
            if event <= 7:
                crops = random.randint(1, 3)
                crops_harvested += crops
                print(f"🌽 You harvested {crops} crops!")
            elif event == 8:
                print("✨ You found a golden vegetable!")
                crops_harvested += 5
            elif event == 9:
                print("🐛 Some crops were eaten by bugs...")
                print("You only saved 1 crop.")
                crops_harvested += 1
            else:
                print("🌧️ Rain ruined some crops, but Farmer Bob thanks you.")
                crops_harvested += 2
            print(f"Current harvest: {crops_harvested} crops")
        else:
            print("Farmer Bob: Just type 'harvest' or 'leave'.")

def run_battle(enemy, bag):
    """Handles turn-based combat between player and enemy"""
    global player_hp, dead, player_money
    abilities["water_shield"] = False
    print(f"\n⚔️ You are fighting {enemy.name}! ({enemy.health}/{enemy.max_health} HP)")
    while not enemy.is_defeated():
        if player_hp > player_max_hp:
            hp_display = f"{player_hp}/{player_max_hp} 💚"
        else:
            hp_display = f"{player_hp}/{player_max_hp}"
        print(f"\n{enemy.name}: {enemy.health}/{enemy.max_health} HP   |   You: {hp_display} HP")
        if abilities["weakness_scroll"] and enemy.weakness:
            print("📜 Weakness Scroll: " + enemy.name + " is weak to " + enemy.weakness + "!")
        print("Type an item name to use it, or: bag, stats, examine, flee")
        action = input("> ").strip().lower()

        if action == "flee":#when fleeing has a chance of taking damage
            if random.randint(1, 4) == 1:
                flee_damage = 5
                player_hp -= flee_damage
                print(f"{enemy.name} strikes you as you turn to run! You take {flee_damage} damage!")
                if player_hp <= 0:
                    player_hp = 0
                    print("\nYou were struck down while fleeing..oh no how sad.")
                    if replay_game():
                        return False
                    else:
                        dead = True
                        return False
            print("You fled from the fight!")
            return False

        if action == "bag":
            show_bag(); continue
        if action == "stats":
            show_stats(); continue
        if action == "examine":
            examine_item(); continue

        target = find_item(action)#item not present in bag
        if target is None:
            print("You don't have a '" + action + "' to use.")
            continue

        acted = False
        is_weakness = enemy.weakness and target.get_name().lower() == enemy.weakness.lower()

        if target.healing > 0:
            if target.get_name().lower() == "fruit":
                player_hp += target.healing
                print(" You eat the fruit and overheal! You now have " + str(player_hp) + " HP!")
            else:
                healed = min(target.healing, player_max_hp - player_hp)
                player_hp += healed
                print("You eat the " + target.get_name() + " and recover " + str(healed) + " HP.")
            bag.remove(target)
            continue

        if is_weakness:
            enemy.health = 0
            print("The " + target.get_name() + " is extremely effective against " + enemy.name + "!")
            acted = True

        elif callable(target.damage):
            damage = target.damage()
            enemy.health -= damage
            if enemy.health < 0:
                enemy.health = 0
            # Harry cannot be killed without vegemite
            if enemy is harry and not is_weakness:
                if enemy.health <= 0:
                    enemy.health = 1
                    print("\n🛡 Harry staggers but refuses to fall!")
                    print("Harry: Those weapons can't kill me...wahahahahah")
                    has_vegemite = any(i.get_name().lower() == "vegemite" for i in bag)
                    if not has_vegemite:
                        print("💡 Hint: Maybe there's something at the town the Wumpus truly fears...")
                    else:
                        print("💡 You have something in your bag Harry really hates...")
            if target.get_name().lower() == "coin":
                if damage == 0:#coin with special damage
                    print("🪙 The coin landed on tails! You dealt 0 damage!")
                else:
                    print("🪙 The coin landed on heads! Critical hit! You dealt 60 damage!")
            elif target.get_name().lower() == "waterscroll":
                print("You used the waterscroll and dealt " + str(damage) + " damage!")
                abilities["water_shield"] = True
                print("🌊 A water barrier surrounds you! Incoming damage reduced by 30%!")
            else:
                print("You used the " + target.get_name() + " and dealt " + str(damage) + " damage!")
            acted = True

        elif target.damage > 0:
            damage_before = enemy.health
            enemy.take_damage(target)
            damage_done = damage_before - enemy.health
            print("You hit " + enemy.name + " with the " + target.get_name() + " for " + str(damage_done) + " damage!")
            if enemy is harry and not is_weakness:
                if enemy.health <= 0:
                    enemy.health = 1
                    print("\n🛡️ Harry staggers but refuses to fall!")
                    print("Harry: Those weapons can't kill me...wahahahahah")
                    has_vegemite = any(i.get_name().lower() == "vegemite" for i in bag)
                    if not has_vegemite:
                        print("💡 Hint: Maybe there's something at the town the Wumpus truly fears...")
                    else:
                        print("💡 You have something in your bag Harry really hates...")
            if target.get_name().lower() == "oil":
                bag.remove(target)
                print("The oil bottle shatters!")
            acted = True

        if not acted:#give hints to player
            print("The " + target.get_name() + " has no effect on " + enemy.name + ".")
            hints = {
                "Harry": "The Wumpus hates something people spread on toast...",
                "???": "The creature seems terrified of tropical fruit...",
                "River monster": "Maybe something fishermen usually carry..."
            }
            if enemy.name in hints:
                print("Hint:", hints[enemy.name])
            if abilities["weakness_scroll"] and enemy.weakness:
                print("📜 Weakness Scroll:", enemy.name, "is weak to", enemy.weakness + "!")
            continue

        if enemy.is_defeated():
            break

        damage = enemy.attack()
        if abilities["water_shield"]:
            reduced = int(damage * 0.3)
            damage -= reduced
            print("🌊 Water barrier absorbs " + str(reduced) + " damage!")
        player_hp -= damage
        print(enemy.name + " attacks you for " + str(damage) + " damage!")
        if player_hp <= 0:
            player_hp = 0
            print("\nYou have been defeated.")
            if replay_game():
                return False
            else:
                dead = True
                return False

    print("\nYou defeated " + enemy.name + "!")
    player_money += enemy.money_drop
    if enemy.money_drop > 0:
        print(f"You found ${enemy.money_drop}!")
    for drop in enemy.inventory:
        bag.append(drop)
        print("You found a " + drop.get_name() + "!")
    return True

def run_shop(merchant):
    """Handles buying items from a merchant"""
    global player_money
    print("\n🛒 " + merchant.name + "'s shop")
    if len(merchant.stock) == 0:
        print(merchant.name + " has nothing left to sell.")
        return
    while True:
        print(f"Balance: ${player_money}")
        print("\nFor sale:")
        for i in merchant.stock:
            print(f" - {i.get_name()} : ${merchant.get_price(i)}")
        print("Type an item name to buy it, or 'leave'")
        choice = input("> ").strip().lower()
        if choice == "leave":
            print("You leave the shop.")
            return
        target = None
        for i in merchant.stock:
            if i.get_name().lower() == choice:
                target = i
                break
        if target is None:
            print(merchant.name + " doesn't sell that.")
            continue
        price = merchant.get_price(target)
        if player_money < price:
            print("You can't afford that.")
            continue
        player_money -= price
        bag.append(target)
        merchant.stock.remove(target)
        print("You bought the " + target.get_name() + " for $" + str(price) + "!")

def tell_fortune():
    """Prints a random fortune hint about the game"""
    fortunes = [
        "🔮 I see a wumpus that despises Vegemite...",
        "🔮 A skeleton fears bright flames.",
        "🔮 The river beast avoids fishing rods.",
        "🔮 Someone in the kingdom protects an important key.",
        "🔮 A pineapple will strike fear into ????.",
        "🔮 Not every battle requires strength. Sometimes the right item is enough.",
        "🔮 Merchants often sell equipment worth saving money for.",
        "🔮 Explore every path. Valuable treasures hide in unexpected places.",
        "🔮 The Wumpus is stronger than it looks...",
        "🔮 A magical scroll can reveal the world itself."
    ]
    print(random.choice(fortunes))

def play_heads_or_tails():
    """Heads or tails betting mini game"""
    global player_money
    print("\n🪙 Heads or tails! (Money: $" + str(player_money) + ")")
    while True:
        print("How much do you want to bet? (or 'cancel')")
        bet_text = input("> ").strip().lower()
        if bet_text == "cancel":
            print("Maybe next time.")
            return
        if not bet_text.isdigit():
            print("Enter a whole number.")
            continue
        bet = int(bet_text)
        if bet <= 0:
            print("Your bet must be greater than 0.")
            continue
        if bet > player_money:
            print("You don't have that much money.")
            continue
        break
    while True:
        print("Heads or tails?")
        guess = input("> ").strip().lower()
        if guess in ["heads", "tails"]:
            break
        print("Please type 'heads' or 'tails'.")
    result = random.choice(["heads", "tails"])
    print("The coin lands on... " + result + "!")
    if guess == result:
        player_money += bet
        print("You won $" + str(bet) + "!")
    else:
        player_money -= bet
        print("You lost $" + str(bet) + ".")

def play_dice():
    """Dice number guessing mini game"""
    global player_money
    print("\n🎲 Roll the dice! (Money: $" + str(player_money) + ")")
    while True:
        print("How much do you want to bet? (or 'cancel')")
        bet_text = input("> ").strip().lower()
        if bet_text == "cancel":
            print("Maybe next time.")
            return
        if not bet_text.isdigit():
            print("Enter a whole number.")
            continue
        bet = int(bet_text)
        if bet <= 0:
            print("Your bet must be greater than 0.")
            continue
        if bet > player_money:
            print("You don't have that much money.")
            continue
        break
    while True:
        print("Guess a number from 1 to 6:")
        guess_text = input("> ").strip()
        if guess_text.isdigit():
            guess = int(guess_text)
            if 1 <= guess <= 6:
                break
        print("Please enter a number from 1 to 6.")
    roll = random.randint(1, 6)
    print("The die lands on " + str(roll) + "!")
    if guess == roll:
        winnings = bet * 5
        player_money += winnings
        print("You won $" + str(winnings) + "!")
    else:
        player_money -= bet
        print("You lost $" + str(bet) + ".")

# ============ TUTORIAL - LEVEL 1 ============
def run_tutorial_level():
    """Guided tutorial teaching core game mechanics before main game"""
    tutorial_bag = []
    tutorial_hp = 100

    print("\n" + "=" * 50)
    print("              LEVEL 1: TUTORIAL")
    print("=" * 50)
    print("Welcome to the tutorial!")
    print("I am IAN LEE and I'll teach you how to play my game")
    print("Type exactly what the tutorial asks.")
    print("Type 'quit' anytime to leave the tutorial.\n")

    # Stage 1 - movement
    print("Tutorial 1/7: Movement")
    print("Type 'up' to move forward.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "up":
            print("✅ Nice! You moved forward."); break
        else:
            print("Type 'up' to continue.")

    # Stage 2 - take item
    print("\nTutorial 2/7: Taking items")
    print("You found a practice sword.")
    print("Type 'take' to pick it up.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "take":
            tutorial_bag.append("sword")
            print("✅ You picked up the sword."); break
        else:
            print("Type 'take' to pick up the sword.")

    # Stage 3 - check bag
    print("\nTutorial 3/7: Inventory check")
    print("Type 'bag' to check what you're carrying.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "bag":
            if len(tutorial_bag) == 0:
                print("Your bag is empty...")
            else:
                print("You are carrying:", ", ".join(tutorial_bag))
            print("✅ Now you can check the inventory"); break
        else:
            print("Type 'bag' to continue.")

    # Stage 4 - search
    print("\nTutorial 4/7: Searching")
    print("There seems to be something hidden nearby.")
    print("Type 'search' to inspect the area.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "search":
            print("You searched the area carefully...")
            print("✅ You found some vegemite hidden in the rocks!")
            tutorial_bag.append("vegemite"); break
        else:
            print("Type 'search' to continue.")

    # Stage 5 - talk
    print("\nTutorial 5/7: Talking")
    print("A friendly training bat appears.")
    print("Type 'talk' to speak with them.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "talk":
            print("\nTraining Bat:")
            print("Hello traveller! Some enemies can be beaten normally,")
            print("but others have a special weakness item.")
            print("Keep that in mind...")
            print("✅ Nice! Talking to characters can give hints."); break
        else:
            print("Type 'talk' to continue.")

    # Stage 6 - normal fight
    print("\nTutorial 6/7: Fighting")
    print("A Training Skeleton appears!")
    print("Type 'fight' to begin battle.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "fight":
            break
        else:
            print("Type 'fight' to begin.")

    enemy_hp = 30
    while enemy_hp > 0:
        print(f"\nTraining Skeleton: {enemy_hp}/30 HP   |   You: {tutorial_hp}/100 HP")
        print("Type 'sword' to attack, or 'bag' to check inventory.")
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "bag":
            print("You are carrying:", ", ".join(tutorial_bag))
        elif action == "sword":
            damage = random.randint(12, 18)
            enemy_hp -= damage
            if enemy_hp < 0:
                enemy_hp = 0
            print(f"✅ You used the sword and dealt {damage} damage!")
        else:
            print("Type 'sword' to attack.")
    print("✅ You defeated the Training Skeleton!")

    # Stage 7 - weakness fight
    print("\nTutorial 7/7: Enemy weakness")
    print("A Mini Wumpus appears! This enemy has a special weakness.")
    print("Type 'fight' to begin battle.")
    while True:
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "fight":
            break
        else:
            print("Type 'fight' to begin.")

    while True:
        print(f"\nMini Wumpus: 999/999 HP   |   You: {tutorial_hp}/100 HP")
        print("Try using an item from your tutorial bag.")
        action = input("> ").strip().lower()
        if action == "quit":
            print("Leaving tutorial..."); return
        elif action == "bag":
            print("You are carrying:", ", ".join(tutorial_bag))
        elif action == "sword":
            print("The Mini Wumpus barely reacts...")
            print("❗ This enemy must have a special weakness.")
        elif action == "vegemite":
            print("✅ The vegemite is extremely effective against the Mini Wumpus!")
            print("The Mini Wumpus is defeated instantly!")
            break
        else:
            print("Try using one of your items.")

    print("\n" + "=" * 50)
    print("Tutorial complete! You learned:")
    print("- how to move")
    print("- how to take items")
    print("- how to check your bag")
    print("- how to search")
    print("- how to talk to characters")
    print("- how to fight normally")
    print("- how to use enemy weaknesses")
    print("=" * 50)
    input("Press Enter to return to the menu...")

# ============ MAIN MENU ============
def show_main_menu():
    """Displays main menu with tutorial and game options"""
    while True:
        print("\n" + "=" * 50)
        print("               HUNT THE WUMPUS")
        print("=" * 50)
        print("1. Level 1: Tutorial")
        print("2. Level 2: Main Game")
        print("3. Help / Commands")
        print("4. Quit")
        print("=" * 50)
        choice = input("> ").strip()
        if choice == "1":
            run_tutorial_level()
        elif choice == "2":
            return
        elif choice == "3":
            print("\n" + commands)
            input("Press Enter to return to the menu...")
        elif choice == "4":
            print("Thanks for playing!")
            quit()
        else:
            print("Please choose 1, 2, 3 or 4.")

# ============ RESET AND REPLAY ============
def reset_game():
    global current_cave, bag, player_hp, player_money, has_map, dead, abilities

    current_cave = cavern
    bag.clear()
    player_hp = player_max_hp
    player_money = 0
    has_map = False
    dead = False

    # Reset all cave discovery states
    for cave in all_caves:
        cave.discovered = False
    cavern.discovered = True

    # Put items back in their starting locations
    dungeon.set_item(map_item)
    farm.set_item(apple)
    sanctuary.set_item(tpcard)
    ncp.set_item(fruit)
    forest.set_item(herb)
    mt.set_item(torch)
    casino.set_item(coin)
    grotto.set_item(vine)
    island.set_item(fishing_rod)


    # Restore all enemy health
    mark.health = mark.max_health
    harry.health = harry.max_health
    rivmon.health = rivmon.max_health
    skeleton.health = skeleton.max_health
    thief.health = thief.max_health
    sking.health = sking.max_health

    # Respawn enemies in their caves
    town.set_character(townsman)
    river.set_character(rivmon)
    grave.set_character(skeleton)
    dalley.set_character(thief)
    temple.set_character(mark)
    castle.set_character(harry)
    ocean.set_character(sking)
    trident.current_damage = 5         # ADD
    sking.flags["pgave"] = False       # ADD

    # Reset player abilities
    abilities["weakness_scroll"] = False
    abilities["shield_spell"] = False
    abilities["fortune_card"] = False
    abilities["water_shield"] = False

    # Restock merchants
    zepile.stock.clear()
    zepile.add_item(sword, 120)
    zepile.add_item(potion, 20)
    zepile.add_item(potion, 20)
    zepile.add_item(potion, 20)
    zepile.add_item(potion, 20)

    mage.stock.clear()
    mage.add_item(mega_potion, 80)
    mage.add_item(magic_scroll, 10)
    mage.add_item(weakness_scroll, 50)

    # Reset all character flags
    zac.flags["gave_pineapple"] = False
    zain.flags["gave_oil"] = False
    david.flags["gave_money"] = False
    phop.flags["gave_figurine"] = False
    king.flags["gave_sword"] = False
    king.flags["gave_key"] = False
    sking.flags["pgave"] = False
    townsman.flags["traded"] = False

    print("\n===== NEW GAME =====")
    print(current_cave.get_description())

def replay_game():
    """Asks player if they want to replay, shows menu if yes"""
    while True:
        replay = input("Wanna play again? (yes/no): ").lower()
        if replay == "yes":
            show_main_menu()
            reset_game()
            print("=" * 50)
            print("        HUNT THE WUMPUS")
            print("=" * 50)
            print("Your only goal is to defeat the Wumpus.")
            print("\nStarting Area:", current_cave.get_name())
            print("=" * 50)
            return True
        elif replay == "no":
            print("Thanks for playing!")
            return False
        else:
            print("Please type yes or no.")

# ============ GAME TEXT ============
# These must be defined before show_main_menu() is called
tutorial = """Welcome to my game!! I hope you enjoy, here's a quick guide
Move around! Find characters, items and events which you can use to your advantage!
Whenever you see an item, just take it!
Definitely try find the map first
All enemies seem to have a weakness to a specific item!!
"""

commands = """help: Show commands
up,down,left,right: Move in the given direction
map: Displays map
bag: Shows bag
search: Searches for item in area
take: Takes item from area
examine: Get details on a specific item in inventory
fight: Begin a fight with inhabitant
pat: Pat inhabitant
talk: Talk to inhabitant
quit: Quit game
stats: Display stats
use: Use an item in bag
hint: If you ever feel lost!
"""

# ============ GAME STATE ============
# All game variables set up before the menu is shown
current_cave = cavern
bag = []
dead = False
has_map = False
player_hp = 100
player_max_hp = 100
player_money = 0
abilities = {
    "weakness_scroll": False,
    "shield_spell": False,
    "fortune_card": False,
    "water_shield": False
}
# Set character flags
zac.flags["gave_pineapple"] = False
zain.flags["gave_oil"] = False
david.flags["gave_money"] = False
phop.flags["gave_figurine"] = False
king.flags["gave_sword"] = False
king.flags["gave_key"] = False
sking.flags["pgave"] = False
townsman.flags["traded"] = False

# ============ START GAME ============
# Show menu first, then start the game when player picks Level 2
show_main_menu()
print("=" * 50)
print("        HUNT THE WUMPUS")
print("=" * 50)
print("Your only goal is to defeat the Wumpus.")
print("Type 'help' for available commands, Type 'tutorial' for quick guide")
print("\nStarting Area:", current_cave.get_name())
print("=" * 50)

# ============ GAME LOOP ============
while dead == False:
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()
    has_key = any(i.get_name() == "Castle Key" for i in bag)

    command = input('> ').strip().lower()

    # Dev commands for testing
    if command.startswith("dev-"):
        parts = command.split(maxsplit=1)
        dev = parts[0]
        if dev == "dev-money":
            if len(parts) < 2 or not parts[1].isdigit():
                print("Usage: dev-money <amount>")
            else:
                player_money = int(parts[1])
                print(f"Money set to ${player_money}")
        elif dev == "dev-item":
            if len(parts) < 2:
                print("Usage: dev-item <item>")
            else:
                name = parts[1].lower()
                item_lookup = {
                    "map": map_item,
                    "vegemite": vegemite,
                    "torch": torch,
                    "apple": apple,
                    "sword": sword,
                    "potion": potion,
                    "tpcard": tpcard,
                    "pineapple": pineapple,
                    "castle key": castle_key,
                    "fishingrod": fishing_rod,
                    "coin": coin,
                    "oil": oil,
                    "herb": herb,
                    "vine": vine,
                    "kingsword": kingsword,
                    "trident": trident,
                    "waterscroll": water_scroll,
                    "mega potion": mega_potion,
                    "big potion": mark_potion,
                    "magic scroll": magic_scroll,
                    "weakness scroll": weakness_scroll,
                    "ryoshu_figurine": ryoshu_figurine
                }
                if name in item_lookup:
                    bag.append(item_lookup[name])
                    print(f"Gave yourself {item_lookup[name].get_name()}.")
                    if name == "map":
                        has_map = True
                else:
                    print("Unknown item.")
        elif dev == "dev-tp":
            if len(parts) < 2:
                print("Usage: dev-tp <location>")
            else:
                destination = parts[1].lower()
                found = False
                for cave in all_caves:
                    if cave.get_name().lower() == destination:
                        current_cave = cave
                        current_cave.discovered = True
                        print(f"Teleported to {current_cave.get_name()}.")
                        print(current_cave.get_description())
                        found = True
                        break
                if not found:
                    print("Unknown location.")
        else:
            print("Unknown dev command.")
        continue

    # Movement
    if command in ["up", "right", "down", "left"]:
        old_cave = current_cave
        current_cave = current_cave.move(command)

        if current_cave == ncp:
            if random.randint(1, 4) == 1:
                fall_damage = random.randint(10, 20)
                player_hp -= fall_damage
                print("⚠️ The rocks crack beneath you!!!")
                print(f"You slip and take {fall_damage} damage!")
                if player_hp <= 0:
                    player_hp = 0
                    print("You fell off the cliff...")
                    if replay_game():
                        continue
                    else:
                        dead = True
                        continue
            else:
                print("You carefully navigate the narrow path...")

        if current_cave == castle and not has_key:
            print("The castle gates are locked.")
            print("Try finding a key.... maybe the king has it?")
            current_cave = old_cave
            continue

        if current_cave != old_cave:
            current_cave.discovered = True
            if current_cave.get_name() == "Dungeon":
                if has_map:
                    dungeon.set_description("An eerie breeze gushes down the endless tunnel. You successfully found the map here!")
                else:
                    dungeon.set_description("An eerie breeze gushes down the endless, winding tunnel, making the distant, flickering wall torches sputter in the damp gloom. A forgotten map may be hidden somewhere here...")
            print("\n➡️ You enter", current_cave.get_name())
            print(current_cave.get_description())
            if current_cave.get_item() is not None:
                print("→→You notice a", current_cave.get_item().get_name(), "nearby.")
            if current_cave.get_character() is not None:
                print("Someone is here...")
            inhabitant = current_cave.get_character()
            if inhabitant is not None:
                inhabitant.describe()

    elif command == "help":
        print(commands)

    elif command == "tutorial":
        print(tutorial)

    elif command == "search":
        current_cave.search()

    elif command == "talk":
        if inhabitant is not None:
            result = inhabitant.dialogue()
            if result == "fight":
                if run_battle(inhabitant, bag):
                    current_cave.set_character(None)
                    if inhabitant is harry:
                        print("Congratulations, you survived the adventure!")
                        print("\n" + "=" * 50)
                        print("               HAPPY ENDING")
                        print("=" * 50)
                        print ("GAME BY IAN LEE")
                        print("THANKS FOR PLAYING MY GAME")
                        if replay_game():
                            continue
                        else:
                            dead = True

            elif result == "pgive":
                if inhabitant.flags.get("pgave", False):
                    print("Sea King: I already gave you one")
                else:
                    bag.append(water_scroll)
                    print("Here, have this")
                    print("You received a water scroll!")
                    inhabitant.flags["pgave"] = True

            elif result == "trade_veg":
                if townsman.flags["traded"]:
                    print("Townsman: We already traded!")
                elif find_item("coin") is not None:
                    bag.remove(find_item("coin"))
                    bag.append(vegemite)
                    townsman.flags["traded"] = True
                    print("Townsman: Here, take the vegemite!")
                    print("You traded the coin for vegemite!")
                else:
                    print("Townsman: You don't have a coin")
            elif result == "oil":
                if inhabitant.flags.get("gave_oil", False):
                    print("Zain: I already gave you one!")
                else:
                    bag.append(oil)
                    print("Here you go!")
                    print("You received Oil!")
                    inhabitant.flags["gave_oil"] = True
            elif result == "figure":
                if inhabitant.flags.get("gave_figurine", False):
                    print("Phopiang: I already gave you one greedy person!!")
                else:
                    bag.append(ryoshu_figurine)
                    print("You received a Ryōshū figurine!!")
                    inhabitant.flags["gave_figurine"] = True
            elif result == "trade":
                run_shop(inhabitant)
            elif result == "givekey":
                if inhabitant.flags.get("gave_key", False):
                    print("King Aldric: I have already entrusted you with the key.")
                else:
                    print("King Aldric: For years this key has remained under royal protection.")
                    print("King Aldric: May you succeed where so many heroes have failed.")
                    print("You received the Castle Key!")
                    bag.append(castle_key)
                    inhabitant.flags["gave_key"] = True
            elif result == "gkingsword":
                if inhabitant.flags.get("gave_sword", False):
                    print("King Aldric: I have given you the kingsword, go slay the monster.")
                else:
                    print("King Aldric: Here's my old sword")
                    print("You received the Kingsword!")
                    bag.append(kingsword)
                    inhabitant.flags["gave_sword"] = True
            elif result == "fortune":
                tell_fortune()
            elif result == "farmjob":
                farming_game()
            elif result == "pineapple":
                if inhabitant.flags.get("gave_pineapple", False):
                    print(f"{inhabitant.name}: I already gave you one.")
                else:
                    print(f"{inhabitant.name}: Just this once.")
                    print("You put the pineapple in your bag.")
                    bag.append(pineapple)
                    inhabitant.flags["gave_pineapple"] = True
            elif result == "davidmoney":
                if inhabitant.flags.get("gave_money", False):
                    print(inhabitant.name + ": I already gave you money!!")
                else:
                    player_money += 20
                    print(inhabitant.name + ": Here you go, $20.")
                    inhabitant.flags["gave_money"] = True
            elif result == "gamble_heads":
                play_heads_or_tails()
            elif result == "gamble_dice":
                play_dice()
        else:
            print("There is nobody here to talk to you crazy person!")

    elif command == "fight":
        if inhabitant is None:
            print("There's nothing here to fight! Maybe that rock on the ground?")
        elif isinstance(inhabitant, Enemy):
            if run_battle(inhabitant, bag):
                current_cave.set_character(None)
                if inhabitant is harry:
                    print("Congratulations, you survived the adventure!")
                    print("\n" + "=" * 50)
                    print("               HAPPY ENDING")
                    print("=" * 50)
                    print("GAME BY IAN LEE")
                    print("THANKS FOR PLAYING MY GAME")
                    if replay_game():
                        continue
                    else:
                        dead = True
        else:
            print("You really shouldn't attack " + inhabitant.name + "...")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I dont recommend doing that.....")
            else:
                inhabitant.pat()
        else:
            print("As there is nobody to pat, you gave yourself a pat, good job...")

    elif command == "take":
        if item is not None:
            print("You put the", item.get_name(), "into your bag")
            if item.get_name() == "map":
                has_map = True
                print("🗺️ You found a map!")
                print("The 'map' command has been unlocked.")
            bag.append(item)
            current_cave.set_item(None)
        else:
            print("There is nothing here.")

    elif command == "bag":
        if len(bag) == 0:
            print("Your bag is empty...")
        else:
            bag_names = [bag_item.get_name() for bag_item in bag]
            print("You are carrying: " + ", ".join(bag_names))
            print("Type examine to examine specific items")


    elif command == "stats":
        print("\n===== PLAYER STATS =====")
        if player_hp > player_max_hp:
            print(f"HP: {player_hp}/{player_max_hp} 💚 (Overhealed!)")
        else:
            print(f"HP: {player_hp}/{player_max_hp}")
        print(f"Money: ${player_money}")
        if len(bag) == 0:
            print("Inventory: Empty")
        else:
            print("Inventory:", ", ".join(item.get_name() for item in bag))
        print("=" * 24)

    elif command == "examine":
        examine_item()

    elif command == "use":
        print("Which item?")
        use_name = input("> ").strip().lower()
        target = find_item(use_name)
        if target is None:
            print("You don't have a '" + use_name + "' in your bag.")
        elif not target.usable:
            print("You can't use the " + target.get_name() + " right now.")
        elif target.get_name().lower() == "magic scroll":
            for cave in all_caves:
                cave.discovered = True
            print("✨ The scroll reveals the entire map!")
            bag.remove(target)
        elif target.get_name().lower() == "tpcard":
            teleport_menu()
        elif target.get_name().lower() == "weakness scroll":
            abilities["weakness_scroll"] = True
            print("📜 The scroll burns into your memory...")
            print("You can now identify enemy weaknesses forever.")
            bag.remove(target)
        elif target.healing > 0:
            if target.get_name().lower() == "fruit":
                player_hp += target.healing
                print("You eat the fruit and overheal! You now have " + str(player_hp) + " HP!")
            else:
                healed = min(target.healing, player_max_hp - player_hp)
                player_hp += healed
                print("You use the " + target.get_name() + " and recover " + str(healed) + " HP.")
            bag.remove(target)
        elif callable(target.damage) or (isinstance(target.damage, (int, float)) and target.damage > 0):
            print("There's nothing to fight here. Save it for a battle!")
        else:
            print("Nothing happens.")

    elif command == "quit":
        answer = input("Are you sure you want to quit? (yes)/(no): ").strip().lower()
        if answer == "yes":
            show_main_menu()
            reset_game()
            print("=" * 50)
            print("        HUNT THE WUMPUS")
            print("=" * 50)
            print("Your only goal is to defeat the Wumpus.")
            print("\nStarting Area:", current_cave.get_name())
            print("=" * 50)
        elif answer == "no":
            pass

    elif command == "hint":
        if not has_map:
            print("Maybe grab the map in the dungeon?")
        elif not has_key:
            print("You might want to find a key to enter castle")
        else:
            print("There's nothing left to help you")

    elif command == "map":
        if has_map:
            display_map()
        else:
            print("You don't know the layout of this place yet.")
            print("Find a map first.... check the dungeon.")

    else:
        print("I dont understand {" + command + "} please retry your action")