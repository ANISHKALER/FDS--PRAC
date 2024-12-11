#include <iostream>
#include <stack>
#include <string>
#include <cctype>  // for isalpha and tolower

using namespace std;

// Function to print the original and reversed string using a stack
void printReversedString(const string &str) {
    stack<char> s;
    string cleanedStr = "";

    // Clean the string: remove non-alphabetic characters and convert to lowercase
    for (char ch : str) {
        if (isalpha(ch)) {
            cleanedStr += tolower(ch);
        }
    }

    // Push characters to the stack
    for (char ch : cleanedStr) {
        s.push(ch);
    }

    // Print original cleaned string
    cout << "Original string (cleaned): " << cleanedStr << endl;

    // Print reversed string by popping from the stack
    cout << "Reversed string: ";
    while (!s.empty()) {
        cout << s.top();
        s.pop();
    }
    cout << endl;
}

// Function to check if a string is a palindrome
bool isPalindrome(const string &str) {
    stack<char> s;
    string cleanedStr = "";

    // Clean the string: remove non-alphabetic characters and convert to lowercase
    for (char ch : str) {
        if (isalpha(ch)) {
            cleanedStr += tolower(ch);
        }
    }

    // Push characters to the stack
    for (char ch : cleanedStr) {
        s.push(ch);
    }

    // Check if the string matches when reversed
    for (char ch : cleanedStr) {
        if (ch != s.top()) {
            return false;
        }
        s.pop();
    }

    return true;
}

// Function to check if parentheses are balanced using a stack
bool areParenthesesBalanced(const string &expr) {
    stack<char> s;

    for (char ch : expr) {
        if (ch == '(' || ch == '[' || ch == '{') {
            s.push(ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (s.empty()) return false;

            char top = s.top();
            if ((ch == ')' && top == '(') || (ch == ']' && top == '[') || (ch == '}' && top == '{')) {
                s.pop();
            } else {
                return false;
            }
        }
    }

    return s.empty();
}

// Menu function to check palindrome
void palindromeMenu() {
    string input;
    cout << "Enter a string to check if it's a palindrome: ";
    cin.ignore();
    getline(cin, input);

    printReversedString(input);  // Print original and reversed
    if (isPalindrome(input)) {
        cout << "The string is a palindrome!" << endl;
    } else {
        cout << "The string is not a palindrome!" << endl;
    }
}

// Menu function to check balanced parentheses
void parenthesesMenu() {
    string expr;
    cout << "Enter an expression to check for balanced parentheses: ";
    cin.ignore();
    getline(cin, expr);

    if (areParenthesesBalanced(expr)) {
        cout << "The parentheses are balanced!" << endl;
    } else {
        cout << "The parentheses are NOT balanced!" << endl;
    }
}

int main() {
    int choice;

    do {
        cout << "\nMenu: ";
        cout << "1. Check Palindrome\n";
        cout << "2. Check Balanced Parentheses\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                palindromeMenu();
                break;
            case 2:
                parenthesesMenu();
                break;
            case 3:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
    } while (choice != 3);

    return 0;
}
