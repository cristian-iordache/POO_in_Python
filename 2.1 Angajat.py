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

ang1 = Angajat('Marian', 'M', 45, 10, True)
ang2 = Angajat('Victor', 'M', 35, 15, False)
ang3 = Angajat('Andreea', 'F', 25, 5, True)

print(ang1.statusAngajare())
print(ang2.statusAngajare())
print(ang3.statusAngajare())