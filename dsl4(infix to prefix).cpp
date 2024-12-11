#include <iostream>
#include <stack>
#include <cctype>  // for isdigit() function
#include <stdexcept>  // for exception handling
using namespace std;

// Function to return precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// Function to perform arithmetic operations
int applyOperation(int a, int b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': 
            if (b == 0) throw runtime_error("Divide by zero error.");
            return a / b;
    }
    return 0;
}

// Function to convert infix to postfix
string infixToPostfix(string infix) {
    stack<char> s;
    string postfix = "";

    for (char &ch : infix) {
        // If operand, add it to the postfix expression
        if (isalnum(ch))
            postfix += ch;

        // If opening parenthesis, push to stack
        else if (ch == '(')
            s.push(ch);

        // If closing parenthesis, pop until '(' is found
        else if (ch == ')') {
            while (!s.empty() && s.top() != '(') {
                postfix += s.top();
                s.pop();
            }
            s.pop();  // Remove '(' from stack
        }

        // If operator, pop all higher precedence operators and then push current operator
        else {
            while (!s.empty() && precedence(s.top()) >= precedence(ch)) {
                postfix += s.top();
                s.pop();
            }
            s.push(ch);
        }
    }

    // Pop all remaining operators in the stack
    while (!s.empty()) {
        postfix += s.top();
        s.pop();
    }

    return postfix;
}

// Function to evaluate a postfix expression
int evaluatePostfix(string postfix) {
    stack<int> s;

    for (char &ch : postfix) {
        // If operand, push to stack
        if (isdigit(ch))
            s.push(ch - '0');

        // If operator, pop two operands and apply the operation
        else {
            if (s.size() < 2) throw runtime_error("Invalid postfix expression.");
            int val2 = s.top(); s.pop();
            int val1 = s.top(); s.pop();
            int result = applyOperation(val1, val2, ch);
            s.push(result);
        }
    }

    if (s.size() != 1) throw runtime_error("Invalid postfix expression.");
    return s.top();  // The result is at the top of the stack
}

int main() {
    try {
        string infixExp;
        cout << "Enter infix expression: ";
        cin >> infixExp;

        string postfixExp = infixToPostfix(infixExp);
        cout << "Postfix Expression: " << postfixExp << endl;

        int result = evaluatePostfix(postfixExp);
        cout << "Evaluation Result: " << result << endl;
    } catch (const exception &e) {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}
