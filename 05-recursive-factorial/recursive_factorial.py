def recursive_factorial(n: int) -> int:
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * recursive_factorial(n - 1)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        n = int(f.readline())    
    # Calculate result
    result = recursive_factorial(n)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main() 