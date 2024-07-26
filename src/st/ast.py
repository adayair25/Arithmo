from lark import Transformer, v_args

@v_args(inline=True)  # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg

    number = int  # NO COMENT THIS LINE

    #def concat(self, args):
     #   return f"{args}"

    def __init__(self):
        self.vars = {}

    def assign_var(self, var, value):
        self.vars[var] = value
        return value
    
    def show_var(self, var):
        return self.vars[var]

    def var(self, var):
        try:
            return self.vars[var]
        except KeyError:
            raise Exception("Variable not found: %s" % var)