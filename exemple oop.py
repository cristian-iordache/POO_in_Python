class Automobil():
    def __init__(self, marca, model, putere, caroserie, culoare, pret, areDiscount, stock=[]):
        self.marca = marca
        self.model = model
        self.putere = putere
        self.caroserie = caroserie
        self.culoare = culoare
        self.pret = pret
        self.areDiscount = areDiscount
        self.stock = stock

    def discount(self):
        if self.areDiscount:
            pret = self.pret - self.pret*0.19
            return pret

    def inStock(self, id, stock):
        if id in stock:
            print(f'Modelul {id.marca} {id.model} este disponibil.')
            print('-'*10)
        else:
            print(f'Modelul {id.marca} {id.model} nu este disponibil. Este nevoie de o comanda.')
            print('-' * 10)

    def modele_disponibile(self):
        for i in self.stock:
            print(i.marca, i.model, i.putere, i.caroserie)
            # print('-' * 10)

    def rm_model(self, mod):
        if mod in self.stock:
            self.stock.remove(mod)
            print(f'Modelul {mod.marca} {mod.model} a fost scos cu succes din stock.')
            print('-' * 10)

# ------------------------------------------------------------------------------------------------------------


car1 = Automobil('Mercedes-Benz', 'E Class', 240, 'Coupe', 'Matte Black', 89000, True)
car2 = Automobil('Mercedes-Benz', 'C Class', 220, 'Coupe', 'Matte Black', 79000, True)
car3 = Automobil('Mercedes-Benz', 'S Class', 320, 'Coupe', 'Matte Gold', 139000, True)
car4 = Automobil('Mercedes-Benz', 'V Class', 240, 'Coupe', 'Matte Black', 109000, True)
car5 = Automobil('Mercedes-Benz', 'E Class', 340, 'Coupe', 'Matte Black', 89000, True)

# print(car1.marca)
# print(car1.discount())

stock=[car1, car2, car3, car4, car5]
# print(stock)

model=Automobil('Mercedes-Benz', 'E-Class', 000, 'Caro', 'Color', 000000, True, stock)
# print(model1.inStock(car5))
model.rm_model(car2)
model.inStock(car3, stock)

model.modele_disponibile()