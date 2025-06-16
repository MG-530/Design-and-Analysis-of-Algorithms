def interpolation_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # If array has only one element
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Calculate position using interpolation formula
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        if arr[pos] == target:
            return pos
        
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1  # Not found

def main():
    # Read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        target = int(lines[2])
    
    # Search
    result = interpolation_search(arr, target)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()