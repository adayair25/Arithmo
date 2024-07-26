from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS

SYNTAX = f""" 
    ?start: codeblock+
    ?codeblock: deriv_gen
    
    ?deriv_gen: FUNCTIONS_CALL LPAREN MODES COMMA STRING? COMMA ( ( ( LBRACKET (INT COMMA INT COMMA INT COMMA INT) RBRACKET ) | FUNCTION_EXP) COMMA ) ( ( ( LBRACKET (INT COMMA INT COMMA INT COMMA INT) RBRACKET ) | FUNCTION_EXP)) (CONSTANTS EQUAL LBRACKET (INT COMMA)+ RBRACKET)? RPAREN SEMICOLON
      
      | VAR IDENTIFIER EQUAL sum SEMICOLON -> assign 

    ?sum: prod 
      | sum "+" prod -> add
      | sum "-" prod -> sub 

    ?prod: atom
      | prod "*" atom -> mul
      | prod "/" atom -> div

    ?atom: INT -> number
      | "-" atom -> neg
      | VAR IDENTIFIER -> variable
      | "(" sum ")"
    
    
    VAR: /{TOKENS["VAR"]}/
    EQUAL: /{TOKENS["EQUALITY"]}/
    COMMA: /{TOKENS["COMMA"]}/
    LPAREN: /{TOKENS["LPAREN"]}/
    RPAREN: /{TOKENS["RPAREN"]}/
    LBRACKET: /{TOKENS["LBRACKET"]}/
    RBRACKET: /{TOKENS["RBRACKET"]}/
    MODES: /{TOKENS["MODES"]}/
    FUNCTIONS_CALL: /{TOKENS["FUNCTIONS_CALL"]}/
    FUNCTION_EXP: /{TOKENS["FUNCTION_EXP"]}/
    CONSTANTS: /{TOKENS["CONSTANTS"]}/
    STRING: /{TOKENS["STRING"]}/
    MULTIPLY: /{TOKENS["MULTIPLY"]}/
    IDENTIFIER: /{TOKENS["IDENTIFIER"]}/
    VALUE: /{TOKENS["VALUE"]}/
    INT: /{TOKENS["INT"]}/
    SEMICOLON: /{TOKENS["SEMICOLON"]}/
    
    %import common.WS_INLINE
    %ignore WS_INLINE
    %ignore " "
"""
# ?deriv_gen: "deriv_gen" LPAREN MODES COMMA (STRING)? COMMA ( (LBRACKET (INT COMMA)+ RBRACKET ) | FUNCTION_EXP )+ (CONSTANTS EQUAL LBRACKET (INT COMMA)+ RBRACKET)? -> derivative_general

'''
def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))


def test():
    print(calc("a = 1+2"))
    print(calc("1+a*-3"))


if __name__ == '__main__':
    # test()
    main()
'''    