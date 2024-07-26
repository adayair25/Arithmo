from lark import Transformer, v_args

@v_args(inline=True)  # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    from methods.Derivate.Derivative_general import derivative_general

    number = int  # NO COMENT THIS LINE

    def __init__(self):
        self.vars = {}

    #def assign_dev(self, dev, value):
     #   self.vars[dev] = value

    def assign_var(self, var, value):
       self.vars[var] = value
       return value

    def var(self, var):
        try:
            return self.vars[var]
        except KeyError:
            raise Exception("Variable not found: %s" % var)