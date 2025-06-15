def recursive_quotient(a: int, b: int) -> int:
    # Handle negative numbers
    if a < 0 and b < 0:
        return recursive_quotient(-a, -b)
    elif a < 0:
        return -recursive_quotient(-a, b)
    elif b < 0:
        return -recursive_quotient(a, -b)
    
    # Base case
    if a < b:
        return 0
    
    # Recursive case
    return 1 + recursive_quotient(a - b, b)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        a, b = map(int, f.read().strip().split())
    
    # Calculate result
    result = recursive_quotient(a, b)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main() 