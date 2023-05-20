import pytest
from stack_queue.queue import (Node ,Queue,) 

def test_Queue_enqueue ():
    Queue_01 = Queue()
    Queue_01.enqueue(1)
    index=Queue_01.__str__()
    actual = index
    expected =  '1 -> None'
    assert actual == expected
def test_Queue_enqueue02 ():
    Queue_01= Queue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    index=Queue_01.__str__()
    actual = index
    expected =  '1 -> 2 -> 3 -> 4 -> None'
    assert actual == expected
def test_Queue_dequeue():
    Queue_01= Queue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    Queue_01.dequeue()
    index=Queue_01.__str__()
    actual = index
    expected =  '2 -> 3 -> 4 -> None'
    assert actual == expected
def test_Queue_dequeue2():
    Queue_01= Queue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    Queue_01.dequeue()
    Queue_01.dequeue()
    Queue_01.dequeue()
    Queue_01.dequeue()
    index=Queue_01.is_empty()
    actual = index
    expected =  True
    assert actual == expected
def test_Queue_next ():
    Queue_01= Queue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    index=Queue_01.peek()
    actual = index
    expected =  1
    assert actual == expected
def test_Queue_instantiate ():
    Queue_01= Queue()
    index=Queue_01.is_empty()
    actual = index
    expected =  True
    assert actual == expected
def test_Queue_dequeues_():
    Queue_01= Queue()
    with pytest.raises(Exception) as error:
       Queue_01.dequeue()
    assert str(error.value) == "the queue is empty"
    
def test_Queue_peek ():
    Queue_01= Queue()
    with pytest.raises(Exception) as error:
       Queue_01.peek()
    assert str(error.value) == "the queue is empty"

