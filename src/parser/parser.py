from lark import Lark

class Parser:
    #def __init__(self, syntax, calculate_tree):
    def __init__(self, syntax):
        self.parser = Lark(syntax, ambiguity="explicit")#parser='lalr', start="start") # Crea el analizador sintáctico
    def parsing(self, tokens):
        return self.parser.parse(''.join(token[1] for token in tokens))#.pretty() # Return the parse tree
    