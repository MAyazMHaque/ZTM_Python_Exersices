class User():
    def sign_in(self):
        return ("Logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.name} has arrows left is {self.arrows}')

# creating another class with multiple inheritances


class HybridClass(Wizard, Archer):
    def __int__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridClass('Pappu', 100, 80)
