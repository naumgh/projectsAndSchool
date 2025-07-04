#include <iostream> // C++ standard library version: This project uses the standard library version.

int main()
{
    std::cout << "Hello, World!" << std::endl;
    std::cout << "std does not imply sexually transmitted disease, but rather the standard library in C++." << std::endl;
    // if returnd 0, the program executed successfully
    // if return 1, the program encountered an error

    // comments are completely ignored by the compiler, which means they are injectable in expressions
    //  declaration and assignment of a
    int a;
    a = 5;
    // declaration and assignment of b
    int b = 10;
    int sum = a + b;
    std::cout << "The sum of " << a << " and " << b << " is: " << sum << std::endl;

    int age = 24;
    int year = 2023;
    int days = 3.5; // Note: This will cause a warning since 'days' is declared as an int but assigned a float/double value.

    double pi = 3.14159; // Using double for more precision
    std::cout << "Age: " << age << ", Year: " << year << ", Days: " << days << ", Pi: " << pi << std::endl;

    double gpa = 2.15;         // GPA can be a floating-point number
    double temperature = 36.6; // Temperature can also be a floating-point number

    std::cout << pi;

    // single character
    char grade = 'A';
    char initial = 'J';

    char currency = '$';

    // boolean values(true or false)
    bool isPassed = true;
    bool isFailed = false;

    // string is a sequence of characters
    std::string name = "John Doe";
    std::cout << "Name: " << name;

    std::string day = "Monday";
    std::string food = "Pizza";
    std::string address = "123 Main St";

    std::cout << " Hello, " << name << initial << "\n";

    // the const ketword is used to declare a constant variable. it is readonly unmodifiable
    // lets calculate the area of a circle

    const double pi_const = 3.14159265358979323846;
    double radius = 6.0;
    double area = pi_const * radius * radius;
    std::cout << "The area of the circle with radius " << radius << " is: " << area << std::endl;

    // namespace provides a solution for preventing name conflicts in large projects. each entity needs a unique name. a namespace allows for
    // identically named entities as long as the namespaces are different.

    std::cout << "Value from first namespace: " << first::value << std::endl;

    return 0;
}

namespace first
{
    int value = 42;
}

namespace second
{
    int value = 4;
}