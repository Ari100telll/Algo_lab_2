import unittest
from BagsTracker import get_min_size_of_square


class BagsTracker(unittest.TestCase):
    def test_bags_tracker(self):
        self.assertEqual(get_min_size_of_square(10, 2, 3), 9)
        self.assertEqual(get_min_size_of_square(10, 1, 10), 10)
        self.assertEqual(get_min_size_of_square(10, 10, 1), 10)
        self.assertEqual(get_min_size_of_square(1, 1, 100), 100)
        self.assertEqual(get_min_size_of_square(1, 100, 1), 100)
        self.assertEqual(get_min_size_of_square(2, 100000000, 99999999), 199999998)


if __name__ == '__main__':
    unittest.main()
