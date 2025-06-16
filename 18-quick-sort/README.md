# Quick Sort

This algorithm sorts an array using the divide and conquer quick sort algorithm with partitioning.

## Time and Space Complexity

- Time Complexity: O(n log n) average case, O(n²) worst case
- Space Complexity: O(log n) average case due to recursion stack

### How it Works
Selects a pivot element and partitions the array around it, then recursively sorts the partitions.

**Algorithm Steps:**
1. Choose a pivot element (last element in this implementation)
2. Partition array: elements ≤ pivot go left, elements > pivot go right
3. Recursively apply quicksort to left and right partitions

**Partitioning:**
- Use two pointers to rearrange elements
- Place pivot in its correct final position
- Return pivot index for recursive calls

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
7
10 7 8 9 1 5 3
```

Output (output.txt):
```
1 3 5 7 8 9 10
```

## Implementation Notes

- All implementations use standard libraries only
- In-place sorting algorithm with O(1) extra space for partitioning
- Pivot selection affects performance (last element used here)
- Worst case O(n²) occurs with already sorted arrays
- Average case performance is excellent for random data
- Can be optimized with randomized pivot selection or median-of-three