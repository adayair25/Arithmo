from lark import Lark, Token
from parser.syntax import CalculateTree

class Parser:
    def __init__(self, syntax):
        # self.parser = Lark(syntax, parser='lalr', start="start") # Recibe la grámatica del lenguaje
          self.parser = Lark(syntax, parser='lalr', transformer=CalculateTree())
    # Analiza la cadena o lista de tokens según la sintaxis
    #def parsing(self, tokens):
     #   return self.parser.parse(''.join(token[1] for token in tokens)).pretty() # Devuelve el árbol de análisis
    def parsing(self, text):
        return self.parser.parse(text)
    