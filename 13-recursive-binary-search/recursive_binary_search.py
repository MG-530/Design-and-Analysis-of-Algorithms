def recursive_binary_search(arr: list[int], target: int, left: int, right: int) -> int:
    # Base case
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        target = int(lines[2])
    
    # Search
    result = recursive_binary_search(arr, target, 0, n - 1)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()