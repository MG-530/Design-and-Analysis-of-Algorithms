# Strassen's Matrix Multiplication

Strassen's algorithm is a divide-and-conquer algorithm for matrix multiplication that is asymptotically faster than the standard algorithm.
Instead of the standard O(n³) matrix multiplication, Strassen's algorithm achieves O(n^log₂7) ≈ O(n^2.807) complexity by reducing the number of recursive multiplications from 8 to 7.

## Time and Space Complexity

- Time Complexity: O(n^log₂7) ≈ O(n^2.807)
- Space Complexity: O(n^2) for storing matrices

## How it Works

For 2×2 matrices:
```
A = [a11 a12]    B = [b11 b12]
    [a21 a22]        [b21 b22]
```

Standard algorithm requires 8 multiplications, but Strassen uses only 7:
- P1 = (a11 + a22)(b11 + b22)
- P2 = (a21 + a22)b11
- P3 = a11(b12 - b22)
- P4 = a22(b21 - b11)
- P5 = (a11 + a12)b22
- P6 = (a21 - a11)(b11 + b12)
- P7 = (a12 - a22)(b21 + b22)

Result matrix C:
- c11 = P1 + P4 - P5 + P7
- c12 = P3 + P5
- c21 = P2 + P4
- c22 = P1 - P2 + P3 + P6


## Input Format

The input.txt file should contain:
1. First line: Size of matrices (n)
2. Next n lines: First matrix elements (space-separated)
3. Next n lines: Second matrix elements (space-separated)

## Output Format

The output.txt file will contain:
- n lines with n space-separated numbers representing the resulting matrix

## Example

Input (input.txt):
```
2
1 2
3 4
5 6
7 8
```

Output (output.txt):
```
19 22
43 50
```

## Implementation Notes

- All implementations use standard libraries only
- Matrices are represented as 2D arrays/lists
- The algorithm uses divide-and-conquer approach
- Base case is when matrix size is 1x1 