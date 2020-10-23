from PythonApplication1 import *
import unittest

class Test_test1(unittest.TestCase):

    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.left.left.right = Node(8); 
    root.left.left.left = Node(9); 
    root.left.right.right = Node(10);
    root.left.right.left = Node(11);
    root.right.left.right = Node(12);
    root.right.left.left = Node(13);
    root.right.right.right = Node(14);
    root.right.right.left = Node(15);

    def test_A(self):
        self.fail("Not implemented")
        self.assertAlmostEqual(findLCA(root, 10, 15), 1)
        self.assertAlmostEqual(findLCA(root, 8, 11), 2)
        self.assertAlmostEqual(findLCA(root, 3, 8), 3)
        self.assertAlmostEqual(findLCA(root, 12, 14), 1)

    def test_NULL(self):
        self.fail("Not implemented")
        self.assertAlmostEqual(findLCA(root, 10, 15), 1)
        self.assertAlmostEqual(findLCA(root, 10, 16), 2)

    def testSame(self):
        self.fail("Not implemented")
        self.assertAlmostEqual(findLCA(root, 10, 10), 10)

    def testRoot(self):
        self.fail("Not implemented")
        self.assertAlmostEqual(findLCA(root, root, root), 1)

if __name__ == '__main__':
    unittest.main()
