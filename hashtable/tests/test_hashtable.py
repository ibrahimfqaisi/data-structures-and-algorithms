import pytest
from hashtable.hashtable import HashTable

# 'ab' -> 141+142 * 283 = 28300 % 1024 = 652

def test_hash_method1():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual
  
def test_hash_method2():
  expected = 913
  hash = HashTable()
  actual = hash._HashTable__hash('ab')
  assert expected == actual
  
def test_hash_method3():
  expected = 593
  hash = HashTable()
  actual = hash._HashTable__hash('a@b')
  assert expected == actual


def test_hash_method4():
  
  expected = "lolo"
  hash = HashTable()
  hash.set("cat","lolo")
  actual = hash.get('cat')
  assert expected == actual
  
def test_hash_method4():
  
  expected = "lolo"
  hash = HashTable()
  hash.set("cat","lolo")
  
  actual = hash.get('cat')
  assert expected == actual
  
def test_hash_method5():
  
  expected = "mkmo"
  hash = HashTable()
  hash.set("cat","dglo")
  hash.set("cat","mkmo")
  
  actual = hash.get('cat')
  assert expected == actual
  
def test_hash_method6():
  
  expected = None
  hash = HashTable()
  hash.set("cat","dglo")
  hash.set("cat","mkmo")
  
  actual = hash.get('dog')
  assert expected == actual

def test_hash_method7():
  
  expected = ['cat', 'cat', 'dog', 'baird']
  hash = HashTable()
  hash.set("cat","dglo")
  hash.set("cat","mkmo")
  hash.set("dog","hoky")
  hash.set("baird","soso")
  
  actual = hash.keyss()
  assert expected == actual
  
def test_hash_method8():
  expected = True
  hash = HashTable()
  hash.set("cat","dglo")
  hash.set("cat","mkmo")
  actual = hash.check_collision("cat")
  assert expected == actual
  
def test_hash_method9():
  expected = False
  hash = HashTable()
  hash.set("cat","dglo")
  hash.set("cat","mkmo")
  hash.set("dog","hoky")
  actual = hash.check_collision("dog")

  assert expected == actual

def test_hash_method10():
  expected = 1024
  hash = HashTable()
  actual = hash._HashTable__hash('www')
  assert expected >= actual

# (DS._DataScience__PrintMeNot()