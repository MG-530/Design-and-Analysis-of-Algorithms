#include <iostream>
#include <fstream>
#include <cstdlib>

int recursiveGCD(int a, int b) {
    // Handle negative numbers
    a = abs(a);
    b = abs(b);
    
    // Base case
    if (b == 0) {
        return a;
    }
    
    // Recursive case
    return recursiveGCD(b, a % b);
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int a, b;
    input >> a >> b;
    input.close();
    
    // Calculate GCD
    int result = recursiveGCD(a, b);
    
    // Write output
    std::ofstream output("output.txt");
    output << result;
    output.close();
    
    return 0;
} 