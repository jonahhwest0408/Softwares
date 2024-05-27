#include <iostream>  //input and output operations
#include <vector>    //using the vector container via STL
#include <map>       //using the map container via STL

//abstract base class for operations
class Operation {
public:
    virtual double execute(double a, double b) = 0; //pure virtual function
};

//derived class for addition
class Addition : public Operation {
public:
    double execute(double a, double b) override {
        return a + b; // Perform addition
    }
};

//derived class for subtraction
class Subtraction : public Operation {
public:
    double execute(double a, double b) override {
        return a - b; // Perform subtraction
    }
};

//derived class for multiplication
class Multiplication : public Operation {
public:
    double execute(double a, double b) override {
        return a * b; // Perform multiplication
    }
};

//derived class for division
class Division : public Operation {
public:
    double execute(double a, double b) override {
        if (b != 0)
            return a / b; //perform division
        else {
            std::cerr << "Error: Division by zero!" << std::endl; //error message
            return 0;
        }
    }
};

int main() {
    std::map<char, Operation*> operations; //using STL map to store operations
    operations['+'] = new Addition();      //add addition operation
    operations['-'] = new Subtraction();   //add subtraction operation
    operations['*'] = new Multiplication();//add multiplication operation
    operations['/'] = new Division();      //add division operation

    char op;
    double num1, num2;
    std::vector<double> results; //using STL vector to store results

    std::cout << "Simple Calculator\n"; //welcome message
    std::cout << "Enter 'q' to quit.\n"; //quit instruction

    int operation_count = 0; //count the number of operations

    while (true) {
        std::cout << "Enter operation (+, -, *, /) or 'q' to quit: ";
        std::cin >> op; //read operation

        if (op == 'q') //check for quit condition
            break;

        if (operations.find(op) == operations.end()) {
            std::cout << "Invalid operation! Valid operations are +, -, *, /.\n"; //invalid operation message
            continue;
        }

        std::cout << "Enter first number: ";
        std::cin >> num1; //read first number
        std::cout << "Enter second number: ";
        std::cin >> num2; //read second number

        double result = operations[op]->execute(num1, num2); //execute operation
        results.push_back(result); //store the result in the vector
        std::cout << "Result: " << result << std::endl; //print result
        operation_count++; //increment operation count
    }

    std::cout << "\nCalculation history:\n"; //print calculation history
    for (double res : results) {
        std::cout << res << std::endl; //print each result
    }

    std::cout << "Total operations performed: " << operation_count << std::endl; //print total operations

    //clean up dynamic memory
    for (auto& pair : operations) {
        delete pair.second; //delete each operation object
    }

    return 0; //end program
}
