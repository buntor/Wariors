from random import randrange


class Warrior:
    health = 200

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":

    units = [Warrior("Red"), Warrior("Blue")]
    victim_name = ""

    while len(victim_name) == 0:
        agressor = units.copy()
        victim = agressor.pop(randrange(0, 2))
        agressor = agressor[0]

        input(f"{agressor.name} ({agressor.health}) -> "
              f"{victim.name} ({victim.health})...")

        victim.health -= 20

        if victim.health <= 0:
            victim_name = victim.name

    print(f"† {victim_name} умер †")
