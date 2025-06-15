# Recursive Combination

This algorithm calculates the number of ways to choose k items from a set of n items using recursion. The combination formula C(n,k) represents the number of possible combinations.

## Time and Space Complexity

- Time Complexity: O(2^n) where n is the total number of items
- Space Complexity: O(n) due to the recursion stack

## How it Works
Calculates C(n,k) = n!/(k!(n-k)!) using Pascal's triangle property.

**Recursive Formula:**
- Base cases: C(n,0) = 1, C(n,n) = 1
- Recursive case: C(n,k) = C(n-1,k-1) + C(n-1,k)

**Mathematical Insight:**
To choose k items from n items, either:
- Include the first item and choose k-1 from remaining n-1, OR
- Exclude the first item and choose k from remaining n-1

## Input Format

The input.txt file should contain:
1. First line: Total number of items (n)
2. Second line: Number of items to choose (k)

## Output Format

The output.txt file will contain:
1. Single line: Number of possible combinations C(n,k)

## Example

Input (input.txt):
```
5
2
```

Output (output.txt):
```
10
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses the properties of Pascal's triangle
- Base cases:
  - C(n,0) = 1 (choosing 0 items)
  - C(n,n) = 1 (choosing all items)
  - C(n,k) = 0 if k > n (impossible to choose more items than available)
- Recursive case: C(n,k) = C(n-1,k-1) + C(n-1,k)
- This is a classic example of recursive combinatorial mathematics 