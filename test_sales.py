import unittest

from sales import average_order_value


class SalesTests(unittest.TestCase):
    def test_average_order_value(self):
        self.assertEqual(average_order_value([10, 20, 30]), 20.0)

    def test_decimal_amounts(self):
        self.assertAlmostEqual(average_order_value([10.5, 20.0]), 15.25)

    def test_empty_orders(self):
        with self.assertRaisesRegex(ValueError, "At least one order"):
            average_order_value([])


if __name__ == "__main__":
    unittest.main()
