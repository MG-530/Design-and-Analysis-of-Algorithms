#include <iostream>
#include <fstream>
using namespace std;

long long recursiveFactorial(int n) {
    // Base cases
    if (n == 0 || n == 1) {
        return 1;
    }
    
    // Recursive case
    return n * recursiveFactorial(n - 1);
}

int main() {
    // Read input
    ifstream input("input.txt");
    int n;
    input >> n;
    input.close();
    
    // Calculate result
    long long result = recursiveFactorial(n);
    
    // Write output
    ofstream outFile("output.txt");
    outFile << result << endl;
    
    return 0;
} 