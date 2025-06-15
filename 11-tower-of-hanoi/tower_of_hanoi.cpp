#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void tower_of_hanoi(int n, const std::string& source, const std::string& auxiliary, 
                 const std::string& destination, std::vector<std::string>& moves) {
    if (n == 1) {
        moves.push_back("Move disk from rod " + source + " to rod " + destination);
        return;
    }
    
    // Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary, moves);
    
    // Move nth disk from source to destination
    moves.push_back("Move disk from rod " + source + " to rod " + destination);
    
    // Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination, moves);
}

int main() {
    // Read input
    std::ifstream input("input.txt");
    int n;
    input >> n;
    input.close();
    
    // Solve Tower of Hanoi
    std::vector<std::string> moves;
    tower_of_hanoi(n, "A", "B", "C", moves);
    
    // Write output
    std::ofstream output("output.txt");
    for (const auto& move : moves) {
        output << move << std::endl;
    }
    output << "Total moves: " << moves.size();
    output.close();
    
    return 0;
} 