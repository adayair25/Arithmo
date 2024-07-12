TOKENS = [
    ('VAR', r'var\s'), # variable declaration
    ('FUNCTION', r'fn\s'), # function declaration
    ('IF', r'if\s'), # if statement
    ('ELSE', r'else\s'), # else statement
    ('WHILE', r'while\s'), # while statement
    ('FOR', r'for\s'), # for statement
    ('DO', r'do\s'), # do statement
    ('BREAK', r'break\s'), # break statement
    ('CASE', r'case\s'), # case statement
    ('SWITCH', r'switch\s'), # switch statement
    ('CONTINUE', r'continue'), # continue statement
    ('PRINT', r'print'), # print statement
    ('LPAREN', r'\('), # search for (
    ('RPAREN', r'\)'), # search for )
    ('LBRACE', r'\{'), # search for {
    ('RBRACE', r'\}'), # search for }
    ('LBRACKET', r'\['), # search for [
    ('RBRACKET', r'\]'), # search for ]
    ('COMMA', r','), # search for ,
    ('RETURN', r'return'), # return statement
    #('INT', r'\d+'), # integer
    #('FLOAT', r'\d+\.\d+'),
    ('COLON', r':'), # search for :
    ('TYPES', r'\b(int|flt|dbl|bool)\b'), # search for int, float, double, bool              
    #('OPERATORS', r'\b(and|or|not)\b'), # search for and, or, not
    ('GREATER', r'>'), # search for >
    ('LESS', r'<'), # search for <
    ('DOUBLE_EQUAL', r'='), # search for =

    ('EQUALITY', r'=='), # search for ==
    ('INEQUALITY', r'!='), # search for !=
    ('GREATER_EQUAL', r'>='), # search for >=
    ('LESS_EQUAL', r'<='), # search for <=
    ('PLUS', r'\+'), # search for +
    ('MULTIPLY', r'\*'), # search for *
    ('DIVIDE', r'/'), # search for /
    ('MINUS', r'-'), # search for -
    ('AND', r'&&'), # search for &&
    ('OR', r'\|\|'), # search for ||
    ('NOT', r'!'), # search for !
    ('EXPONENT', r'\^'), # search for ^
    ('REMAINDER', r'%'), # search for %
    ('PLUS_DOUBLE', r'\+\+'), # search for ++
    #('IDENTIFIER', r'\b\w+\b'), # search for variable name
    ('VALUE', r'(\"\w+\"|\d*\.?\d+)'), # search for value
    ('SEMICOLON', r';'), # search for ;
    ('IDENTIFIER', r'(\w+)'), # search for variable name
    ('BOOLEAN', r'\b(true|false)\b'), # search for true, false

    # EXPERIMENTAL TOKENS
]