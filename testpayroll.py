import payroll
import unittest

class payrollTest(unittest.TestCase):
    def setUp(self):
        payroll.load_employees()
        self.employees = payroll.employees
    
    def testSearchByID(self):
        self.assertEqual(payroll.search_id(688997)[0].first_name, "Karina")
    
    def testSearchByFirstName(self):
        self.assertEqual(payroll.search_first_name("Karina")[0].first_name, "Karina")
    
    def testSearchByLastName(self):
        self.assertEqual(payroll.search_last_name("Gay")[0].first_name, "Karina")

    def testSearchByFullName(self):
        self.assertEqual(payroll.search_full_name("Rooney Alvar")[0].first_name, "Rooney")

    def testResave(self):
        payroll.update_file()

if __name__ == '__main__':
    unittest.main()