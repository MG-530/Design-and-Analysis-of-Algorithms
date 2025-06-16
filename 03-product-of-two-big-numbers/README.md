# Product of Two Big Numbers (Divide and Conquer)

This algorithm multiplies two large numbers using the Karatsuba divide and conquer algorithm. It's more efficient than the traditional O(n²) multiplication for large numbers.

## Time and Space Complexity

- Time Complexity: O(n^log₂3) ≈ O(n^1.585) where n is the number of digits
- Space Complexity: O(n log n) due to the recursion stack and temporary strings

### How it Works
Uses Karatsuba algorithm by splitting numbers into two halves:
- For numbers x and y with n digits each:
- x = x₁ × 10^(n/2) + x₀
- y = y₁ × 10^(n/2) + y₀
- x × y = x₁y₁ × 10^n + ((x₁ + x₀)(y₁ + y₀) - x₁y₁ - x₀y₀) × 10^(n/2) + x₀y₀

**Optimization:**
This reduces 4 multiplications to 3 recursive calls:
1. x₁y₁
2. x₀y₀  
3. (x₁ + x₀)(y₁ + y₀)

## Input Format

The input.txt file should contain:
1. First line: First big number (as string of digits)
2. Second line: Second big number (as string of digits)

## Output Format

The output.txt file will contain:
1. Single line: Product of the two numbers

## Example

Input (input.txt):
```
123456789
987654321
```

Output (output.txt):
```
121932631137021795226185032733622923332237463801111263526900
```

## Implementation Notes

- Numbers are stored as strings to handle arbitrary precision
- Leading zeros are handled properly
- The algorithm works with numbers of different lengths
- Base case uses standard multiplication for small numbers (< 10 digits)
- Handles edge cases like zero and single-digit numbers