from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS
from lark import Transformer, v_args

SYNTAX = f""" 
    ?start: exp+

    ?exp: sum
      | NAME "=" sum -> assign
      | join -> concat
    ?var: VAR NAME "=" sum
    ?join: "join" LPAREN NAME+ RPAREN

    ?sum: prod 
      | sum "+" prod -> add
      | sum "-" prod -> sub 

    ?prod: atom
      | prod "*" atom -> mul
      | prod "/" atom -> div

    ?atom: NUMBER -> number
      | "-" atom -> neg
      | var NAME -> variable
      | "(" sum ")"
    
    
    VAR: /{TOKENS["VAR"]}/
    COMMA: /{TOKENS["COMMA"]}/
    LPAREN: /{TOKENS["LPAREN"]}/
    RPAREN: /{TOKENS["RPAREN"]}/
    NAME: /{TOKENS["IDENTIFIER"]}/
    NUMBER: /{TOKENS["VALUE"]}/
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = int

    def __init__(self):
        self.vars = {}

    def join (self, *args):
        return args
    
    def assign_var(self, name, value):
        self.vars[name] = value
        return value
    
    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)

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