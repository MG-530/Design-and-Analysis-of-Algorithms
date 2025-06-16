# 🚀 Design and Analysis of Algorithms

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-17+-red.svg)](https://en.cppreference.com/)
[![Rust](https://img.shields.io/badge/Rust-Latest-orange.svg)](https://www.rust-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive collection of fundamental algorithms implemented in **Python**, **C++**, and **Rust**. This repository serves as a learning resource, reference guide, and comparative study of algorithmic implementations across three popular programming languages.

## 📚 Implemented Algorithms

### 🧮 Mathematical & Arithmetic Algorithms
| # | Algorithm | Description | Time Complexity | Space Complexity |
|---|-----------|-------------|----------------|------------------|
| 1 | **Strassen's Algorithm** | Fast matrix multiplication using divide-and-conquer | O(n<sup>2.807</sup>) | O(n²) |
| 2 | **Polynomial Product** | Multiplication of two polynomials | O(n<sup>1.58</sup>) | O(n log n) |
| 3 | **Big Number Product** | Multiplication of arbitrarily large numbers | O(n<sup>1.58</sup>) | O(n log n) |
| 4 | **Sum 1 to n (Recursive)** | Calculate sum of integers from 1 to n | O(n) | O(n) |
| 5 | **Factorial (Recursive)** | Calculate factorial of a number | O(n) | O(n) |
| 6 | **Power (Recursive)** | Calculate x^n using recursion | O(log n) | O(log n) |
| 7 | **Quotient (Recursive)** | Division using repeated subtraction | O(a/b) | O(a/b) |
| 8 | **Remainder (Recursive)** | Modulo operation using recursion | O(a/b) | O(a/b) |
| 9 | **GCD (Recursive)** | Greatest Common Divisor using Euclidean algorithm | O(log min(a,b)) | O(log min(a,b)) |
| 10 | **Combination (Recursive)** | Calculate nCr combinatorially | O(2^n) | O(n) |

### 🏗️ Problem Solving
| # | Algorithm | Description | Time Complexity | Space Complexity |
|---|-----------|-------------|----------------|------------------|
| 11 | **Hanoi Tower** | Classic recursive puzzle solver | O(2^n) | O(n) |

### 🔍 Search Algorithms
| # | Algorithm | Description | Time Complexity | Space Complexity |
|---|-----------|-------------|----------------|------------------|
| 12 | **Binary Search** | Iterative search in sorted array | O(log n) | O(1) |
| 13 | **Binary Search (Recursive)** | Recursive search in sorted array | O(log n) | O(log n) |
| 14 | **Interpolation Search** | Enhanced search for uniformly distributed data | O(log log n) avg, O(n) worst | O(1) |

### 📊 Array Processing
| # | Algorithm | Description | Time Complexity | Space Complexity |
|---|-----------|-------------|----------------|------------------|
| 15 | **Min & Max (Linear)** | Find minimum and maximum in array | O(n) | O(1) |
| 16 | **Min & Max (Partitioning)** | Divide-and-conquer approach | O(n) | O(log n) |

### 📊 Sort Algorithms
| # | Algorithm | Description | Time Complexity | Space Complexity |
|---|-----------|-------------|----------------|------------------|
| 17 | **Merge Sort** | Stable, divide-and-conquer sorting algorithm | O(n log n) | O(n) |
| 18 | **Quick Sort** | Efficient divide-and-conquer sorting algorithm | O(n log n) avg, O(n²) worst | O(log n) |


## 🏗️ Repository Structure

Each algorithm is implemented in its own directory with the following structure:
```
algorithm-name/
├── algorithm_name.py    # Python implementation
├── algorithm_name.cpp   # C++ implementation
├── algorithm_name.rs    # Rust implementation
├── input.txt           # Example input
├── output.txt          # Example output
└── README.md           # Algorithm documentation
```

## 🛠️ Prerequisites & Setup

### Required Software
- **Python 3.8+** with standard library
- **C++ compiler** supporting C++17 (GCC 7+, Clang 10+, MSVC 2019+)
- **Rust** latest stable version (1.60+)

### Installation Commands
```bash
# Install Python (if not already installed)
# Ubuntu/Debian: sudo apt install python3 python3-pip
# macOS: brew install python3
# Windows: Download from python.org

# Install C++ compiler
# Ubuntu/Debian: sudo apt install build-essential
# macOS: xcode-select --install
# Windows: Install Visual Studio Community

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
```

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/MG-530/Design-and-Analysis-of-Algorithms
cd Design-and-Analysis-of-Algorithms
```

### Running Individual Algorithms

#### Python
```bash
cd 01-strassen/
python3 strassen.py
```

#### C++
```bash
cd 01-strassen/
g++ -std=c++17 -O2 strassen.cpp -o strassen
./strassen
```

#### Rust
```bash
cd 01-strassen/
rustc strassen.rs -O
./strassen
```

## 📈 Performance Comparison

Each algorithm folder includes benchmarking information comparing:
- **Execution Time** across languages
- **Memory Usage** patterns
- **Code Complexity** and readability
- **Optimization Opportunities**

## 🎯 Learning Objectives

This repository helps you understand:

### Algorithm Design Patterns
- **Divide and Conquer** (Strassen, Min/Max Partitioning)
- **Recursion** (Factorial, GCD, Hanoi Tower)
- **Iteration vs Recursion** (Binary Search variants)
- **Mathematical Optimization** (Fast exponentiation)

### Language-Specific Features
- **Python**: Clean syntax, built-in big integers, list comprehensions
- **C++**: Memory management, templates, STL containers
- **Rust**: Memory safety, ownership system, pattern matching

### Complexity Analysis
- Time complexity comparison
- Space complexity trade-offs
- Best/Average/Worst case scenarios

## 🔍 Algorithm Categories Explained

### Recursive Algorithms
Most algorithms demonstrate recursive thinking:
- Base case identification
- Recursive case formulation
- Stack space considerations
- Tail recursion optimization

### Mathematical Algorithms
Focus on numerical computation:
- Integer arithmetic operations
- Polynomial mathematics
- Matrix operations
- Number theory concepts

### Search Algorithms
Different approaches to finding elements:
- Linear search baseline
- Binary search optimization
- Interpolation search enhancement
- Complexity trade-offs

## 📖 Documentation Standards

Each algorithm folder contains:

### README.md Structure
* **Algorithm Name and Description**: A clear title and a brief explanation of the algorithm's purpose.
* **Time and Space Complexity**: The Big O notation for the algorithm's time and space requirements.
* **How it Works**: A detailed explanation of the methodology, including mathematical formulas or step-by-step logic.
* **Input and Output Format**: A description of the expected format for `input.txt` and `output.txt` files.
* **Example**: A concrete example of input and its corresponding output.
* **Implementation Notes**: Language-agnostic details about the implementation, such as the base case for recursion or data structures used.

### Code Standards
- **Comprehensive Comments**: Explaining logic and complexity
- **Test Cases**: Multiple scenarios with expected outputs
- **Error Handling**: Robust input validation
- **Consistent Naming**: Clear variable and function names

## 🎓 Educational Use

### For Students
- Learn algorithm design principles
- Compare programming language paradigms
- Understand complexity analysis
- Practice implementation skills

### For Educators
- Ready-to-use teaching materials
- Cross-language comparison examples
- Performance analysis demonstrations
- Homework/project foundations

### For Professionals
- Interview preparation resource
- Algorithm reference guide
- Performance optimization examples
- Code quality standards

## 🤝 Contributing

We welcome contributions! Here's how to help:

### Types of Contributions
1. **Bug Fixes**: Correct implementation errors
2. **Optimizations**: Improve algorithm efficiency
3. **Documentation**: Enhance explanations and examples
4. **Benchmarking**: Performance analysis improvements

## 📊 Benchmark Results

soon...

## 📄 License

This project is licensed under the **MIT License** 

```
MIT License - Free for educational and commercial use
- ✅ Use for any purpose
- ✅ Modify and distribute
- ✅ Private and commercial use
- ❗ Include license notice
```
---

### 🌟 Star this Repository!

If you find this resource helpful, please give it a star ⭐ and share it with others!

**Happy Coding and Learning! 🚀**

---

*Last Updated: June 2025 | Version 1.0.0*