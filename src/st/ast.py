from lark import Transformer, v_args
@v_args(inline=True)  # Affects the signatures of the methods #
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg

    number = int  # NO COMENT THIS LINE
    
    def __init__(self):
        self.vars = {}

    @v_args(meta=True)
    def assign(self, meta, var, value):
        self.vars[var] = value
        return self.vars[var]

    def var(self, var):
        try:
            return self.vars[var]
        except KeyError:
            raise Exception("Variable not found: %s" % var)
        
"""
class Interpreter:
    def __init__(self) -> None:
        pass

    def get_result(self, tree):
        print(tree)
        method_name = tree.data # Obtiene la data (rule) del objeto Token
        method = getattr(self, method_name) # Obtiene el método del objeto Interpreter, dependiendo de "rule"
        return method(tree)
    
    def deriv_gen(self, tree):
        return print(derivative_general('sum','t',[2,2,2,3],'sin'))
    
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

"""
@v_args(meta=True)  # meta=True hace que se pase un objeto Meta a la función
class MyTransformer(Transformer):
    def start(self, meta, word1, comma, word2, exclamation):
        print(f"Meta info: line {meta.line}, column {meta.column}")
        return f"{word1} {word2}"

parser = Lark(grammar, parser='lalr', transformer=MyTransformer())
result = parser.parse("Hello, world!")
print(result)  # Output: Hello world


@v_args(meta=True): Configura el decorador para que pase un objeto Meta a la función transformadora.
def start(self, meta, word1, comma, word2, exclamation):: La función start ahora recibe meta como el primer argumento, seguido de los otros argumentos.
print(f"Meta info: line {meta.line}, column {meta.column}"): Imprime la información de línea y columna del objeto Meta.
Cuando se ejecuta el código, se imprimirá la información de la línea y columna donde se encuentra el nodo start en el texto original.

"""