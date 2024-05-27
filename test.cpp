#include <iostream>
#include <vector>
#include <map>

// Abstract base class for operations
class Operation {
public:
    virtual double execute(double a, double b) = 0; // Pure virtual function
};

// Derived class for addition
class Addition : public Operation {
public:
    double execute(double a, double b) override {
        return a + b;
    }
};

// Derived class for subtraction
class Subtraction : public Operation {
public:
    double execute(double a, double b) override {
        return a - b;
    }
};

// Derived class for multiplication
class Multiplication : public Operation {
public:
    double execute(double a, double b) override {
        return a * b;
    }
};

// Derived class for division
class Division : public Operation {
public:
    double execute(double a, double b) override {
        if (b != 0)
            return a / b;
        else {
            std::cerr << "Error: Division by zero!" << std::endl;
            return 0;
        }
    }
};

int main() {
    std::map<char, Operation*> operations; // Using STL map to store operations
    operations['+'] = new Addition();
    operations['-'] = new Subtraction();
    operations['*'] = new Multiplication();
    operations['/'] = new Division();

    char op;
    double num1, num2;
    std::vector<double> results; // Using STL vector to store results

    std::cout << "Simple Calculator\n";
    std::cout << "Enter 'q' to quit.\n";

    while (true) {
        std::cout << "Enter operation (+, -, *, /) or 'q' to quit: ";
        std::cin >> op;

        if (op == 'q')
            break;

        if (operations.find(op) == operations.end()) {
            std::cout << "Invalid operation!\n";
            continue;
        }

        std::cout << "Enter first number: ";
        std::cin >> num1;
        std::cout << "Enter second number: ";
        std::cin >> num2;

        double result = operations[op]->execute(num1, num2);
        results.push_back(result); // Store the result in the vector
        std::cout << "Result: " << result << std::endl;
    }

    std::cout << "\nCalculation history:\n";
    for (double res : results) {
        std::cout << res << std::endl;
    }

    // Clean up dynamic memory
    for (auto& pair : operations) {
        delete pair.second;
    }

    return 0;
}
