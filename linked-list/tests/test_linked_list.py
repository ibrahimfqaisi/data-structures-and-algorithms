import pytest
from linked_list.linked_list import (Node ,linked_list,) 

def test_instantiate_empty_linked_list():
    class1 = linked_list()
    actual = class1.head
    expected = None
    assert actual == expected
    

def test_insert ():
    class2=linked_list("malek")
    class2.insert("ibrahim")
    actual = class2.head.value  
    expected = "ibrahim"
    assert actual == expected

def test_first_node():
    node_M=Node("malek")
    node_I=Node("Ibrahim",node_M)
    ll_ =linked_list(node_I)
    actual = ll_.head.value
    expected = "Ibrahim"
    assert actual == expected
    
def test_multiple_nodes():
    node_M=Node("malek")
    node_I=Node("Ibrahim",node_M)
    actual = node_I.value
    expected = "Ibrahim"
    assert actual == expected

def test_multivalue_is_not_exists():
    node_A=Node("Ahmad")
    node_M=Node("malek",node_A)
    node_I=Node("Ibrahim",node_M)
    ll_ =linked_list(node_I)
    test=ll_.includes("mahdi")
    actual = test
    expected = False
    assert actual == expected
    
def test_value_is_exists():
    node_A=Node("Ahmad")
    node_M=Node("malek",node_A)
    node_I=Node("Ibrahim",node_M)
    ll_ =linked_list(node_I)
    test=ll_.includes("Ahmad")
    actual = test
    expected = True
    assert actual == expected

def test_all_the_values():
    node_A=Node("Ahmad")
    node_M=Node("malek",node_A)
    node_I=Node("Ibrahim",node_M)
    ll_ =linked_list(node_I)
    values =ll_.to_string ()
    actual = values
    expected = '{ Ibrahim } -> { malek } -> { Ahmad } ->  None '
    assert actual == expected

