## Code Challenge 32 / Find common values in 2 binary trees.
### arguments:  2 binary trees.



## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/256347066-9cc2df35-c81d-4d6e-b9a6-a4495283e0df.jpg)
## Approach & Efficiency

Function repeated_word(string) finds the first repeated word using a custom hash table.

### Approach:


- We'll traverse both trees, tree1 and tree2, in a recursive depth-first manner.
- During the traversal of tree1, we'll collect its node values in a set.
- While traversing tree2, we'll check if the current node's value exists in the set obtained from - tree1. If it does, then it's a common value, and we'll add it to the result list.
- Finally, we'll return the list of common values found during the traversal.
### Efficiency:

Time Complexity: O(m + n)
Space Complexity: O((m, n))
## Solution
```
def tree_intersection(tree1,tree2):
    check= HashTable()
    array = []
    def _walk(root,num=0):

        # root
        if num ==0:
            check.set(root.value,root.value)
        else:
          if  check.has(root.value) :
             array.append(root.value)
             

        # left
        if root.left:
            _walk(root.left,num)
        # right
        if root.right:
            _walk(root.right, num)

    _walk(tree1.root, 0)
    
    _walk(tree2.root, 1)
    return array
```
