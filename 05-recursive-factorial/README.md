# Recursive Factorial

This algorithm calculates the factorial of a number using recursion. The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.

## Time and Space Complexity

- Time Complexity: O(n) where n is the input number
- Space Complexity: O(n) due to the recursion stack

## How It Works

The recursive factorial algorithm works as follows:

1. Base Cases:
   - If n = 0 or n = 1, return 1 (since 0! = 1 and 1! = 1)

2. Recursive Case:
   - For any n > 1, calculate n! as: n × (n-1)!
   - This breaks down the problem into smaller subproblems

3. Recursion Process:
   - For example, calculating 5!:
     * 5! = 5 × 4!
     * 4! = 4 × 3!
     * 3! = 3 × 2!
     * 2! = 2 × 1!
     * 1! = 1 (base case)

## Input Format

The input.txt file should contain:
1. Single line: A non-negative integer n

## Output Format

The output.txt file will contain:
1. Single line: Factorial of n (n!)

## Example

Input (input.txt):
```
5
```

Output (output.txt):
```
120
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses simple recursion
- Base case is when n = 0 or n = 1
- Recursive case multiplies n by (n-1)!
- No iteration or loops are used in the main algorithm
- Handles edge case of 0! = 1 