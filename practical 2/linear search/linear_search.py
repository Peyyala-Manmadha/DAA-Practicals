def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
print("Array:", arr)
target = int(input("Enter element to search: "))
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Time Complexity: O(n)
# Space Complexity: O(1)
