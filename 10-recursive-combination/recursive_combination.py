def recursive_combination(n: int, k: int) -> int:
    # Base cases
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    
    # Recursive case
    return recursive_combination(n-1, k-1) + recursive_combination(n-1, k)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        n, k = map(int, f.read().strip().split())
    
    # Calculate combination
    result = recursive_combination(n, k)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main() 