TOKENS = [
    ("VAR", r"var"),  # variable declaration
    ("FUNCTION", r"fn"),  # function declaration
    ("IF", r"if\s"),  # if statement
    ("MODES", r"(\"sum\"|\"product\"|\"quotient\"|\"chain\")"),  # derivative general mode
    ("FUNCTION_EXP", r"(\"sin\"|\"cos\"|\"tan\"|\"cot\"|\"csc\"|\"sec\"|\"exp\"|\"log\")"),  # search for sin, cos, tan, exp, log, sqrt
    ("CONSTANTS", r"constants"),
    ("FUNCTIONS_CALL", r"deriv_gen"),  # derivative general function call
    ("STRING", r"\"t\""),  # search for string
    ("ELSE", r"else\s"),  # else statement
    ("WHILE", r"while\s"),  # while statement
    ("FOR", r"for\s"),  # for statement
    ("DO", r"do\s"),  # do statement
    ("BREAK", r"break\s"),  # break statement
    ("CASE", r"case\s"),  # case statement
    ("SWITCH", r"switch\s"),  # switch statement
    ("CONTINUE", r"continue"),  # continue statement
    ("PRINT", r"print"),  # print statement
    ("LPAREN", r"\("),  # search for (
    ("RPAREN", r"\)"),  # search for )
    ("LBRACE", r"\{\s"),  # search for {
    ("RBRACE", r"\}"),  # search for }
    ("LBRACKET", r"\["),  # search for [
    ("RBRACKET", r"\]"),  # search for ]
    ("COMMA", r","),  # search for ,
    ("RETURN", r"return"),  # return statement
    ("COLON", r":"),  # search for :
    ("TYPES", r"(srg|int|flt|dbl|bool)"),  # search for int, float, double, bool
    ("INT", r"\d+"),  # search for integer
    ("BOOLEAN", r"\b(true|false)\b"),  # search for true, false
    ("GREATER", r">"),  # search for >
    ("LESS", r"<"),  # search for <
    ("EQUALITY", r"="),  # search for =
    ("DOUBLE_EQUAL", r"=="),  # search for ==
    ("INEQUALITY", r"!="),  # search for !=
    ("GREATER_EQUAL", r">="),  # search for >=
    ("LESS_EQUAL", r"<="),  # search for <=
    ("PLUS", r"\+"),  # search for +
    ("MULTIPLY", r"\*"),  # search for *
    ("DIVIDE", r"/"),  # search for /
    ("MINUS", r"-"),  # search for -
    ("AND", r"&&"),  # search for &&
    ("OR", r"\|\|"),  # search for ||
    ("NOT", r"!"),  # search for !
    ("EXPONENT", r"\^"),  # search for ^
    ("REMAINDER", r"%"),  # search for %
    ("PLUS_DOUBLE", r"\+\+"),  # search for ++
    ("VALUE", r"\".*?\"|\d+(\.\d+)?"),  # search for value
    ("SEMICOLON", r";"),  # search for ;
    ("IDENTIFIER", r"\w+"),  # search for variable name without spaces
]

# Transform the tokens into a dictionary
TOKENS = dict(TOKENS)
