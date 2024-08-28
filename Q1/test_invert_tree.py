import unittest
from invert_tree import TreeNode, invertTree, insert_level_order, print_level_order

class TestInvertTree(unittest.TestCase):

    def test_example1(self):
        root = None
        arr = [5, 3, 8, 1, 7, 2, 6]
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = [5, 8, 3, 6, 2, 7, 1]
        self.assertEqual(print_level_order(inverted_root), expected_output)

    def test_example2(self):
        root = None
        arr = [6, 8, 9]
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = [6, 9, 8]
        self.assertEqual(print_level_order(inverted_root), expected_output)

    def test_example3(self):
        root = None
        arr = [5, 3, 8, 1, 7, 2, 6, 100, 3, -1]
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = [5, 8, 3, 6, 2, 7, 1, None, None, None, None, None, -1, 3, 100]
        self.assertEqual(print_level_order(inverted_root), expected_output)

    def test_empty_tree(self):
        root = None
        arr = []
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = []
        self.assertEqual(print_level_order(inverted_root), expected_output)
        
    def test_single_node(self):
        root = None
        arr = [10]
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = [10]
        self.assertEqual(print_level_order(inverted_root), expected_output)

    def test_complete_binary_tree(self):
        root = None
        arr = [4, 2, 7, 1, 3, 6, 9]
        root = insert_level_order(arr, root, 0, len(arr))
        inverted_root = invertTree(root)
        expected_output = [4, 7, 2, 9, 6, 3, 1]
        self.assertEqual(print_level_order(inverted_root), expected_output)

if __name__ == '__main__':
    unittest.main()
