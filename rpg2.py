# Character class
class Character(object):
    def alive(self):
        if self.health <= 0:
            print "%s is dead." % self
            return False
        else:
            return True

    def attack(self, attackee):
        attackee.health -= self.power
        print "ATTACK!!"
        print "%s does %s damage to %s." % (self, self.power, attackee)

    def print_status(self):
        print "%s: %d health and %d power." % (self, self.health, self.power)


# Hero instance of Character
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5

    def __repr__(self):
        return 'The Hero'


# Zombie instance of Character
class Zombie(Character):
    def __init__(self):
        self.health = 6
        self.power = 2

    def __repr__(self):
        return 'The Zombie'

    # Override inherited alive method, always return True and always have health of 6. Zombie cannot die.
    def alive(self):
        self.health = 6
        return True

# Goblin instance of Character
class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2

    def __repr__(self):
        return 'The Goblin'

# Game function
def main(hero, enemy):
    print "%s vs %s" % (hero, enemy)
    while enemy.alive() and hero.alive():
        print """
Current status:"""
        hero.print_status()
        enemy.print_status()
        print """
You're %s, what do you want to do?
1. Fight %s
2. Do nothing
3. Flee""" % (hero, enemy)
        input = raw_input("> ")
        if input == "1":
            hero.attack(enemy)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input
        if enemy.health > 0:
            enemy.attack(hero)

goblin = Goblin()
zombie = Zombie()
hero = Hero()

main(hero, zombie)
