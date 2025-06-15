# Recursive Remainder

This algorithm calculates the remainder (modulo) of two numbers using recursion. It computes a%b where a is the dividend and b is the divisor, using a recursive approach.

## Time and Space Complexity

- Time Complexity: O(a/b) where a is the dividend and b is the divisor
- Space Complexity: O(a/b) due to the recursion stack

## How it Works
Calculates a mod b (remainder when a is divided by b) using recursive subtraction.

**Recursive Formula:**
- Base case: if a < b, remainder = a
- Recursive case: remainder = (a-b) mod b

## Input Format

The input.txt file should contain:
1. First line: Dividend (a)
2. Second line: Divisor (b)

## Output Format

The output.txt file will contain:
1. Single line: Remainder of a%b

## Example

Input (input.txt):
```
10
3
```

Output (output.txt):
```
1
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses simple recursion
- Base case is when a < b
- Recursive case subtracts b from a until a < b
- Handles negative numbers by converting to positive and adjusting sign
- Assumes b is not zero
- Result is always non-negative and less than b 