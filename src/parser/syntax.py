from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS

SYNTAX = f""" 
    ?start: (deriv_gen | set_var | show_var)
    
    ?set_var: VAR IDENTIFIER EQUAL (VALUE | deriv_gen ) SEMICOLON
    ?deriv_gen: FUNCTIONS_CALL LPAREN MODES COMMA IDENTIFIER? COMMA (LIST_POLY | FUNCTION_EXP) COMMA? (LIST_POLY | FUNCTION_EXP)? COMMA? (CONSTANTS LIST_POLY)? RPAREN SEMICOLON
    ?show_var: IDENTIFIER SEMICOLON

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
    LIST_POLY: /{TOKENS["LIST_POLY"]}/
    
    %import common.WS_INLINE
    %ignore WS_INLINE
    %ignore " "
"""