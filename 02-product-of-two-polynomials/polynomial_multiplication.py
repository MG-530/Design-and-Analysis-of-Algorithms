def add_polynomials(a, b):
    max_len = max(len(a), len(b))
    result = [0] * max_len
    
    for i in range(max_len):
        if i < len(a):
            result[i] += a[i]
        if i < len(b):
            result[i] += b[i]
    
    return result

def subtract_polynomials(a, b):
    max_len = max(len(a), len(b))
    result = [0] * max_len
    
    for i in range(max_len):
        if i < len(a):
            result[i] += a[i]
        if i < len(b):
            result[i] -= b[i]
    
    return result

def multiply_polynomials(a, b):
    # Remove trailing zeros
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    
    if not a or not b:
        return [0]
    
    n, m = len(a), len(b)
    
    # Base case: small polynomials
    if n <= 2 or m <= 2:
        result = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                result[i + j] += a[i] * b[j]
        return result
    
    # Make both polynomials the same size (power of 2)
    max_size = max(n, m)
    new_size = 1
    while new_size < max_size:
        new_size *= 2
    
    # Pad with zeros
    a += [0] * (new_size - len(a))
    b += [0] * (new_size - len(b))
    
    half = new_size // 2
    
    # Split polynomials
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:half]
    b1 = b[half:]
    
    # Recursive calls
    p1 = multiply_polynomials(a1[:], b1[:])
    p2 = multiply_polynomials(a0[:], b0[:])
    p3 = multiply_polynomials(add_polynomials(a0, a1), add_polynomials(b0, b1))
    
    # Combine results
    result = [0] * (2 * new_size - 1)
    
    # p2 (constant term)
    for i in range(len(p2)):
        result[i] += p2[i]
    
    # p1 * x^n
    for i in range(len(p1)):
        result[i + 2 * half] += p1[i]
    
    # (p3 - p1 - p2) * x^(n/2)
    middle = subtract_polynomials(subtract_polynomials(p3, p1), p2)
    for i in range(len(middle)):
        result[i + half] += middle[i]
    
    # Remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return result

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    
    m = int(lines[2])
    b = list(map(int, lines[3].split()))
    
    result = multiply_polynomials(a, b)
    
    with open('output.txt', 'w') as f:
        f.write(str(len(result) - 1) + '\n')
        f.write(' '.join(map(str, result)))

if __name__ == "__main__":
    main()