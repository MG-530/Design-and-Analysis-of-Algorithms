# Recursive GCD (Greatest Common Divisor)

This algorithm calculates the Greatest Common Divisor (GCD) of two numbers using recursion. The GCD is the largest positive integer that divides both numbers without leaving a remainder.

## Time and Space Complexity

- Time Complexity: O(log(min(a,b))) where a and b are the input numbers
- Space Complexity: O(log(min(a,b))) due to the recursion stack

### How it Works
Uses Euclidean algorithm: GCD(a,b) = GCD(b, a mod b).

**Mathematical Principle:**
The GCD of two numbers doesn't change if we replace the larger number with the remainder of dividing it by the smaller number.

**Recursive Formula:**
- Base case: GCD(a, 0) = a
- Recursive case: GCD(a, b) = GCD(b, a mod b)

## Input Format

The input.txt file should contain:
1. First line: First number (a)
2. Second line: Second number (b)

## Output Format

The output.txt file will contain:
1. Single line: GCD of a and b

## Example

Input (input.txt):
```
48
18
```

Output (output.txt):
```
6
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses Euclid's algorithm: GCD(a,b) = GCD(b,a%b)
- Base case is when b = 0, in which case a is the GCD
- The algorithm handles negative numbers by using absolute values
- This is one of the most efficient ways to calculate GCD 