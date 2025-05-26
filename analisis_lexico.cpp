#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

struct Token {
    string type;
    string value;
};

bool isLetter(chat c) {
    return isalpha(c);
}

bool isDigit(char c) {
    return isdigit(c);
}

vector<Token> AnalizadorLexico(const string& input) {
}