#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int iterativeBinarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Not found
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
    
    int target;
    input >> target;
    input.close();
    
    // Search
    int result = iterativeBinarySearch(arr, target);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
}
