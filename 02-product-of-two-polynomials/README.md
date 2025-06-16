# Product of Two Polynomials (Divide and Conquer)

This algorithm multiplies two polynomials using divide and conquer approach. The implementation uses Karatsuba-like algorithm for polynomial multiplication.

## Time and Space Complexity

- Time Complexity: O(n^log₂3) ≈ O(n^1.585) where n is the degree of the polynomial
- Space Complexity: O(n log n) due to the recursion stack and temporary arrays

## How it Works
Uses divide and conquer by splitting polynomials into two halves and applying the formula:
- P(x) = P₁(x) * x^(n/2) + P₀(x)
- Q(x) = Q₁(x) * x^(n/2) + Q₀(x)
- P(x) * Q(x) = P₁Q₁ * x^n + (P₁Q₀ + P₀Q₁) * x^(n/2) + P₀Q₀

**Optimization:**
Uses the identity: (P₁Q₀ + P₀Q₁) = (P₁ + P₀)(Q₁ + Q₀) - P₁Q₁ - P₀Q₀
This reduces the number of recursive calls from 4 to 3.

## Input Format

The input.txt file should contain:
1. First line: Degree of first polynomial (n)
2. Second line: Coefficients of first polynomial (a₀ a₁ a₂ ... aₙ)
3. Third line: Degree of second polynomial (m)
4. Fourth line: Coefficients of second polynomial (b₀ b₁ b₂ ... bₘ)

## Output Format

The output.txt file will contain:
1. First line: Degree of result polynomial
2. Second line: Coefficients of result polynomial

## Example

Input (input.txt):
```
2
1 2 3
1
2 1
```

This represents:
- First polynomial: 1 + 2x + 3x²
- Second polynomial: 2 + x

Output (output.txt):
```
3
2 5 8 3
```

This represents: 2 + 5x + 8x² + 3x³

## Implementation Notes

- Coefficients are stored from lowest to highest degree
- The algorithm handles polynomials of different degrees
- Padding with zeros is used to make degrees equal for divide and conquer
- Base case is multiplication of polynomials with degree ≤ 1