import unittest

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_plus(self):
        expected = 3;
        result = add1 + add2;
        self.assertEqual(expected, result);

    def test_minus(self):
        result = self.args[0]-self.args[1];
        self.assertEqual(expected, result);

expected = 1
add1 = 1
add2 = 2
suite = unittest.TestSuite()
suite = (unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)
##suite = (unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase))
