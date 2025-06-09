#include <iostream>
#include <fstream>
using namespace std;

int recursiveSum(int n) {
    // Base case
    if (n == 1) {
        return 1;
    }
    
    // Recursive case
    return n + recursiveSum(n - 1);
}

int main() {
    // Read input
    ifstream input("input.txt");
    int n;
    input >> n;
    input.close();
    
    // Calculate result
    int result = recursiveSum(n);
    
    // Write output
    ofstream outFile("output.txt");
    outFile << result << endl;
    
    return 0;
} 