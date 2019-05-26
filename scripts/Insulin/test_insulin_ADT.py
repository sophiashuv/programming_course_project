import unittest
from scripts.Insulin.insulin_ADT import Insulin
from flask_glucu.database_search import *


class InsulinTest(unittest.TestCase):
    def setUp(self):
        ins1 = found_in_database('table_insulin.json', "Lispro (Humalog)")
        self.insulin1 = Insulin(ins1["Type of Insulin & Brand Names"], ins1["Onset"], ins1["Peak"],
                                ins1["Duration"])
        ins2 = found_in_database('table_insulin.json', "Insulin degludec (Tresiba)")
        self.insulin2 = Insulin(ins2["Type of Insulin & Brand Names"], ins2["Onset"], ins2["Peak"],
                                ins2["Duration"])
        ins3 = found_in_database('table_insulin.json', "Velosulin (for use in the insulin pump)")
        self.insulin3 = Insulin(ins3["Type of Insulin & Brand Names"], ins3["Onset"], ins3["Peak"],
                                ins3["Duration"])

    def test_get_names(self):
        self.assertEqual(self.insulin1.get_names(), "Lispro (Humalog)")
        self.assertEqual(self.insulin2.get_names(), "Insulin degludec (Tresiba)")
        self.assertEqual(self.insulin3.get_names(), "Velosulin (for use in the insulin pump)")

    def test_get_onset(self):
        self.assertEqual(self.insulin1.get_onset(), 22.5)
        self.assertEqual(self.insulin2.get_onset(), 60.0)
        self.assertEqual(self.insulin3.get_onset(), 45.0)

    def test_get_peak(self):
        self.assertEqual(self.insulin1.get_peak(), 60.0)
        self.assertEqual(self.insulin2.get_peak(), "No peak time")
        self.assertEqual(self.insulin3.get_peak(), 90.0)

    def test_get_durationk(self):
        self.assertEqual(self.insulin1.get_duration(), (3, 5))
        self.assertEqual(self.insulin2.get_duration(), (0, 42))
        self.assertEqual(self.insulin3.get_duration(), (2, 3))

    def test_insulin_type(self):
        self.assertEqual(self.insulin1.insulin_type(), "Rapid-acting")
        self.assertEqual(self.insulin2.insulin_type(), "Rapid-acting")
        self.assertEqual(self.insulin3.insulin_type(), "Rapid-acting")

    def test_str(self):
        self.assertEqual(str(self.insulin1), "Lispro (Humalog) - інсулін раптової дії. Він покриває потребу в "
                                             "інсуліні під-час прийому їжі . This type of insulin is often used "
                                             "with longer-acting insulin. Для нього характерні наступні властивості. "
                                             "Середнє значення початку дії препарату є 22.5, середнє значення піку "
                                             "дії препарату є 60.0 максимальна тривалість - 5, мінімальна "
                                             "тривалість - 3.")

        self.assertEqual(str(self.insulin2), "Insulin degludec (Tresiba) - інсулін раптової дії. Він покриває потребу "
                                             "в інсуліні під-час прийому їжі . This type of insulin is often used "
                                             "with longer-acting insulin. Для нього характерні наступні властивості. "
                                             "Середнє значення початку дії препарату є 60.0, середнє значення піку "
                                             "дії препарату є No peak time максимальна тривалість - 42, мінімальна "
                                             "тривалість - 0.")

        self.assertEqual(str(self.insulin3), "Velosulin (for use in the insulin pump) - інсулін раптової дії. Він "
                                             "покриває потребу в інсуліні під-час прийому їжі . This type of insulin"
                                             " is often used with longer-acting insulin. Для нього характерні "
                                             "наступні властивості. Середнє значення початку дії препарату є 45.0, "
                                             "середнє значення піку дії препарату є 90.0 максимальна тривалість - 3,"
                                             " мінімальна тривалість - 2.")


if __name__ == "__main__":
    unittest.main()
    print("OK")
