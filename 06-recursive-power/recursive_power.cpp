#include <iostream>
#include <fstream>
using namespace std;

double recursivePower(double x, int n) {
    // Base case
    if (n == 0) {
        return 1;
    }
    
    // Handle negative exponent
    if (n < 0) {
        return 1 / recursivePower(x, -n);
    }
    
    // Recursive case for even exponent
    if (n % 2 == 0) {
        double temp = recursivePower(x, n / 2);
        return temp * temp;
    }
    
    // Recursive case for odd exponent
    double temp = recursivePower(x, n / 2);
    return x * temp * temp;
}

int main() {
    // Read input
    ifstream inFile("input.txt");
    double x;
    int n;
    inFile >> x >> n;
    inFile.close();
    
    // Calculate result
    double result = recursivePower(x, n);
    
    // Write output
    ofstream outFile("output.txt");
    outFile << result << endl;
    
    return 0;
} 