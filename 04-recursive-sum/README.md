# Recursive Sum

This algorithm calculates the sum of numbers from 1 to n using recursion. It demonstrates a simple recursive approach to solve a basic mathematical problem.

## Time and Space Complexity

- Time Complexity: O(n) where n is the input number
- Space Complexity: O(n) due to the recursion stack

## How it Works

The algorithm uses recursion to break down the problem into smaller subproblems:

1. Base Case:
   - When n = 1, return 1
   - This is the smallest subproblem we need to solve

2. Recursive Case:
   - For any n > 1, the sum is n + sum(n-1)
   - This breaks down the problem into:
     * Current number (n)
     * Sum of all previous numbers (sum(n-1))

Example for n = 5:
```
sum(5) = 5 + sum(4)
sum(4) = 4 + sum(3)
sum(3) = 3 + sum(2)
sum(2) = 2 + sum(1)
sum(1) = 1

Therefore:
sum(5) = 5 + 4 + 3 + 2 + 1 = 15
```

The recursion stack builds up as the function calls itself, and then unwinds as it returns the results.

## Input Format

The input.txt file should contain:
1. Single line: A positive integer n

## Output Format

The output.txt file will contain:
1. Single line: Sum of numbers from 1 to n

## Example

Input (input.txt):
```
5
```

Output (output.txt):
```
15
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses simple recursion
- Base case is when n = 1
- Recursive case adds n to the sum of (n-1)
- No iteration or loops are used in the main algorithm 