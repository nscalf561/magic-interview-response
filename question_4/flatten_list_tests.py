import unittest
from flatten_deeply_nested_lists import flatten_lists

class TestFlattenMethods(unittest.TestCase):

    def test_already_flat_list(self):
        test_case = ['flat', 'arr', 'test']
        expected_output = ['flat', 'arr', 'test']
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_shallow_layered_ints(self):
        test_case = [1, 2, [3]]
        expected_output = [1, 2, 3]
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_nested_mixed_content(self):
        test_case = ['a', [2, ['words']]]
        expected_output = ['a', 2, 'words']
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_deeply_nested_ints(self):
        test_case = [[4], [5], [6,[7, [8]]], 9]
        expected_output = [4, 5, 6, 7, 8, 9]
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_empty_list(self):
        test_case = []
        expected_output = []
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_deeply_nested_variable_content(self):
        test_case = [{'test_dict':True}, [1, [False, [8]], 'Will this work?']]
        expected_output = [{'test_dict': True}, 1, False, 8, 'Will this work?']
        self.assertEqual(expected_output, flatten_lists(test_case))

    def test_improper_type(self):
        test_case = {}
        with self.assertRaises(TypeError):
            flatten_lists(test_case)
