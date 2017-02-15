"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s." % (self.name, enemy.name)
        # Self is attacker here, will become enemy in recieve damage method
        enemy.receive_damage(self)
        if not enemy.alive():
            print "%s receives a bounty of %s coins for defeating the %s." % (self.name, enemy.bounty, enemy.name)
            hero.coins += enemy.bounty
        # time.sleep(1.5)

    # enemy is character that attacked from line 22 (ex. if the hero was attacking, the hero is the enemy here)
    def receive_damage(self, enemy):
        self.health -= enemy.power
        print "%s received %d damage." % (self.name, enemy.power)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.coins = 20
        self.health = 10
        self.power = 5
        self.armor = 0
        self.evade = 0
        self.swap = False
        self.bounty = 100
        self.arsenal = []

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        # time.sleep(1)

    def add_to_bag(self, item):
        self.coins -= item.cost
        print "%s added to %s's arsenal." % (item.name, self.name)
        self.arsenal.append(item)

    def show_arsenal(self):
        print "%s's arsenal contents:" % self.name
        for i in range(len(self.arsenal)):
            print "%d. %s" % ((i + 1), self.arsenal[i].name)

    # Override Character attack method
    def attack(self, enemy):
        double_damage = random.random() < 0.2
        if double_damage:
            print "%s has double power." % (self.name)
            self.power = (self.power * 2)
        super(Hero, self).attack(enemy)
        if double_damage:
            self.power = (self.power / 2)

    # Override Character attack by adding armor
    def receive_damage(self, enemy):
        evade_probability = self.evade / float(20 + self.evade)
        if random.random() < evade_probability:
            print "%s evaded the attack!" % self.name
        else:
            self.health -= (enemy.power - self.armor)
            print "%s has received %d damage." % (self.name, (enemy.power - self.armor))
            if self.health <= 0:
                print "%s is dead." % self.name

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 8
        self.power = 1
        self.bounty = 7

    # Override Character attack method
    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack." % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = "Medic"
        self.health = 10
        self.power = 1
        self.bounty = 8

    def receive_damage(self, enemy):
        recuperate = random.random() < 0.2
        if recuperate:
            print "%s has recuperated 2 health points." % self.name
            self.health += 2
        super(Medic, self).receive_damage(enemy)

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 2
        self.bounty = 9

    def receive_damage(self, enemy):
        take_damage = random.random() < 0.1
        if take_damage:
            super(Shadow, self).receive_damage(enemy)
        else:
            print "Shadow hid from the attack!"

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 5
        self.power = 2
        self.bounty = 15

    def alive(self):
        return True

    def receive_damage(self, enemy):
        self.health -= enemy.power
        print "%s received %d damage." % (self.name, enemy.power)
        if self.health <= 0:
            print "%s cannot die." % self.name

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            # time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. Fight %s" % enemy.name
            print "2. Do nothing"
            print "3. Flee"
            print "4. Use item from arsenal"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)

            elif input == 4:
                if len(hero.arsenal) == 0:
                    print "Arsenal empty."
                    continue
                print "Which item do you want to use? Enter number."
                hero.show_arsenal()
                if len(hero.arsenal) == 0:
                    print "Sorry arsenal is empty."
                choice = int(raw_input("> "))
                hero.arsenal[choice - 1].apply(hero)
                continue
            else:
                print "Invalid input %r" % input
                continue

            enemy.attack(hero)
        if hero.alive():
            print "Congrats - you defeated the %s!" % enemy.name
            return True
        else:
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, hero):
        hero.health += 2
        hero.arsenal.remove(self)
        print "%s's health increased to %d." % (hero.name, hero.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        hero.arsenal.remove(self)
        print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
    cost = 7
    name = 'super tonic'
    def apply(self, hero):
        hero.health = 10
        hero.arsenal.remove(self)
        print "%s's health has been restored to 10." % (hero.name)

class Armor(object):
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        hero.arsenal.remove(self)
        print "%s's armor has been increased to %s" % (hero.name, hero.armor)

class Evade(object):
    cost = 5
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        hero.arsenal.remove(self)
        print "%s's evade has increased to %s." % (hero.name, hero.evade)


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "9. show arsenal"
            print "10. leave"
            try:
                input = int(raw_input("> "))
                if input == 10:
                    break
                if input == 9:
                    hero.show_arsenal()
                elif Store.items[input - 1].cost > hero.coins:
                    print "Sorry you don't have enough coins to purchase %s." % Store.items[input - 1].name
                    continue
                else:
                    ItemToBuy = Store.items[input - 1]
                    item = ItemToBuy()
                    hero.add_to_bag(item)
            except IndexError or ValueError:
                print "Sorry that's not a valid choice."
            except ValueError:
                print "Sorry that's not a valid choice."

hero = Hero()
enemies = [Medic(), Shadow(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
