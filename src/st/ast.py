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
        

class Interpreter:
    def __init__(self) -> None:
        pass

    def get_result(self, tree):
        print(tree)
        method_name = tree.data # Obtiene la data (rule) del objeto Token
        method = getattr(self, method_name) # Obtiene el método del objeto Interpreter, dependiendo de "rule"
        return method(tree)
    
    def set_var(self, tree): # Busca de entre los nodos, para asignar variables y valores
        variable_name = None
        assigned_value = None

        for children in tree.children:
            if children.type == "IDENTIFIER":
                variable_name = children.value
            elif children.type == "VALUE":
                assigned_value = children.value
        return variable_name, assigned_value