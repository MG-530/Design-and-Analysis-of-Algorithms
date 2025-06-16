#include <iostream>
#include <fstream>
#include <vector>

void merge(std::vector<int>& arr, int left, int mid, int right) {
    // Create temporary arrays for left and right subarrays
    std::vector<int> leftArr(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> rightArr(arr.begin() + mid + 1, arr.begin() + right + 1);
    
    int i = 0, j = 0, k = left;
    
    // Merge the temporary arrays back into arr[left..right]
    while (i < leftArr.size() && j < rightArr.size()) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    
    // Copy remaining elements of leftArr[], if any
    while (i < leftArr.size()) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    
    // Copy remaining elements of rightArr[], if any
    while (j < rightArr.size()) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        
        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int n;
    input >> n;
    
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        input >> arr[i];
    }
    input.close();
    
    // Sort
    mergeSort(arr, 0, n - 1);
    
    // Write output
    std::ofstream output("output.txt");
    for (int i = 0; i < n; i++) {
        output << arr[i];
        if (i < n - 1) output << " ";
    }
    output.close();
    
    return 0;
}