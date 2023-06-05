import pytest
from stack_queue.validate_brackets import validateBrackets 

def test_validate_brackets1 ():
    output=validateBrackets("{}")
    actual = output
    expected =  True
    assert actual == expected
def test_validate_brackets2 ():
    output=validateBrackets("{}(){}")
    actual = output
    expected =  True
    assert actual == expected
    
def test_validate_brackets3 ():
    output=validateBrackets("()[[Extra Characters]]")
    actual = output
    expected =  True
    assert actual == expected

def test_validate_brackets4 ():
    output=validateBrackets("(){}[[]]")
    actual = output
    expected =  True
    assert actual == expected

def test_validate_brackets5 ():
    output=validateBrackets("{}{Code}[Fellows](())")
    actual = output
    expected =  True
    assert actual == expected

def test_validate_brackets6 ():
    output=validateBrackets("[({}]")
    actual = output
    expected =  False
    assert actual == expected

def test_validate_brackets7 ():
    output=validateBrackets("(](")
    actual = output
    expected =  False
    assert actual == expected

def test_validate_brackets8 ():
    output=validateBrackets("{(})")
    actual = output
    expected =  False
    assert actual == expected