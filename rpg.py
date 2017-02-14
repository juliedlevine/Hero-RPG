# Character class
class Character(object):

    def alive(self):
        if self.health <= 0:
            print "%s is dead." % self
            return False
        else:
            return True

    def print_status(self):
        print "%s has %d health and %d power." % (self, self.health, self.power)

    def attack(self, attackee):
        attackee.health -= self.power
        print "%s does %s damage to %s" % (self, self.power, attackee)


# Hero instance of Character
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5

    def __repr__(self):
        return 'The Hero (you)'


# Goblin instance of Character
class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2

    def __repr__(self):
        return 'The goblin'


# Game function- Hero vs. Goblin
def main():
    hero = Hero()
    goblin = Goblin()

    while zombie.alive() and hero.alive():
        print """
Current status:"""
        hero.print_status()
        goblin.print_status()
        print """
You're the Hero, what do you want to do?
1. Fight Zombie
2. Do nothing
3. Flee"""
        input = raw_input(">")
        if input == "1":
            hero.attack(goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input
        if goblin.health > 0:
            goblin.attack(hero)

main()
