def recursive_sum(n: int) -> int:
    # Base case
    if n == 1:
        return 1
    
    # Recursive case
    return n + recursive_sum(n - 1)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        n = int(f.readline())
    
    # Calculate result
    result = recursive_sum(n)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main() 