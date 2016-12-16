The bogus dynamic library
In the attachment you can find a file named quadratic.dll. This is a dynamic link library
designed to solve quadratic equations.
It has the following interface:
void setA(const double a); sets the coefficient “a” of the equation
void setB(const double b); sets the coefficient “b” of the equation
void setC(const double c); sets the coefficient “c” of the equation
int getSolution(double * px1, double * px2);
calculates the solutions of the equation a*x*x + b*x + c = 0.
The return values of getSolution are defined by the following enum:
enum {
SOLUTION_OK = 0,
ERROR_A_IS_ZERO = 1,
ERROR_NO_REAL_ROOTS = 2
};
For example, if we call setA(1.0), setB(0), setC(-4.0), then getSolution will calculate
x1 = -2, x2 = 2 and return SOLUTION_OK.
Note that the quadratic.dll is highly unstable and sometimes delivers wrong results.
Perform manual and automated testing of this dynamic-link library. Find and describe as many bugs
in it as possible. For automated testing scripts use Python or Ruby.
Provide the list of bugs found and the test script used.

To run tests you need install required libraries "pip install requirements.txt"
Then "py.tets -s -q"
