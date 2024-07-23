from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS
from lark import Transformer, v_args
SYNTAX = """ 
    ?start: sum
      | NAME "=" sum -> assign

    ?sum: prod 
      | sum "+" prod -> add
      | sum "-" prod -> sub

    ?prod: atom
      | prod "*" atom -> mul
      | prod "/" atom -> div

    ?atom: NUMBER -> number
      | "-" atom -> neg
      | NAME -> var
      | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

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