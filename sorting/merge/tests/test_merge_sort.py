import pytest
from Insertion_Sort.merge_sort import (merge_sort)
# Test cases for Insertion Sort

def test_insertion_sort_empty_array():
    input_array = []
    sorted_array = merge_sort(input_array)
    assert sorted_array == []

def test_insertion_sort_already_sorted_array():
    input_array = [1, 2, 3, 4, 5]
    sorted_array = merge_sort(input_array)
    assert sorted_array == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted_array():
    input_array = [20, 18, 12, 8, 5, -2]
    sorted_array = merge_sort(input_array)
    assert sorted_array == [-2, 5, 8, 12, 18, 20]

def test_insertion_sort_few_uniques_array():
    input_array = [5, 12, 7, 5, 5, 7]
    sorted_array = merge_sort(input_array)
    assert sorted_array == [5, 5, 5, 7, 7, 12]

def test_insertion_sort_nearly_sorted_array():
    input_array = [2, 3, 5, 7, 13, 11]
    sorted_array = merge_sort(input_array)
    assert sorted_array == [2, 3, 5, 7, 11, 13]

