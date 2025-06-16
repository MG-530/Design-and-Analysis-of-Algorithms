#include <iostream>
#include <fstream>
#include <vector>

int partition(std::vector<int>& arr, int low, int high) {
    // Choose rightmost element as pivot
    int pivot = arr[high];
    
    // Index of smaller element (indicates right position of pivot)
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        // Partitioning index
        int pi = partition(arr, low, high);
        
        // Separately sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
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
    quickSort(arr, 0, n - 1);
    
    // Write output
    std::ofstream output("output.txt");
    for (int i = 0; i < n; i++) {
        output << arr[i];
        if (i < n - 1) output << " ";
    }
    output.close();
    
    return 0;
}