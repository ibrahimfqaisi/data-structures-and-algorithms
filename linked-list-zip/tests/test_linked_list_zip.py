import pytest
from linked_list_zip.linked_list_zip import (Node ,linked_list,zipLists) 

def test_all_the_values():
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_2 = linked_list(Node(10))
    ll_2.insert(11)
    ll_2.insert(12)
    ll_2.insert(13)
    ll_2.insert(14)       
    values = zipLists(ll_,ll_2)     
    actual = values
    expected = '{ 9 } -> { 14 } -> { 6 } -> { 13 } -> { 5 } -> { 12 } -> { 11 } -> { 10 } ->  None '
    assert actual == expected

def test_all_the_values2():
    ll_ = linked_list(Node(2))
    ll_.insert(3)
    ll_.insert(1)
    ll_2 = linked_list(Node(4))
    ll_2.insert(9)
    ll_2.insert(5)
         
    values = zipLists(ll_,ll_2)     
    actual = values
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } ->  None '
    assert actual == expected
    
def test_all_the_values3():
    ll_ = linked_list(Node(3))
    ll_.insert(1)

    ll_2 = linked_list(Node(4))
    ll_2.insert(9)
    ll_2.insert(5)
    values = zipLists(ll_,ll_2)     
    actual = values
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } ->  None '
    assert actual == expected
def test_all_the_values4():
    ll_ = linked_list(Node(2))
    ll_.insert(3)
    ll_.insert(1)
    ll_2 = linked_list(Node(9))
    ll_2.insert(5)  
    values = zipLists(ll_,ll_2)     
    actual = values
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } ->  None '
    assert actual == expected

