def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    first_occurrence = -1  # Initialize to -1 if not found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_occurrence = mid
            high = mid - 1  # Continue searching in the left half for the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_occurrence

arr = [2, 5, 5, 5, 8, 9]
target = 5
index = find_first_occurrence(arr, target)
print(f"The first occurrence of {target} is at index: {index}")