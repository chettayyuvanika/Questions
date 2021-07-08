# Problem Name is &&& Search Tree &&& PLEASE DO NOT REMOVE THIS LINE. 
# Instructions to candidate.
# 1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
# 2) Implement the "put" and "contains" methods.
# 3) Fix the "inOrderTraversal" method.
# 4) Add additional relevant tests
# 5) If time permits, try to improve your implementation. 
import unittest 

class BST(object):
    def __init__(self):
        
        self.root = Node()
        
    def put(self, value):
        val=Node(value)
        if self.root.value is None:
            self.root=val
        else:
            prev=None
            temp=self.root
            while temp:
                if temp.value>value:
                    prev=temp
                    temp=temp.left
                elif temp.value<value:
                    prev=temp
                    temp=temp.right
            if prev.value>value:
                prev.left=val
            else:
                prev.right=val
                
    def contains(self,value):
        #TODO: implement me
        temp=self.root
        while temp != None:
            if value==temp.value:
                return True
            elif value>temp.value:
                temp=temp.right
            elif value<temp.value:
                temp=temp.left
        return False
        
    def in_order_traversal(self):
        acc = list()
        self._in_order_traversal(self.root, acc)
        return acc
        
    def _in_order_traversal(self, node, acc):
        if node is None or node.value is None:
            return
        self._in_order_traversal(node.left, acc)
        acc.append(node.value)
        self._in_order_traversal(node.right, acc)

class Node(object):
    def __init__(self, value=None, left=None, right=None):
        
        self.value = value
        self.left = left
        self.right = right
        
class TestBST(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.search_tree = BST()

    def test_bst(self):
        self.search_tree.put(3)
        self.search_tree.put(1)
        self.search_tree.put(2)
        self.search_tree.put(5)
        self.assertFalse(self.search_tree.contains(0))
        self.assertTrue(self.search_tree.contains(1))
        self.assertTrue(self.search_tree.contains(2))
        self.assertTrue(self.search_tree.contains(3))
        self.assertFalse(self.search_tree.contains(4))
        self.assertTrue(self.search_tree.contains(5))
        self.assertFalse(self.search_tree.contains(6))
        self.assertEqual(self.search_tree.in_order_traversal(), [1,2,3,5])
    
    #TODO: Write some more tests

if __name__ == '__main__':
    unittest.main()
    