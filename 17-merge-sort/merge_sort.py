def merge(arr: list[int], left: int, mid: int, right: int):
    # Create temporary arrays for left and right subarrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge the temporary arrays back into arr[left..right]
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr, if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr, if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr: list[int], left: int, right: int):
    if left < right:
        mid = left + (right - left) // 2
        
        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
    
    # Sort
    merge_sort(arr, 0, n - 1)
    
    # Write output
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()