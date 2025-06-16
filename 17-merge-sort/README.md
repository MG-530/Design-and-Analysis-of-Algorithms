# Merge Sort

This algorithm sorts an array using the divide and conquer merge sort algorithm.

## Time and Space Complexity

- Time Complexity: O(n log n) in all cases (best, average, worst)
- Space Complexity: O(n) for temporary arrays during merging

### How it Works
Recursively divides the array into halves until single elements, then merges them back in sorted order.

**Algorithm Steps:**
1. Divide: Split array into two halves
2. Conquer: Recursively sort both halves
3. Combine: Merge the sorted halves

**Merge Process:**
- Compare elements from both halves
- Place smaller element in result array
- Continue until all elements are merged

## Input Format

The input.txt file should contain:
1. First line: Size of array (n)
2. Second line: n space-separated integers

## Output Format

The output.txt file will contain:
1. Single line: n space-separated sorted integers

## Example

Input (input.txt):
```
6
64 34 25 12 22 11
```

Output (output.txt):
```
11 12 22 25 34 64
```

## Implementation Notes

- All implementations use standard libraries only
- Stable sorting algorithm (maintains relative order of equal elements)
- Guaranteed O(n log n) performance regardless of input distribution
- Uses additional O(n) space for temporary arrays during merging
- Recursive depth is O(log n)
- Well-suited for large datasets and external sorting