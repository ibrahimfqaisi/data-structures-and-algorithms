import pytest
from tree_intersection.tree_intersection import (binary_search_tree,tree_intersection)

def test_run_tests1():
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    bst2 = binary_search_tree()
    bst2.Add(5)
    bst2.Add(3)
    bst2.Add(7)
    assert tree_intersection(bst,bst2) == [5, 3, 7]
    print("Test 1 passed")

def test_run_tests2():
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    bst2 = binary_search_tree()
    bst2.Add(0)
    bst2.Add(1)
    bst2.Add(2)
    assert tree_intersection(bst,bst2) == []
    print("Test 2 passed")
def test_run_tests3():
    bst = binary_search_tree()
    bst.Add(5)
    bst.Add(3)
    bst.Add(7)
    bst2 = binary_search_tree()
    bst2.Add(5)
    bst2.Add(10)
    bst2.Add(99)
    assert tree_intersection(bst,bst2) == [5]

    print("Test 3 passed")