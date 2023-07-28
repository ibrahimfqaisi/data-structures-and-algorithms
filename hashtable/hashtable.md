
# Code Challenge: Class 30 - Hash Table Implementation 
- Approach & Efficiency

## Time Complexity:

- `__hash method`: The time complexity of calculating the hash code for the given key is O(n), where n is the length of the key. The method iterates through each character of the key and calculates the ASCII value using `ord`, resulting in linear time complexity.

- `set method`: The time complexity of inserting a key-value pair in the hashtable is O(1) on average. However, in the worst-case scenario, when there are many collisions at the same index, the time complexity can become O(n), where n is the number of key-value pairs in the same bucket (linked list traversal).

- `get method`: The time complexity of retrieving a value based on the key is O(1) on average. However, in the worst-case scenario, when there are many collisions at the same index, the time complexity can become O(n), where n is the number of key-value pairs in the same bucket (linked list traversal).

- `has method`: The time complexity of checking if a key exists in the hashtable is the same as the get method, which is O(1) on average and O(n) in the worst-case scenario due to linked list traversal.

- `keys method`: The time complexity of returning a list of all keys present in the hashtable is O(1), as it returns a pre-stored list of keys.

## Space Complexity:

The space complexity of the HashTable class is O(size + n), where size is the size of the bucket array (number of buckets), and n is the number of key-value pairs in the hashtable.


## Solution
python Python/code_challenge30/hashtable/hashtable.py

for testing: pytest Python/code_challenge30/tests/test_hashtable.py
