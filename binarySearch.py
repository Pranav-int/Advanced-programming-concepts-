def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 40

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
