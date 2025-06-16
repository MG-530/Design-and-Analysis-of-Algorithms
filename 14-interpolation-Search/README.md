# Interpolation Search

This algorithm searches for a target value in a uniformly distributed sorted array using interpolation search.

## Time and Space Complexity

- Time Complexity: O(log log n) for uniform distribution, O(n) worst case
- Space Complexity: O(1) - constant space

## How it Works
Estimates the position of the target based on the value distribution, similar to how we search in a phone book.

**Position Formula:**
pos = left + [(target - arr[left]) / (arr[right] - arr[left])] * (right - left)

**Algorithm Steps:**
1. Calculate interpolated position
2. If array[pos] == target, return pos
3. If array[pos] < target, search right part
4. If array[pos] > target, search left part

## Input Format

The input.txt file should contain:
1. First line: Size of array (n)
2. Second line: n space-separated sorted integers (preferably uniform distribution)
3. Third line: Target value to search

## Output Format

The output.txt file will contain:
1. Single line: Index of target (0-based) or -1 if not found

## Example

Input (input.txt):
```
8
10 20 30 40 50 60 70 80
50
```

Output (output.txt):
```
4
```

## Implementation Notes

- All implementations use standard libraries only
- Works best with uniformly distributed data
- Falls back to linear-like performance for non-uniform distributions
- Handles boundary checks to prevent array index out of bounds
- More efficient than binary search for uniformly distributed large datasets
- Returns -1 when target is not found in the array