#Clase in Python

import math

class Robot:
    #variabila a clasei
    garantie = 10
    noRobots = 0
    def __init__(self, nume, serialNumber, hardware, software, sleep, age):
        self.nume = nume
        self.serialNumber = serialNumber
        self.hardware = hardware
        self.software = software
        self.sleep = sleep
        self.age = age
        Robot.noRobots += 1

    def turnOn(self):
        if self.sleep == False:
            return f'{self.nume} is already running'
        else:
            self.sleep = False
            return f'{self.nume} turned on'

    def endOfLife(self):
        if self.age > self.garantie:
            print(f'{self.nume} is end of life')
        else:
            print(f"{self.nume} has {self.garantie - self.age} years till end of life")

    # metoda clasei - keyword cls va fi inlocuit de numele clasei - primesc ca prin argument clasa si nu instanta
    @classmethod
    def seteazaGarantie(cls, ani):
        cls.garantie = ani

    # metoda alternativa
    @classmethod
    def fromList(cls, lst):
        nume, serialNumber, hardware, software, sleep, age = lst
        return cls(nume, serialNumber, hardware, software, sleep, age)

    # metode statice
    @staticmethod
    def dimensiuniCerc(raza):
        return 2*math.pi*raza, math.pi*raza*raza

r1 = Robot('John', '12333', 'i5', 'Python', True, 11)
r2 = Robot('Mark', '22333', 'i5', 'C++', True, 3)

Robot.seteazaGarantie(7)
# print(Robot.garantie)
# print(r1.garantie)
# print(r2.garantie)

robotAttributes = ('Techie', '33333', 'M1', 'Python', True, 2)
# nume, serialNumber, hardware, software, sleep, age = robotAttributes
# r3 = Robot(nume, serialNumber, hardware, software, sleep, age)

# print(r3.serialNumber)

r4 = Robot.fromList(robotAttributes)
print(r4.nume)

print(Robot.dimensiuniCerc(10))

print(Robot.noRobots)