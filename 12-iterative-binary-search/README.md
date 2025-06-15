# Iterative Binary Search

This algorithm searches for a target value in a sorted array using iterative binary search.

## Time and Space Complexity

- Time Complexity: O(log n) where n is the size of the array
- Space Complexity: O(1) - constant space

## How it Works
Repeatedly divides the search interval in half by comparing the target with the middle element.

**Algorithm Steps:**
1. Set left = 0, right = array_size - 1
2. While left <= right:
   - Calculate mid = (left + right) / 2
   - If array[mid] == target, return mid
   - If array[mid] < target, set left = mid + 1
   - If array[mid] > target, set right = mid - 1
3. Return -1 if not found

## Input Format

The input.txt file should contain:
1. First line: Size of array (n)
2. Second line: n space-separated sorted integers
3. Third line: Target value to search

## Output Format

The output.txt file will contain:
1. Single line: Index of target (0-based) or -1 if not found

## Example

Input (input.txt):
```
7
1 3 5 7 9 11 13
7
```

Output (output.txt):
```
3
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm assumes the input array is already sorted
- Uses iterative approach with while loop to avoid recursion overhead
- Handles edge cases like empty arrays and single-element arrays
- Returns -1 when target is not found in the array
- Mid calculation uses (left + right) / 2 to avoid integer overflow