
# Code Challenge: Class 33 - Implement a simplified LEFT JOIN for 2 Hashmaps.
### arguments:  2 Hashmaps.

## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/257262106-00acfefe-36b7-4a9f-8494-6a30b8a79c73.jpg)
## Approach & Efficiency

### Approach:

The function left_join performs a left join on two hash tables hashTable1 and hashTable2.
It initializes an empty list output.
For each key in hashTable1, it checks if the key exists in hashTable2.
If the key exists in both hash tables, it appends [key, hashTable1.get(key), hashTable2.get(key)] to output.
If the key exists only in hashTable1, it appends [key, hashTable1.get(key), None] to output.
Finally, it returns the output list.
### Efficiency:

Time Complexity: O(n), where "n" is the number of keys in hashTable1.
Space Complexity: O(n) in the worst case due to the output list storing the left join results.
## Solution
```
def left_join(hashTable1,hashTable2):
    '''
    A method to perform a left join on two hashtables
    args: HashTable1,HashTable2
    '''
    
    output=[]
    keyss= hashTable1.keyss()
    for key in keyss:
        if hashTable2.has(key):
            output.append([key,hashTable1.get(key),hashTable2.get(key)])
        else:
            output.append([key,hashTable1.get(key),None])
            
    return output
```
