def read_matrix(n, file):
    matrix = []
    for _ in range(n):
        row = list(map(int, file.readline().split()))
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen_multiply(A, B):
    n = len(A)
    
    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Divide matrices into quarters
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    # Calculate the seven products
    P1 = strassen_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))
    
    # Calculate the four quadrants of the result
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)
    
    # Combine the four quadrants
    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])
    for i in range(mid):
        result.append(C21[i] + C22[i])
    
    return result

def main():
    # Read input from file
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        A = read_matrix(n, f)
        B = read_matrix(n, f)
    
    # Calculate result
    result = strassen_multiply(A, B)
    
    # Write output
    with open('output.txt', 'w') as f:
        for row in result:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main() 