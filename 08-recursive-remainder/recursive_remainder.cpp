#include <iostream>
#include <fstream>
#include <cstdlib>

int recursiveRemainder(int a, int b) {
    // Handle negative numbers
    a = abs(a);
    b = abs(b);
    
    // Base case
    if (a < b) {
        return a;
    }
    
    // Recursive case
    return recursiveRemainder(a - b, b);
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int a, b;
    input >> a >> b;
    input.close();
    
    // Calculate remainder
    int result = recursiveRemainder(a, b);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
} 