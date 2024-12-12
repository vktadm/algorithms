import unittest

from sorting.bubblesort import bubblesort


class BubblesortTest(unittest.TestCase):

    def run_sort(self, array):
        standart_sort = bubble_sort = array
        standart_sort.sort()
        bubblesort(bubble_sort)
        self.assertEqual(standart_sort, bubble_sort)

    def test_case_1(self):
        self.run_sort([10, 9, 8])

    def test_case_2(self):
        self.run_sort([10, 8, 9])


if __name__ == "__main__":
    unittest.main()
