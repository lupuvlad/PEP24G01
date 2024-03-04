class Shop:
    stoc = {}
    user_input = None
    status = None
    menu = '''   
Meniu:
       1. Vizualizare stoc
       2. Adaugare produs
       3. Stergere produs
       4. Reducere
       5. Iesire
'''

    # def modif_stoc(self):
    #     print('''
    #     Meniu:
    #            1. Vizualizare stoc
    #            2. Adaugare produs
    #            3. Stergere produs
    #            4. Iesire
    #     ''')
    #     self.user_input = input(f'Alege optiune:\n')
    #     if self.user_input == '2':
    #         produs, pret, stoc = input('give product, price, stoc').split(',')
    #         self.adauga_prod(produs, pret, stoc)

    def adauga_prod(self):
        produs, pret, stoc = input('give product, price, stoc: ').split(',')
        pret = int(pret)
        stoc = int(stoc)
        self.stoc.update({produs: (pret, stoc)})

    # def set_status(self, status):
    #     self.status = status

    def show_stock(self):
        print(self.stoc)

    def remove_prod(self):
        product, price, qty = input('give product, price, quantity: ').split(',')
        price = int(price)
        qty = int(qty)
        stock = self.stoc[product][1] - qty
        self.stoc.update({product: (price, stock)})

    def reducere(self):
        product, discount = input('give product, sale discount: ').split(',')
        discount = int(discount)
        new_price = self.stoc[product][0] - ((discount/100) * self.stoc[product][0])
        self.stoc.update({product: (new_price, self.stoc[product][1])})

    def start(self):
        print(self.menu)
        self.user_input = input(f'Alege optiune:\n')
        while self.user_input != '5':
            if self.user_input == '1':
                self.show_stock()
            elif self.user_input == '2':
                self.adauga_prod()
            elif self.user_input == '3':
                self.remove_prod()
            elif self.user_input == '4':
                self.reducere()
            print(self.menu)
            self.user_input = input(f'Alege optiune:\n')


s = Shop()
s.start()
# t = Shop()
# Shop.adauga_prod(s, 'unt', 5, 100)
# s.adauga_prod('unt', 5, 100)
# t.adauga_prod('unt', 6, 100)


# s.modif_stoc()
# print(f'Ai ales: {s.user_input}')
# print(s.stoc)
# print(t.stoc)
# print(s.show_stock())
# print(t.status)
