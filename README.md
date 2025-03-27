# Linear Search Algorithm in Python

This repository contains the implementation of the Linear Search algorithm in Python.

## How to use

1. Clone this repository.
2. Run the `linear_search.py` file with Python.
3. The `linear_search(arr, target)` method searches for the target value in an array.

## Example

```python
arr = [5, 3, 6, 8, 9, 2]
target = 8

result = linear_search(arr, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")