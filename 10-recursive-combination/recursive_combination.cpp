#include <iostream>
#include <fstream>

int recursiveCombination(int n, int k) {
    // Base cases
    if (k == 0 || k == n) {
        return 1;
    }
    if (k > n) {
        return 0;
    }
    
    // Recursive case
    return recursiveCombination(n-1, k-1) + recursiveCombination(n-1, k);
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int n, k;
    input >> n >> k;
    input.close();
    
    // Calculate combination
    int result = recursiveCombination(n, k);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
} 