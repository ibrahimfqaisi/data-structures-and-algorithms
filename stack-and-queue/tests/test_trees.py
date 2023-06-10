import pytest
from stack_queue.trees.trees import (binary_tree, Tnode, binary_search_tree)

def test_run_tests():
    # Test 1: Can successfully instantiate an empty tree
    tree = binary_tree()
    assert tree.root is None
    print("Test 1 passed")
    
def test_run_tests2():
    # Test 2: Can successfully instantiate a tree with a single root node
    tree = binary_tree()
    tree.root = Tnode(1)
    assert tree.root.value == 1
    print("Test 2 passed")
    
def test_run_tests3():
    # Test 3: For a Binary Search Tree, can successfully add a left child and right child properly to a node
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.root.value == 5
    assert bst.root.left.value == 3
    assert bst.root.right.value == 7
    print("Test 3 passed")
    
def test_run_tests4():
    # Test 4: Can successfully return a collection from a pre-order traversal
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.pre_order() == [5, 3, 7]
    print("Test 4 passed")
    
def test_run_tests5():
    # Test 5: Can successfully return a collection from an in-order traversal
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.in_order() == [3, 5, 7]
    print("Test 5 passed")
    
def test_run_tests6():
    # Test 6: Can successfully return a collection from a post-order traversal
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.post_order() == [3, 7, 5]
    print("Test 6 passed")

def test_run_tests7():
    # Test 7: Returns true for the Contains method, given an existing node value
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.Contains(3) is True
    print("Test 7 passed")
def test_run_tests8():
    # Test 8: Returns false for the Contains method, given a non-existing node value
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.Contains(10) is False
    print("Test 8 passed")