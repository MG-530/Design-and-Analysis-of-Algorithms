# Recursive Power

This algorithm calculates the power of a number using recursion. It computes x^n where x is the base and n is the exponent, using an efficient recursive approach.

## Time and Space Complexity

- Time Complexity: O(log n) where n is the exponent
- Space Complexity: O(log n) due to the recursion stack

### How it Works
Calculates aᵇ using fast exponentiation (exponentiation by squaring).

**Recursive Formula:**
- Base case: a⁰ = 1
- If b is even: aᵇ = (a^(b/2))²
- If b is odd: aᵇ = a × a^(b-1)

**Example for 2¹⁰:**
```
2¹⁰ = (2⁵)² = (32)² = 1024
2⁵ = 2 × 2⁴ = 2 × 16 = 32
2⁴ = (2²)² = 4² = 16
2² = (2¹)² = 2² = 4
```

This reduces O(n) multiplications to O(log n).
## Input Format

The input.txt file should contain:
1. First line: Base number (x)
2. Second line: Exponent (n)


## Output Format

The output.txt file will contain:
1. Single line: Result of x^n

## Example

Input (input.txt):
```
2
10
```

Output (output.txt):
```
1024
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses efficient recursion with divide-and-conquer
- Base case is when n = 0
- Recursive case uses the property: x^n = (x^(n/2))^2 for even n
- For odd n, multiply by x after squaring
- Handles negative exponents by using 1/x^n 