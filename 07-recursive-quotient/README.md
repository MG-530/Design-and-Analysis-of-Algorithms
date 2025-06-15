# Recursive Quotient

This algorithm calculates the integer division (quotient) of two numbers using recursion. It computes a/b where a is the dividend and b is the divisor, using a recursive approach.

## Time and Space Complexity

- Time Complexity: O(a/b) where a is the dividend and b is the divisor
- Space Complexity: O(a/b) due to the recursion stack

## How it Works
Calculates integer division a ÷ b using repeated subtraction.

**Recursive Formula:**
- Base case: if a < b, quotient = 0
- Recursive case: quotient = 1 + (a-b) ÷ b

## Input Format

The input.txt file should contain:
1. First line: Dividend (a)
2. Second line: Divisor (b)

## Output Format

The output.txt file will contain:
1. Single line: Quotient of a/b

## Example

Input (input.txt):
```
17
5
```

Output (output.txt):
```
3
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses simple recursion
- Base case is when a < b
- Recursive case subtracts b from a and adds 1 to the quotient
- Handles negative numbers by converting to positive and adjusting sign
- Assumes b is not zero 