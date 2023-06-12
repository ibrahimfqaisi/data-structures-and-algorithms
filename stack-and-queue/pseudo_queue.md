# Challenge Title
    Extending an Implementation

## Whiteboard Process
![dequeue()](https://user-images.githubusercontent.com/125550572/245195632-413d8091-f6bb-4c7b-876a-583c7ee1d1e7.jpg)

## Approach & Efficiency
Approach:

1- Initialize max_value to negative infinity.
2- Traverse the binary tree recursively.
3- Update max_value with the maximum of the node's value and the maximum values from the left and right subtrees.
4- Recurse on the left and right children.
5 -Return max_value as the maximum value found.
Efficiency:

* Time Complexity: O(n) - We need to visit all nodes to find the maximum value in the worst case.
* Space Complexity: O(h) - The space used on the call stack is proportional to the height of the tree. In the worst case, the height can be equal to the number of nodes (linear), resulting in O(n) space complexity.

## tests
  [test_pseudo_queue.py](../stack-and-queue/tests/test_trees_maximum_value.py)
## Solution
 [pseudo_queue.py](../stack-and-queue/stack_queue/trees/trees.py)