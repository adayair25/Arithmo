from lark import Transformer, v_args
from methods.Derivate.Derivative_general import derivative_general as dev
class Interpreter:
    def __init__(self) -> None:
        pass

    def get_result(self, tree):
        print(tree)
        method_name = tree.data # Obtiene la data (rule) del objeto Token
        method = getattr(self, method_name) # Obtiene el método del objeto Interpreter, dependiendo de "rule"
        return method(tree)
    
    def deriv_gen(self, tree):
        mode = None
        functions = []
        variable = None

        for children in tree.children:
            if children.type == "MODES":
                mode = children.value
            elif children.type == "STRING":
                variable = children.value
            elif children.type == "FUNCTION_EXP":
                functions.append(children.value)

        return print(dev(mode, variable, functions[0], functions[1])) # 
    
    def set_var(self, tree): # Busca de entre los nodos, para asignar variables y valores
        variable_name = None
        assigned_value = None

        for children in tree.children:
            if children.type == "IDENTIFIER":
                variable_name = children.value
            elif children.type == "VALUE":
                assigned_value = children.value
        return variable_name, assigned_value

"""
@v_args(inline=True)  # Affects the signatures of the methods #
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg

    number = int  # NO COMENT THIS LINE

    def __init__(self):
        self.vars = {}

    def assign_var(self, var, value):
        self.vars[var] = value
        return value

    def var(self, var):
        try:
            return self.vars[var]
        except KeyError:
            raise Exception("Variable not found: %s" % var)

    dev(*vars)
"""