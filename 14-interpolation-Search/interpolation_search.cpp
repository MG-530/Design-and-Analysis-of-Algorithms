#include <iostream>
#include <fstream>
#include <vector>

int interpolationSearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right && target >= arr[left] && target <= arr[right]) {
        // If array has only one element
        if (left == right) {
            if (arr[left] == target) return left;
            return -1;
        }
        
        // Calculate position using interpolation formula
        int pos = left + ((double)(target - arr[left]) / (arr[right] - arr[left])) * (right - left);
        
        if (arr[pos] == target) {
            return pos;
        }
        
        if (arr[pos] < target) {
            left = pos + 1;
        } else {
            right = pos - 1;
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
    int result = interpolationSearch(arr, target);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
}