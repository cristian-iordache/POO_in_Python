
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

#cream o clasa ce o va mosteni pe Robot
class Aspirator(Robot):
    garantie = 15
    def __init__(self,nume, serialNumber, hardware, software, sleep, age, power):
        super().__init__(nume, serialNumber, hardware, software, sleep, age)
        self.power = power
        # Robot.__init__(self, nume, serialNumber, hardware, software, sleep, age) - e la fel ca la varianta cu super

r1 = Robot('John', '12333', 'i5', 'Python', True, 11)
r2 = Robot('Mark', '22333', 'i5', 'C++', True, 3)
s
a1 = Aspirator('Jean', '42333', 'i5', 'Python', True, 11, '1kw')
# print(a1.nume)
# print(r1.garantie)
print(a1.serialNumber, a1.power)