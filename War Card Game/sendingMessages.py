class Player(object):
    __playerCount = 0
    def __init__(self):
        Player.__playerCount += 1
        self.health = 3
        self.attackdmg = 1

    def __show_playerCount__():
        print(Player.__playerCount)

    def die(self):
        if self.health <= 0:
            print("The player has died")

    def update(self):
        self.die()

    def shoot(self, target, damage):
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        self.die()


class Alien(object):
    def __init__(self):
        self.health = 3
        self.attackdmg = 1

    def die(self):
        if self.health <= 0:
            print("The alien has died")

    def take_damage(self, damage):
        self.health -= damage
        self.die()

    def shoot(self, target, damage):
        target.take_damage(damage)


player = Player()
enemy = Alien()

player.shoot(enemy, player.attackdmg)
player.shoot(enemy, player.attackdmg)
player.shoot(enemy, player.attackdmg)