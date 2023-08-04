import pytest
from hashmap_left_join.hashmap_left_join import HashTable, left_join

def test_left_join():
    hashTable1 = HashTable()
    hashTable1.set("diligent", "employed")
    hashTable1.set("fond", "enamored")
    hashTable1.set("guide", "usher")
    hashTable1.set("outfit", "garb")
    hashTable1.set("wrath", "anger")

    hashTable2 = HashTable()
    hashTable2.set("diligent", "idle")
    hashTable2.set("fond", "averse")
    hashTable2.set("guide", "follow")
    hashTable2.set("flow", "jam")
    hashTable2.set("wrath", "delight")

    result = left_join(hashTable1, hashTable2)
    assert result == [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]
def test_left_join_basic():
    hashTable1 = HashTable()
    hashTable1.set("apple", "fruit")
    hashTable1.set("banana", "fruit")
    hashTable1.set("carrot", "vegetable")

    hashTable2 = HashTable()
    hashTable2.set("apple", "red")
    hashTable2.set("banana", "yellow")
    hashTable2.set("grape", "purple")

    result = left_join(hashTable1, hashTable2)
    assert result == [
        ["apple", "fruit", "red"],
        ["banana", "fruit", "yellow"],
        ["carrot", "vegetable", None]
    ]

def test_left_join_empty_second_table():
    hashTable1 = HashTable()
    hashTable1.set("dog", "animal")
    hashTable1.set("cat", "animal")
    hashTable1.set("bird", "animal")

    hashTable2 = HashTable()

    result = left_join(hashTable1, hashTable2)
    assert result == [
        ["dog", "animal", None],
        ["cat", "animal", None],
        ["bird", "animal", None]
    ]