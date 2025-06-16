#include <iostream>
#include <fstream>
#include <vector>

int recursiveBinarySearch(const std::vector<int>& arr, int target, int left, int right) {
    // Base case
    if (left > right) {
        return -1;
    }
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;
    }
    
    if (arr[mid] < target) {
        return recursiveBinarySearch(arr, target, mid + 1, right);
    } else {
        return recursiveBinarySearch(arr, target, left, mid - 1);
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
    
    int target;
    input >> target;
    input.close();
    
    // Search
    int result = recursiveBinarySearch(arr, target, 0, n - 1);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
}