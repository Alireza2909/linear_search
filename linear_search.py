# Linear Search Algorithm Implementation in Python

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Target found
    return -1  # Target not found

# Example usage
arr = [5, 3, 6, 8, 9, 2]
target = 8

result = linear_search(arr, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")