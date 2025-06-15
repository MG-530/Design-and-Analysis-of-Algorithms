def recursive_remainder(a: int, b: int) -> int:
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Base case
    if a < b:
        return a
    
    # Recursive case
    return recursive_remainder(a - b, b)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        a, b = map(int, f.read().strip().split())
    
    # Calculate remainder
    result = recursive_remainder(a, b)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main() 