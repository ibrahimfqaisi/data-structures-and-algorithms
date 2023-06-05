# Challenge Title
    stack-queue-brackets

## Whiteboard Process for stack-queue-brackets_useing stack 
![stack-queue-brackets_useing stack)](https://user-images.githubusercontent.com/125550572/243447284-3bbaaeb8-0557-42d0-a84e-f8e65baea2c9.jpg)


## Whiteboard Process for stack-queue-brackets_with out stack
![ stack-queue-brackets_with out stack](https://user-images.githubusercontent.com/125550572/243447278-ae580dd9-5ad5-4e04-a7e2-61e622253703.jpg)
## Approach & Efficiency
## Approach

1. Initialize a counter variable, `balance`, to 0.

2. Iterate over each character in the input string:
   - If the character is an opening bracket (`(`, `{`, or `[`), increment `balance` by 1.
   - If the character is a closing bracket (`)`, `}`, or `]`), decrement `balance` by 1.
     - If `balance` becomes negative, return `False` immediately since the brackets are not balanced.

3. Return `True` if `balance` is 0, indicating that the brackets are balanced. Otherwise, return `False`.

## Efficiency

- Time Complexity: O(n), where n is the length of the input string. Each character is processed once in the loop.
- Space Complexity: O(1). The space usage is constant as we only need the `balance` variable to keep track of the bracket balance.

## Solution
 [stack-queue-brackets_useing stack](../stack-and-queue/stack_queue/validate_brackets_used_stack.py)
 [stack-queue-brackets_with out stack](../stack-and-queue/stack_queue/validate_brackets.py)

