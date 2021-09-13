from sortAlgos import selectionSort
import unittest

class TestSelectionSort(unittest.TestCase):
    def test_ascending(self):
        output = selectionSort([9, 8, -5, 7, 4, 1, 7, 3, -88],True)
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88],reverse=True))
    def test_descending(self):
        output = selectionSort([9, 8, -5, 7, 4, 1, 7, 3, -88])
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88]))