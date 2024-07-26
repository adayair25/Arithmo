from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS

SYNTAX = f""" 
    ?start: exp+

    ?exp: sum
      | VAR IDENTIFIER EQUAL sum SEMICOLON -> assign 

    ?var: IDENTIFIER SEMICOLON -> show_var


    ?sum: prod 
      | sum "+" prod -> add
      | sum "-" prod -> sub 

    ?prod: atom
      | prod "*" atom -> mul
      | prod "/" atom -> div

    ?atom: NUMBER -> number
      | "-" atom -> neg
      | VAR IDENTIFIER -> variable
      | "(" sum ")"
    
    
    VAR: /{TOKENS["VAR"]}/
    EQUAL: /{TOKENS["EQUALITY"]}/
    COMMA: /{TOKENS["COMMA"]}/
    LPAREN: /{TOKENS["LPAREN"]}/
    RPAREN: /{TOKENS["RPAREN"]}/
    IDENTIFIER: /{TOKENS["IDENTIFIER"]}/
    VALUE: /{TOKENS["VALUE"]}/
    NUMBER: /{TOKENS["VALUE"]}/
    SEMICOLON: /{TOKENS["SEMICOLON"]}/
    
    %import common.WS_INLINE
    %ignore WS_INLINE
    %ignore " "
"""

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