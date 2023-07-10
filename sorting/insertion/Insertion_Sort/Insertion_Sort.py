def InsertionSort(input):
    n = len(input)
    if n <= 1:
        return input  

    for i in range(1, n):
        Insert(input, i)

    return input


def Insert(arr, index):
    value = arr[index]
    j = index - 1
    while j >= 0 and arr[j] > value:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = value
