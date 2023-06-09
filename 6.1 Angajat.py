class Angajat:
    perioadaMunca = 10
    def __init__(self, nume, sex, varsta, vechime, task):
        self.nume = nume
        self.sex = sex
        self.varsta = varsta
        self.vechime = vechime
        self.task = task

    def haveTask(self):
        if self.task == True:
            return f'{self.nume} are deja un task'
        else:
            self.task = False
            return f'Trebuie sa i se atribuie lui {self.nume} un task'

    def statusAngajare(self):
        if self.vechime == self.perioadaMunca:
            return f'{self.nume} are deja {self.vechime} ani vechime. Inceteaza contractul determinat'
        elif self.vechime < self.perioadaMunca:
            return f'{self.nume} mai are {self.perioadaMunca - self.vechime} ani de munca'
        elif self.vechime > self.perioadaMunca:
            return f'{self.nume} nu mai este angajat'

    @classmethod
    def fromList(cls, lst):
        nume, sex, varsta, vechime, task = lst
        return cls(nume, sex, varsta, vechime, task )

    def __add__(self, other):
        return self.vechime + other.vechime

    # daca adaugam property, putem folosi metoda ca un atribut
    @property
    def nume_vechime(self):
        return self.nume + ' -> ' + self.vechime

    # numele metodei trebuie sa fie la fel ca cel al setter-ului
    @nume_vechime.setter
    def nume_vechime(self, nv):
        nume, vech = nv.split(' ')
        self.nume = nume
        self.vechime = vech

    @nume_vechime.deleter
    def nume_vechime(self):
        print("Delete")
        self.nume = None
        self.vechime = None

ang1 = Angajat('Marian', 'M', '45', '10', True)
ang2 = Angajat('Victor', 'M', '35', '15', False)
ang3 = Angajat('Andreea', 'F', '25', '5', True)

# print(ang1.statusAngajare())
# print(ang2.statusAngajare())
# print(ang3.statusAngajare())

angAtt = ('Miguel', 'M', 26, 2, True)
ang4 = Angajat.fromList(angAtt)
# print(ang4.nume)

class SubAngajat(Angajat):
    def __init__(self, nume, sex, varsta, vechime, task, zileConcediu):
        super().__init__(nume, sex, varsta, vechime, task)
        self.zileConcediu = zileConcediu

class Manager(Angajat):
    def __init__(self, nume, sex, varsta, vechime, task, angajati=[]):
        super().__init__(nume, sex, varsta, vechime, task)
        self.angajati = angajati

    def addAngajat(self, ang):
        if ang not in self.angajati:
            self.angajati.append(ang)

    def rmAngajat(self, ang):
        if ang in self.angajati:
            self.angajati.remove(ang)

    def printAngajat(self):
        for angajat in self.angajati:
            print(angajat.nume)
        print("-" * 10)

main1 = Manager('Admin', 'ADM', 45, 25, True, [ang1])
main1.addAngajat(ang2)
main1.printAngajat()


print(ang1.nume_vechime)
ang1.nume = 'Vlad'
print(ang1.nume_vechime)
ang1.nume_vechime = 'Virgil 30'
print(ang1.nume_vechime)
print(ang1.nume)
print(ang1.vechime)
del ang1.nume_vechime
print(ang1.nume)

