import unittest

from assignment1 import karatsuba
from assignment2 import count_inversion
from assignment3 import count_comparisions_quick_sort, PivotPartitionStyles
from assignment4 import min_cut


class Test(unittest.TestCase):
    @unittest.skip("Comment this to run")
    def test_assignment1(self):
        """
        Fast algorithm Karatsuba for multiply 2 big numbers
        """
        expected = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
        with open("./numbers.txt", "r") as f:
            num1, num2 = map(int, f.readline().split())

        actual = karatsuba(num1, num2)
        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment2(self):
        """
        Count how many inversion in array.

        Inversions: A pair (A[i], A[j]) is said to be in inversion if:

           A[i] > A[j]

           i < j
        """
        expected = 2407905288
        with open("./IntegerArray.txt", "r") as f:
            numbers = list(map(int, f.readlines()))
        actual = count_inversion(numbers, [None] * len(numbers), 0, len(numbers) - 1)

        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment3_median_of_three(self):
        """
        Count how many comparisions during quick sort if using median of three for pivot partition
        """
        expected = 138382
        with open("./QuickSort.txt", "r") as f:
            numbers = list(map(int, f.readlines()))
        actual = count_comparisions_quick_sort(numbers, 0, len(numbers) - 1)

        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment3_first_element(self):
        """
        Count how many comparisions during quick sort if using first element for pivot partition
        """
        expected = 162085
        with open("./QuickSort.txt", "r") as f:
            numbers = list(map(int, f.readlines()))
        actual = count_comparisions_quick_sort(
            numbers, 0, len(numbers) - 1, PivotPartitionStyles.first_element
        )

        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment3_last_element(self):
        """
        Count how many comparisions during quick sort if using last element for pivot partition
        """
        expected = 164123
        with open("./QuickSort.txt", "r") as f:
            numbers = list(map(int, f.readlines()))
        actual = count_comparisions_quick_sort(
            numbers, 0, len(numbers) - 1, PivotPartitionStyles.last_element
        )
        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment4_1(self):
        """
        Karger min cut for given graph (KargerMinCut1.txt)
        """
        expected = 2
        graph = {}
        with open("./kargerMinCut1.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                temp = list(map(int, line.split()))
                graph[temp[0]] = temp[1:]
        actual = min_cut(graph)
        self.assertEqual(actual, expected)

    @unittest.skip("Comment this to run")
    def test_assignment4_2(self):
        """
        Karger min cut for given graph (KargerMinCut2.txt)
        """
        expected = 2
        graph = {}
        with open("./kargerMinCut2.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                temp = list(map(int, line.split()))
                graph[temp[0]] = temp[1:]
        actual = min_cut(graph)
        self.assertEqual(actual, expected)

    # @unittest.skip("Comment this to run")
    def test_assignment4_3(self):
        """
        Karger min cut for given graph (KargerMinCut.txt)
        """
        expected = 17
        graph = {}
        with open("./kargerMinCut.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                temp = list(map(int, line.split()))
                graph[temp[0]] = temp[1:]
        actual = min_cut(graph)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
