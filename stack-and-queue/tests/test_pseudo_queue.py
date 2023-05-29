import pytest
from stack_queue.pseudo_queue import PseudoQueue

def test_Queue_enqueue ():
    Queue_01 = PseudoQueue()
    Queue_01.enqueue(1)
    index=Queue_01.__str__()
    actual = index
    expected =  '1'
    assert actual == expected
def test_Queue_enqueue02 ():
    Queue_01= PseudoQueue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    index=Queue_01.__str__()
    actual = index
    expected =  '4 -> 3 -> 2 -> 1'
    assert actual == expected
def test_Queue_dequeue():
    Queue_01= PseudoQueue()
    Queue_01.enqueue(1)
    Queue_01.enqueue(2)
    Queue_01.enqueue(3)
    Queue_01.enqueue(4)
    Queue_01.dequeue()
    index=Queue_01.__str__()
    actual = index
    expected =  '4 -> 3 -> 2'
    assert actual == expected

