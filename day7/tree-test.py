import unittest
from tree import File, DirectoryNode

class TestTree(unittest.TestCase):
    def test_empty_dir(self):
        test_tree = DirectoryNode("test_dir_1")
        self.assertEqual(test_tree.name, 'test_dir_1')
        self.assertEqual(test_tree.size(), 0)
        self.assertEqual(test_tree.parent, None)

    def test_dir_with_single_file(self):
        file = File("test_file", 100)
        test_tree = DirectoryNode("test_dir_2")
        test_tree.add_file(file)
        self.assertEqual(test_tree.name, 'test_dir_2')
        self.assertEqual(test_tree.size(), 100)

    def test_dir_with_multiple_files(self):
        file_1 = File("test_file_1", 100)
        file_2 = File("test_file_2", 100)
        file_3 = File("test_file_3", 100)
        test_tree = DirectoryNode("test_dir_3")
        test_tree.add_file(file_1).add_file(file_2).add_file(file_3)
        self.assertEqual(test_tree.name, 'test_dir_3')
        self.assertEqual(test_tree.size(), 300)

    def test_dir_with_multiple_files(self):
        file_1 = File("test_file_1", 100)
        file_2 = File("test_file_2", 100)
        file_3 = File("test_file_3", 100)
        file_4 = File("test_file_4", 100)
        file_5 = File("test_file_5", 100)
        root = DirectoryNode("root")
        child_1 = DirectoryNode("child_1")
        child_2 = DirectoryNode("child_2")
        root.add_file(file_1).add_file(file_2).add_file(file_3)
        child_1.add_file(file_4)
        child_2.add_file(file_5)
        root.add_dir(child_1).add_dir(child_2)
        self.assertEqual(root.name, 'root')
        self.assertEqual(root.size(), 500)
        self.assertEqual(child_2.parent, root)

if __name__ == '__main__':
    unittest.main()
