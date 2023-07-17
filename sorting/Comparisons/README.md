# Insertion Sort:

## Insertion Sort is a sorting algorithm that gradually builds a sorted sequence by selecting elements from the unsorted part of the array and inserting them into their correct positions within the sorted part. It iterates through the array, comparing and shifting elements as needed, until the entire array is sorted. It is efficient for small or partially sorted arrays.

## Pseudocode:
```
    Insert(int[] sorted, int value)
    initialize i to 0
    WHILE value > sorted[i]
        set i to i + 1
    WHILE i < sorted.length
        set temp to sorted[i]
        set sorted[i] to value
        set value to temp
        set i to i + 1
    append value to sorted

    InsertionSort(int[] input)
    LET sorted = New Empty Array
    sorted[0] = input[0]
    FOR i from 1 up to input.length
        Insert(sorted, input[i])
    return sorted
```
Pass 1:

Pass 1 of Insertion  Sort
![pass1](/sorting/insertion/assest/1.jpg)



sorted = [8]
The second element, 4, is compared to the only element in the sorted array (8). Since 4 is smaller, it is inserted at index 0. The sorted array becomes [4, 8].

Pass 2:

Pass 2 of Insertion  Sort
![pass2](/sorting/insertion/assest/2.jpg)

sorted = [4, 23]
The third element, 23, is compared to the elements in the sorted array. It is greater than 4, so it remains at its current position. The sorted array remains [4, 23]
Pass 3:

Pass 3 of Insertion  Sort
![pass3](/sorting/insertion/assest/3.jpg)
sorted = [4, 8, 23]
The fourth element, 42, is compared to the elements in the sorted array. It is greater than 4 and 8, so it remains at its current position. The sorted array remains [4, 8, 23].

Pass 4:
![pass4](/sorting/insertion/assest/4.jpg)
Pass 4 of Insertion  Sort

sorted = [4, 8, 23, 42]
The fifth element, 16, is compared to the elements in the sorted array. It is smaller than 23 and greater than 8, so it is inserted at index 2. The sorted array becomes [4, 8, 16, 23, 42].

After the fourth pass, the Insertion Sort algorithm completes iterating through all elements of the input array, and the final sorted array is [4, 8, 16, 23, 42], representing the sorted version of the input array [8, 4, 23, 42, 16, 15].

## Efficency
Time: O(n^2)

Space: O(n)
