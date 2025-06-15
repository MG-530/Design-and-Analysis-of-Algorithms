def iterative_binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

def main():
    # Read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        target = int(lines[2])
    
    # Search
    result = iterative_binary_search(arr, target)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()