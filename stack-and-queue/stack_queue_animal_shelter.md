# Challenge Title
    Code Challenge / Algorithm

## Stretch Goal
    I solced Stretch Goal

## Whiteboard Process
![dequeue(animal)](https://user-images.githubusercontent.com/125550572/242603565-baa157c0-5850-4508-9731-db02c2800e34.jpg)
![enqueue(animal , name)](https://user-images.githubusercontent.com/125550572/242603583-cae317cb-089a-4f76-ad65-fe3ce796472e.jpg)
## Approach & Efficiency
## Enqueue:
 The animal's name is added to the respective list based on its species. This operation has a constant time complexity of O(1).

## Dequeue:
 The dequeue function removes an animal from the shelter based on the provided preference. If the preference is "dog" or "cat", the corresponding list is checked for availability, and the first element is removed and returned. If the preference is "cat_or_dog", the dogs list is checked first, then the cats list. The first available animal is removed and returned. The dequeue operation has a constant time complexity of O(1) for accessing and removing the first element from a list.

The space complexity of the implementation is O(n), where n is the total number of animals in the shelter. This is because the space required to store the animal names in the lists grows linearly with the number of animals.
## Solution
 [pseudo_queue.py](../stack-and-queue/stack_queue/stack_queue_animal_shelter.py)

 i used chatgpt to write doc str foe me code 