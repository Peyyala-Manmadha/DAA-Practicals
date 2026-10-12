def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
sorted_arr = insertion_sort(arr.copy())
print("Sorted array:", sorted_arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
