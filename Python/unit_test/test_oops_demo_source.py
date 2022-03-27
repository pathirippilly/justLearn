import unittest
from unittest import mock
from oops_demo_source import Employee, BadResponseException,EtlBaseClass


# unittest.TestLoader.testMethodPrefix='testit'
# unittest.TestLoader.sortTestMethodsUsing = lambda self, a, b:
class TestEmployee(unittest.TestCase):
    # _patcher1=None
    # test_data=None
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_data = {'full_name1': "Akhil Pathirippilly mana ",
                         'full_name2': " Akhil P",
                         'fname1': 'Akhil', 'lname1': 'Pathirippilly mana',
                         'fname2': 'Akhil', 'lname2': 'P',
                         'email1': 'akhil.pathirippillymana@xyzcompany.com',
                         'email2': 'akhil.p@xyzcompany.com', 'month1': 'May',
                         'mock_url1': 'https://xyzcompany.com/Pathirippillymana/May',
                         'mock_ok': True,
                         'mock_not_ok': False,
                         'mock_text1': '88.52',
                         'mock_exptn': BadResponseException
                         }
        cls._patcher1=mock.patch("oops_demo_source.requests.get").start()
        print(type(cls._patcher1))
        print("One time setup for entire test case goes here....")

    @classmethod
    def tearDownClass(cls) -> None:
        print("One time cleanup for entire test case goes here....")
        cls._patcher1.stop()

    def setUp(self) -> None:
        print(f"Test: {self._testMethodName} starts..")
        self.emp1 = Employee(self.test_data['full_name1'])
        if self._testMethodName == 'test_name_change':
            self.emp1.full_name = self.test_data['full_name2']

    def tearDown(self) -> None:
        self.emp1.full_name = self.test_data['full_name1']
        print(f"Test: {self._testMethodName} ends..")

    def test_full_name(self):
        self.assertEqual(self.emp1.full_name, self.test_data['full_name1'].strip())

    def test_fname_name(self):
        self.assertEqual(self.emp1.first, self.test_data['fname1'])

    def test_lname_name(self):
        self.assertEqual(self.emp1.last, self.test_data['lname1'])

    def test_email(self):
        self.assertEqual(self.emp1.email, self.test_data['email1'])

    def test_name_change(self):
        self.assertEqual(self.emp1.first, self.test_data['fname2'])
        self.assertEqual(self.emp1.last, self.test_data['lname2'])
        self.assertEqual(self.emp1.full_name, self.test_data['full_name2'].strip())
        self.assertEqual(self.emp1.email, self.test_data['email2'])
    # @mock.patch("oops_demo_source.requests.get")
    def test_get_monthly_target(self):
        self._patcher1.return_value.ok = self.test_data['mock_ok']
        self._patcher1.return_value.text = self.test_data['mock_text1']
        target = self.emp1.get_monthly_target(self.test_data['month1'])
        self._patcher1.assert_called_with(self.test_data['mock_url1'])
        self.assertEqual(target, self.test_data['mock_text1'])



    def test_get_monthly_target_exception(self):
        with mock.patch("oops_demo_source.requests.get") as mocked_get:
            mocked_get.return_value.ok = self.test_data['mock_not_ok']
            self.assertRaises(self.test_data['mock_exptn'],
                              self.emp1.get_monthly_target,
                              self.test_data['month1'])
            mocked_get.assert_called_with(self.test_data['mock_url1'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployee)
    unittest.TextTestRunner(verbosity=2).run(suite)
