import pytest
from stack_queue.stack import (Node ,Stack,) 

def test_Stack_push ():
    stack_01 = Stack()
    stack_01_new=stack_01.push(1)
    
    index=stack_01.__str__()
    actual = index
    expected =  '1 -> None'
    assert actual == expected
def test_Stack_push02 ():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    index=stack_01.__str__()
    actual = index
    expected =  '4 -> 3 -> 2 -> 1 -> None'
    assert actual == expected
def test_Stack_pop():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01.pop()
    index=stack_01.__str__()
    actual = index
    expected =  '3 -> 2 -> 1 -> None'
    assert actual == expected
def test_Stack_pop2():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01.pop()
    stack_01.pop()
    stack_01.pop()
    stack_01.pop()
    index=stack_01.is_empty()
    actual = index
    expected =  True
    assert actual == expected
def test_Stack_next ():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    index=stack_01.top.next.value
    actual = index
    expected =  3
    assert actual == expected
def test_Stack_instantiate ():
    stack_01= Stack()
    index=stack_01.is_empty()
    actual = index
    expected =  True
    assert actual == expected
def test_Stack_pop_():
    stack_01= Stack()
    with pytest.raises(Exception) as error:
       stack_01.pop()
    assert str(error.value) == "the stack is empty"
    
def test_Stack_peek ():
    stack_01= Stack()
    with pytest.raises(Exception) as error:
       stack_01.peek()
    assert str(error.value) == "the stack is empty"

