# Recursive Binary Search

This algorithm searches for a target value in a sorted array using recursive binary search.

## Time and Space Complexity

- Time Complexity: O(log n) where n is the size of the array
- Space Complexity: O(log n) due to recursion stack

## How it Works
Uses divide and conquer approach with recursive calls to search in half of the array.

**Recursive Formula:**
- Base case: left > right, return -1
- If array[mid] == target, return mid
- If array[mid] > target, search left half
- If array[mid] < target, search right half

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
9
```

Output (output.txt):
```
4
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm assumes the input array is already sorted
- Uses recursive divide and conquer approach
- Base case handles when search space is exhausted
- Recursion depth is logarithmic, making it efficient for most cases
- Returns -1 when target is not found in the array