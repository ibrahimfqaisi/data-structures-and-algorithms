import pytest
from stack_queue.trees.trees import (binary_tree, Tnode, binary_search_tree)

def test_run_tests():
    tree = binary_tree()
    vars
    output =tree.maximum_value()
    assert output=="the tree is empty"
    print("Test 1 passed")
    
def test_run_tests2():
    tree = binary_tree()
    tree.root = Tnode(1)
    assert tree.maximum_value() == 1
    print("Test 2 passed")
    
def test_run_tests3():
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    assert bst.maximum_value() == 7
    print("Test 3 passed")
