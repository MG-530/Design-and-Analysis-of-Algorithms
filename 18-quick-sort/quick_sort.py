def partition(arr: list[int], low: int, high: int) -> int:
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element (indicates right position of pivot)
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr: list[int], low: int, high: int):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)
        
        # Separately sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
    
    # Sort
    quick_sort(arr, 0, n - 1)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()