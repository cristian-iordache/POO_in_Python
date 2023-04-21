#Clase in Python

class Robot:
    # constructor (functia __init__)- definim atribute sau proprietati pt toate obj sau instantele pe care le vom crea
    def __init__(self, nume, serialNumber, hardware, software, sleep):
        self.nume = nume
        self.serialNumber = serialNumber
        self.hardware = hardware
        self.software = software
        # sleep este o variabila
        self.sleep = sleep
    # metoda - functie a clasei - vedem daca robotul este sau nu alimentat
    def turnOn(self):
        if self.sleep == False:
            return f'{self.nume} is already running'
        else:
            self.sleep = False
            return f'{self.nume} turned on'

#r1 - instanta a clasei Robot
r1 = Robot('John', '12333', 'i5', 'Python', True)
print(r1.serialNumber)
print(r1.sleep)
print(r1.turnOn())
# print(Robot.turnOn(r1))
print(r1.sleep)

