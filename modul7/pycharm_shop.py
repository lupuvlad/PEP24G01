from modul7.categorii import Haine, Accesorii, Incaltaminte


class Shop:
    main_menu_options = {1: "Categorii", 2: "Produse", 3: "Iesire"}
    products_menu_options = {1: "Adaugare", 2: "Vizualizare", 3: "Iesire la meniul principal"}
    stoc = []
    product_mapping = {"haine": Haine, "accesorii": Accesorii, "incaltaminte": Incaltaminte}
    user_input_msg = "Alegeti optiunea: "
    product_select_msg = "Introduceti optiunea: "

    @staticmethod
    def get_user_input(msg, menu):
        while True:
            try:
                option = int(input(msg))
                if option in menu:
                    break
            except Exception:
                pass
            print("Optiune invalida.")

        return option

    def print_main_menu(self):
        menu = "Bun venit la magazinul PyCharm: \n"
        options = "\n".join([f"\t{key}. {value}" for key, value in self.main_menu_options.items()])
        print(menu + options + "\n")

    def print_categories(self):
        print("=" * 40)
        print(" CATEGORII ".center(40, "="))
        print("=" * 40)
        print("\n".join(set([f"---\t{cat.__class__.__name__}" for cat in self.stoc])))

    def print_products(self):
        print(" PRODUSE ".center(40, "="))
        print("=" * 40)
        options = "\n".join([f"\t{key}. {value}" for key, value in self.products_menu_options.items()])
        print(options + "\n")

    def add_product(self):
        categorie = input("Introduceti numele categoriei: ").lower()
        produs = input("Introduceti numele produsului: ")
        pret = float(input("Introduceti pretul produsului: "))
        stoc = int(input("Introduceti stocul produsului: "))
        prod_class = self.product_mapping[categorie]  # type: Haine
        product = prod_class(produs, pret, stoc)
        self.stoc.append(product)

    def show_stock(self):
        categories = {}
        for obj in self.stoc:  # type: Haine
            if obj.__class__.__name__ in categories:
                categories[obj.__class__.__name__].append(obj)
            else:
                categories[obj.__class__.__name__] = []
                categories[obj.__class__.__name__].append(obj)

        print(categories)
        for name, obj_list in categories.items():
            print("=" * 30)
            print(f"Categoria {name}")
            print("=" * 30)
            for obj in obj_list:
                print(f"Nume: {obj.nume}")
                print(f"Pret: {obj.pret}")
                print(f"Stoc: {obj.stoc}")
                print("-" * 30)

    # def remove_prod(self):
    #     product, price, qty = input('give product, price, quantity: ').split(',')
    #     price = int(price)
    #     qty = int(qty)
    #     stock = self.stoc[product][1] - qty
    #     self.stoc.update({product: (price, stock)})
    #
    # def reducere(self):
    #     product, discount = input('give product, sale discount: ').split(',')
    #     discount = int(discount)
    #     new_price = self.stoc[product][0] - ((discount/100) * self.stoc[product][0])
    #     self.stoc.update({product: (new_price, self.stoc[product][1])})

    def start(self):
        while True:
            self.print_main_menu()
            option = self.get_user_input(self.user_input_msg, self.main_menu_options)
            if option == 1:
                self.print_categories()
            elif option == 2:
                while True:
                    self.print_products()
                    option2 = self.get_user_input(self.product_select_msg, self.products_menu_options)
                    if option2 == 1:
                        self.add_product()
                    elif option2 == 2:
                        self.show_stock()
                    elif option2 == 3:
                        break
            elif option == 3:
                break


if __name__ == "__main__":
    s = Shop()
    s.stoc.append(Haine(nume="tricouri", pret=100, stoc=200))
    s.stoc.append(Haine(nume="pantaloni", pret=120, stoc=250))
    s.stoc.append(Accesorii(nume="cercei", pret=250, stoc=1000))
    s.stoc.append(Incaltaminte(nume="adidasi", pret=250, stoc=10))
    s.start()
    print(s.stoc)



