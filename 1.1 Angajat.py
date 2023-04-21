#Creare unei instante a unei clase angajat

class Angajat:
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

ang1 = Angajat('Marian', 'M', 35, 5, False)
print(ang1.nume)
print(ang1.haveTask())