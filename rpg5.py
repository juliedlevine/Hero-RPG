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
        enemy.receive_damage(self.power)
        if not enemy.alive():
            print "%s receives a bounty of %s coins." % (self.name, enemy.points)
            self.coins += enemy.points
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

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
    def receive_damage(self, points):
        evade_probability = self.evade / float(20 + self.evade)
        if random.random() < evade_probability:
            print "%s evaded the attack!" % self.name
        else:
            self.health -= (points - self.armor)
            print "%s has received %d damage." % (self.name, (points - self.armor))
            if self.health <= 0:
                print "%s is dead." % self.name

    # Override character status to show armor & evade status
    def print_status(self):
        print "%s has %d health, %d armor, %d evade and %d power." % (self.name, self.health, self.armor, self.evade, self.power)

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 2
        self.power = 2
        self.points = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 8
        self.power = 1
        self.points = 7

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
        self.points = 8

    def receive_damage(self, points):
        recuperate = random.random() < 0.2
        if recuperate:
            print "%s has recuperated 2 health points." % self.name
            self.health += 2
        super(Medic, self).receive_damage(points)

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 2
        self.points = 9

    def receive_damage(self, points):
        take_damage = random.random() < 0.1
        if take_damage:
            super(Shadow, self).receive_damage(points)
        else:
            print "Shadow hid from the attack!"

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 5
        self.power = 2
        self.points = 15

    def alive(self):
        return True

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
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
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
    cost = 7
    name = 'super tonic'
    def apply(self, hero):
        hero.health = 10
        print "%s's health has been restored to 10." % (hero.name)

class Armor(object):
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's armor has increased to %s." % (hero.name, hero.armor)

class Evade(object):
    cost = 5
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
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
            print "10. leave"
            input = int(raw_input("> "))
            try:
                if Store.items[input - 1].cost > hero.coins:
                    print "Sorry you don't have enough coins to purchase %s." % Store.items[input - 1].name
                    continue
                elif input == 10:
                    break
                else:
                    ItemToBuy = Store.items[input - 1]
                    item = ItemToBuy()
                    hero.buy(item)
            except IndexError:
                print "Sorry that's not a valid choice."

hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
