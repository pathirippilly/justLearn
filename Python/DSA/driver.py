from sortAlgos import selectionSort,bubbleSort
from dataStructs import LinkedList
import unittest
import os

class TestSelectionSort(unittest.TestCase):
    def test_ascending(self):
        output = selectionSort([9, 8, -5, 7, 4, 1, 7, 3, -88],True)
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88],reverse=True))
    def test_descending(self):
        output = selectionSort([9, 8, -5, 7, 4, 1, 7, 3, -88])
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88]))

class TestBubbleSort(unittest.TestCase):
    def test_ascending(self):
        output = bubbleSort([9, 8, -5, 7, 4, 1, 7, 3, -88],True)
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88],reverse=True))
    def test_descending(self):
        output = bubbleSort([9, 8, -5, 7, 4, 1, 7, 3, -88])
        self.assertTrue(output == sorted([9, 8, 7, 7, 4, 3, 1, -5, -88]))

# class TestLinkedList(unittest.TestCase):
#     def test_reverse(self):
#         ll=LinkedList(55,44,77,99,22)
#         reversed(ll)
#         expOut=LinkedList(44)