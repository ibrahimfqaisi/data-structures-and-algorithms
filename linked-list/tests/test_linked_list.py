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
    
def test_append1():
    node_3=Node("3")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.append(5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 5 } ->  None '
    assert actual == expected
    
def test_append2():
    ll_ =linked_list()
    output= ll_.append(3)
    values =ll_.to_string ()
    actual = values
    expected = '{ 3 } ->  None '
    assert actual == expected

def test_after():
    node_3=Node("2")
    node_2=Node("3",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.after(3,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 3 } -> { 5 } -> { 2 } ->  None '
    assert actual == expected

def test_after2():
    node_3=Node("2")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.after(2,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 2 } -> { 5 } -> { 2 } ->  None '
    assert actual == expected
    
def test_after3():
    node_3=Node("3")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.after(3,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 5 } ->  None '
    assert actual == expected

def test_after4():
    node_3=Node("3")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.after(6,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 2 } -> { 3 } ->  None '
    assert actual == expected


def test_Before():
    node_3=Node("2")
    node_2=Node("3",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.Before(3,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 2 } ->  None '
    assert actual == expected

def test_Before2():
    node_3=Node("2")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.Before(2,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 5 } -> { 2 } -> { 2 } ->  None '
    assert actual == expected
    
def test_Before3():
    node_3=Node("3")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.Before(1,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 5 } -> { 1 } -> { 2 } -> { 3 } ->  None '
    assert actual == expected

def test_Before4():
    node_3=Node("3")
    node_2=Node("2",node_3)
    node_1=Node("1",node_2)
    ll_ =linked_list(node_1)
    output= ll_.Before(6,5)
    values =ll_.to_string ()
    actual = values
    expected = '{ 1 } -> { 2 } -> { 3 } ->  None '
    assert actual == expected


def test_kth():
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_.insert(8)
    ll_.insert(15)
    print(ll_.to_string ())
    index=ll_.kth(2)
    actual = index
    expected = 9
    assert actual == expected
    
def test_kth2():
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_.insert(8)
    ll_.insert(15)
    print(ll_.to_string ())
    index=ll_.kth(-1)
    actual = index
    expected =  15
    assert actual == expected
    
def test_kth3():
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_.insert(8)
    ll_.insert(15)
    print(ll_.to_string ())
    index=ll_.kth(4)
    actual = index
    expected =  15
    assert actual == expected

def test_kth4():
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_.insert(8)
    ll_.insert(15)
    print(ll_.to_string ())
    
    with pytest.raises(Exception) as error:
        ll_.kth(50)
    assert str(error.value) == "Index out of range."