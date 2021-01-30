import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cs):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Raj', 'Kapoor', 60000)
        self.emp_2 = Employee('Rajan', 'Kapoor', 90000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Raj.Kapoor@gmail.com')
        self.assertEqual(self.emp_2.email, 'Rajan.Kapoor@gmail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Kapoor@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Kapoor@gmail.com')


    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Raj Kapoor')
        self.assertEqual(self.emp_2.fullname, 'Rajan Kapoor')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Kapoor')
        self.assertEqual(self.emp_2.fullname, 'Jane Kapoor')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 63000)
        self.assertEqual(self.emp_2.pay, 94500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Kapoor/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Kapoor/June')
            self.assertEqual(schedule, 'Bad Response')

if __name__== '__main__':
    unittest.main()