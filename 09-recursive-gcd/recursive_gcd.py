def recursive_gcd(a: int, b: int) -> int:
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return recursive_gcd(b, a % b)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        a, b = map(int, f.read().strip().split())
    
    # Calculate GCD
    result = recursive_gcd(a, b)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main() 