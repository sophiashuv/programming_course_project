class Product:
    """ Class for product representation"""
    def __init__(self, number, name, ccal, protein, fats, carbohydrates, cholesterol, old_ho, new_ho):
        self.number = int(number)
        self.name = name
        self.ccal = float(ccal)
        self.protein = float(protein)
        self.fats = float(fats)
        self.carbohydrates = float(carbohydrates)
        self.cholesterol = float(cholesterol)
        self.old_bread_items = float(old_ho)
        self.new_bread_items = float(new_ho)

    def get_number(self):
        """
        Returns number of product in database
        (Product) - > int
        """
        return self.number

    def get_name(self):
        """
        Returns name of product
        (Product) - > str
        """
        return self.name

    def get_protein(self):
        """
        Returns value of protein in product
        (Product) - > float
        """
        return self.protein

    def get_ccal(self):
        """
        Returns value of ccal in product
        (Product) - > float
        """
        return self.ccal

    def get_fats(self):
        """
        Returns value of fats in product
        (Product) - > float
        """
        return self.fats

    def get_carbohydrates(self):
        """
        Returns value of carbohydrates in product
        (Product) - > float
        """
        return self.carbohydrates

    def get_cholesterol(self):
        """
        Returns value of cholesterol in product
        (Product) - > float
        """
        return self.cholesterol

    def get_old_bi(self):
        """
        Returns grams of product in 1 BI calculated by ols sysytem
        (Product) - > float
        """
        return self.old_bread_items

    def get_new_bi(self):
        """
        Returns grams of product in 1 BI calculated by ols sysytem
        (Product) - > float
        """
        return self.new_bread_items

    def count_value(self, characteristic, weight):
        """
        Returns value of characteristic in given weight of product
        (Product) - > float
        """
        if characteristic == 'ccal':
            gr_value = self.ccal/100
        elif characteristic == 'fats':
            gr_value = self.fats / 100
        elif characteristic == 'protein':
            gr_value = self.protein / 100
        elif characteristic == 'fats':
            gr_value = self.fats / 100
        elif characteristic == 'carbohydrates':
            gr_value = self.carbohydrates / 100
        elif characteristic == 'cholesterol':
            gr_value = self.cholesterol / 100
        elif characteristic == 'bread items':
            gr_value = (weight//self.new_bread_items)
            print('In {} grams of {} value of {} is {} '.format(weight, self.name, characteristic, gr_value))
            return gr_value
        else:
            return 'Did not found this characteristic!'
        value = weight * gr_value
        print('In {} grams of {} value of {} is {} '.format(weight, self.name, characteristic, value))
        return value

    def __str__(self):
        """
        String representation of product
        (Product) -> str
        """
        s = ''
        s += 'Product number : ' + str(self.get_number()) + '\n'
        s += 'Product name : ' + str(self.get_name()) + '\n'
        s += 'Product calories : ' + str(self.get_ccal()) + '\n'
        s += 'Product proteins : ' + str(self.get_protein()) + '\n'
        s += 'Product fats : ' + str(self.fats) + '\n'
        s += 'Product carbohydrates : ' + str(self.get_carbohydrates()) + '\n'
        s += 'Product cholesterol : ' + str(self.get_cholesterol()) + '\n'
        s += 'Product in 1  bread item : ' + str(self.get_new_bi())
        return s





