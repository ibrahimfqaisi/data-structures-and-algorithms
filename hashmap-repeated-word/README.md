## Code Challenge / hashmap_repeated_word
### arguments: string



## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/255634365-7daab4fd-96eb-4f14-8bd3-2c6a87ef0de2.jpg)
## Approach & Efficiency

Function repeated_word(string) finds the first repeated word using a custom hash table.

### Approach:

Preprocess input: Remove commas and convert to lowercase.
Split string into words.
Use a hash table to track word occurrences.
Iterate through words, returning the first repeated word.
If no repeat found, return None.
### Efficiency:

Time complexity: O(N + M), where N is string length and M is word count.
Space complexity: O(M) due to the hash table.

## Solution
```
def repeated_word(string):
    '''
    A function that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    '''

    words = string.replace(",","").lower().split()
    
    word_table = HashTable()
    for word in words:
        if word_table.has(word):
            return word
        word_table.set(word, 1)
    return None
            ```
