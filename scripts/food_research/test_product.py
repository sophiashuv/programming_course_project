import unittest
from product import Product
from database_search import *


class ProductTest(unittest.TestCase):
    def setUp(self):
        baguet = found_in_database('ru_database.json', 'багет')
        self.product1 = Product(baguet['Номер'], baguet['Продукт'], baguet['ккал'].replace(',', '.'),
                                baguet['білок'].replace(',', '.'), baguet['жири'].replace(',', '.'),
                                baguet['вуглеводи'].replace(',', '.'),
                                baguet['холестерин'].replace(',', '.'),
                                baguet['1 ХO є в граммах продукта (Старыи розрах)'].replace(',', '.'),
                                baguet['1 ХO є в граммах продукта (новий розрах)'].replace(',', '.'))

        keks = found_in_database('ru_database.json', 'Кекс')
        self.product2 = Product(keks['Номер'], keks['Продукт'], keks['ккал'].replace(',', '.'),
                                keks['білок'].replace(',', '.'), keks['жири'].replace(',', '.'),
                                keks['вуглеводи'].replace(',', '.'),
                                keks['холестерин'].replace(',', '.'),
                                keks['1 ХO є в граммах продукта (Старыи розрах)'].replace(',', '.'),
                                keks['1 ХO є в граммах продукта (новий розрах)'].replace(',', '.'))

    def test_get_number(self):
        self.assertEqual(self.product1.get_number(), 2)
        self.assertEqual(self.product2.get_number(), 6)

    def test_get_name(self):
        self.assertEqual(self.product1.get_name(), 'Багет/булочки')
        self.assertEqual(self.product2.get_name(), 'Кекс')

    def test_get_protein(self):
        self.assertEqual(self.product1.get_protein(), 7.81)
        self.assertEqual(self.product2.get_protein(), 6.76)

    def test_get_ccal(self):
        self.assertEqual(self.product1.get_ccal(), 252.0)
        self.assertEqual(self.product2.get_ccal(), 353)

    def test_get_fats(self):
        self.assertEqual(self.product1.get_fats(), 1.41)
        self.assertEqual(self.product2.get_fats(), 16.9)

    def test_get_carbohydrates(self):
        self.assertEqual(self.product1.get_carbohydrates(), 51.0)
        self.assertEqual(self.product2.get_carbohydrates(), 43.0)

    def test_get_cholesterol(self):
        self.assertEqual(self.product1.get_cholesterol(), 0.0)
        self.assertEqual(self.product2.get_cholesterol(), 46.0)

    def test_get_old_bi(self):
        self.assertEqual(self.product1.get_old_bi(), 19.61)
        self.assertEqual(self.product2.get_old_bi(), 23.26)

    def test_get_new_bi(self):
        self.assertEqual(self.product1.get_new_bi(), 39.68)
        self.assertEqual(self.product2.get_new_bi(), 28.33)

    def test_get_count_value(self):
        self.assertEqual(self.product1.count_value('ccal', 200), 504.0)
        self.assertEqual(self.product2.count_value('ccal', 200), 706.0)
        self.assertEqual(self.product1.count_value('fats', 200), 2.82)
        self.assertEqual(self.product2.count_value('fats', 200), 33.8)
        self.assertEqual(self.product1.count_value('protein', 200), 15.620000000000001)
        self.assertEqual(self.product2.count_value('protein', 200), 13.52)
        self.assertEqual(self.product1.count_value('carbohydrates', 200), 102.0)
        self.assertEqual(self.product2.count_value('carbohydrates', 200), 86.0)
        self.assertEqual(self.product1.count_value('cholesterol', 200), 0.0)
        self.assertEqual(self.product2.count_value('cholesterol', 200), 92.0)
        self.assertEqual(self.product1.count_value('bread items', 200), 5.0)
        self.assertEqual(self.product2.count_value('bread items', 200), 7.0)

    def test_str(self):
        self.assertEqual(str(self.product1), 'Product number : 2\nProduct name : Багет/булочки\nProduct calories :'
                                             ' 252.0\nProduct proteins : 7.81\nProduct fats : 1.41\nProduct '
                                             'carbohydrates : 51.0\nProduct cholesterol : 0.0\nProduct in 1  '
                                             'bread item '': 39.68')

        self.assertEqual(str(self.product2), 'Product number : 6\n'
                                             'Product name : Кекс\n'
                                             'Product calories : 353.0\n'
                                             'Product proteins : 6.76\n'
                                             'Product fats : 16.9\n'
                                             'Product carbohydrates : 43.0\n'
                                             'Product cholesterol : 46.0\n'
                                             'Product in 1  bread item : 28.33')


if __name__ == '__main__':
    unittest.main()
