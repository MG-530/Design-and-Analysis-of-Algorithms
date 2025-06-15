# Tower of Hanoi

This algorithm solves the Tower of Hanoi puzzle using recursion. The puzzle consists of three rods and n disks of different sizes that can slide onto any rod. The objective is to move the entire stack to another rod, obeying the following rules:
1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack
3. No disk may be placed on top of a smaller disk

## Time and Space Complexity

- Time Complexity: O(2^n) where n is the number of disks
- Space Complexity: O(n) due to the recursion stack

## How it Works
Solves the Tower of Hanoi puzzle: move n disks from source to destination using auxiliary peg, with larger disks always below smaller ones.

**Recursive Strategy:**
1. Move n-1 disks from source to auxiliary (using destination as temporary)
2. Move the largest disk from source to destination
3. Move n-1 disks from auxiliary to destination (using source as temporary)

## Input Format

The input.txt file should contain:
1. Single line: Number of disks (n)

## Output Format

The output.txt file will contain:
1. Multiple lines: Each line describes a move in the format "Move disk from rod X to rod Y"
2. Last line: Total number of moves

## Example

Input (input.txt):
```
3
```

Output (output.txt):
```
Move disk from rod A to rod C
Move disk from rod A to rod B
Move disk from rod C to rod B
Move disk from rod A to rod C
Move disk from rod B to rod A
Move disk from rod B to rod C
Move disk from rod A to rod C
Total moves: 7
```

## Implementation Notes

- All implementations use standard libraries only
- The algorithm uses simple recursion
- Base case is when n = 1
- Recursive case follows the pattern:
  1. Move n-1 disks from source to auxiliary rod
  2. Move nth disk from source to destination rod
  3. Move n-1 disks from auxiliary to destination rod
- Rods are labeled as A, B, and C
- The minimum number of moves required is 2^n - 1 