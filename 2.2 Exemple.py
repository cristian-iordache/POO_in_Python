#Clase in Python

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

print(Robot.noRobots)

r1 = Robot('John', '12333', 'i5', 'Python', True, 11)
r2 = Robot('Mark', '22333', 'i5', 'C++', True, 3)

print(Robot.noRobots)
print(r1.endOfLife())
print(r2.endOfLife())
# print(Robot.garantie)
# print(r1.garantie)
# print(r1.prenume)
# print('r1 namespace before', r1.__dict__)
# r1.garantie = "3 ani"
# r1.prenume = "Marean"
# print(r1.garantie)
# #namespace-ul clasei si a instantei __dict__
# print(Robot.__dict__)
# print('r1 namespace after',r1.__dict__)