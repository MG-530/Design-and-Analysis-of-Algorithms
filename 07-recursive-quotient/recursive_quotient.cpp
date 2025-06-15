#include <iostream>
#include <fstream>
using namespace std;

int recursiveQuotient(int a, int b) {
    // Handle negative numbers
    if (a < 0 && b < 0) {
        return recursiveQuotient(-a, -b);
    }
    else if (a < 0) {
        return -recursiveQuotient(-a, b);
    }
    else if (b < 0) {
        return -recursiveQuotient(a, -b);
    }
    
    // Base case
    if (a < b) {
        return 0;
    }
    
    // Recursive case
    return 1 + recursiveQuotient(a - b, b);
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int a, b;
    input >> a >> b;
    input.close();
    
    // Calculate result
    int result = recursiveQuotient(a, b);
    
    // Write output
    ofstream outFile("output.txt");
    outFile << result << endl;
    
    return 0;
} 