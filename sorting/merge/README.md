# Merge Sort:

## Merge Sort is a divide-and-conquer sorting algorithm. It recursively divides the array into smaller subarrays, sorts them individually, and then merges them to obtain a sorted sequence. It has a time complexity of O(n log n) and is efficient for sorting large arrays.

## Pseudocode:
```
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left
```
Trace
Sample Array: [8, 4, 23, 42, 16, 15]

Pass 1:
![pass1](/sorting/merge/assest/1.jpg)

In the first pass of merge sort, the array is divided into smaller subarrays until each subarray contains only one element. The array is recursively split into two halves: [8, 4, 23] and [42, 16, 15]. Each half is further divided until each subarray contains only one element.

Pass 2:
![pass1](/sorting/merge/assest/2.jpg)

In the second pass, the smaller subarrays are merged back together in sorted order. The subarray [8, 4, 23] is further divided into [8] and [4, 23]. The subarray [42, 16, 15] is divided into [42] and [16, 15]. The subarrays [8] and [4, 23] are merged to form [4, 8, 23]. Similarly, the subarrays [42] and [16, 15] are merged to form [15, 16, 42].

Pass 3:
![pass1](/sorting/merge/assest/3.jpg)

In the third pass, the two sorted subarrays [4, 8, 23] and [15, 16, 42] are merged together to form the final sorted array. The elements are compared and merged in ascending order. The resulting sorted array is [4, 8, 15, 16, 23, 42].

Efficiency:
Time Complexity: The time complexity of merge sort is O(n log n), where n is the size of the input array. Merge sort divides the array into halves recursively, and then merges the sorted halves, resulting in a time complexity of O(n log n).
Space Complexity: The space complexity of merge sort is O(n) because it requires auxiliary space to store the merged subarrays during the sorting process.
