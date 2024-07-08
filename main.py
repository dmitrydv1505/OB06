import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero("Player")
        self.computer = Hero("Computer")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Player health: {self.player.health}")
            print(f"Computer health: {self.computer.health}")
            print("======== Player's turn =======")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print("Player wins!")
                break
            print("======== Computer's turn =======")
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print("Computer wins!")
                break

if __name__ == "__main__":
    game = Game()
    game.start()
