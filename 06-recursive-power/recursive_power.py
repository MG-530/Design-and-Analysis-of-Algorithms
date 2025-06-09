def recursive_power(x: float, n: int) -> float:
    # Base case
    if n == 0:
        return 1
    
    # Handle negative exponent
    if n < 0:
        return 1 / recursive_power(x, -n)
    
    # Recursive case for even exponent
    if n % 2 == 0:
        temp = recursive_power(x, n // 2)
        return temp * temp
    
    # Recursive case for odd exponent
    temp = recursive_power(x, n // 2)
    return x * temp * temp

def main():
    # Read input
    with open('input.txt', 'r') as f:
        x = float(f.readline().strip())
        n = int(f.readline().strip())
    
    # Calculate result
    result = int(recursive_power(x, n))
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main() 