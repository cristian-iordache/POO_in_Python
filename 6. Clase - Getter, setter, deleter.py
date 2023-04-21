
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
        # self.identify = nume + '->' + serialNumber
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

    def __repr__(self):
        return f"Robot('{self.nume}', '{self.serialNumber}', '{self.hardware}', '{self.software}', {self.sleep}, {self.age})"

    def __str__(self):
        return self.nume

    def __add__(self, other):
        return self.garantie + other.garantie

    #GETTER
    @property
    def identify(self):
        return self.nume + '->' + self.serialNumber

    #SETTER
    @identify.setter
    def identify(self, ident):
        nume, serial = ident.split(' ')
        self.nume = nume
        self.serialNumber = serial

    #DELETER
    @identify.deleter
    def identify(self):
        print('Delete name and serial number')
        self.nume = None
        self.serialNumber = None


#cream o clasa ce o va mosteni pe Robot
class Aspirator(Robot):
    garantie = 15
    def __init__(self,nume, serialNumber, hardware, software, sleep, age, power):
        super().__init__(nume, serialNumber, hardware, software, sleep, age)
        self.power = power
        # Robot.__init__(self, nume, serialNumber, hardware, software, sleep, age) - e la fel ca la varianta cu super

r1 = Robot('John', '12333', 'i5', 'Python', True, 11)
r2 = Robot('Mark', '22333', 'i5', 'C++', True, 3)
a1 = Aspirator('Jean', '42333', 'i5', 'Python', True, 11, '1kw')

#decorator property - ne ajuta sa definim o metoda pe o puteam accesa ca pe un atribut
print(r1.identify)
r1.nume = 'Johnny'
print(r1.identify)
r1.identify = 'Marcus 123321'
print(r1.nume)
print(r1.serialNumber)
del r1.identify
print(r1.nume)
print(r1.serialNumber)