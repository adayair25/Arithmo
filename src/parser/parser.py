from lark import Lark, Token

class Parser:
    def __init__(self, syntax):
        self.parser = Lark(syntax, parser='lalr') # Recibe la grámatica del lenguaje

    # Analiza la cadena o lista de tokens según la sintaxis
    def parsing(self, tokens):
        print(' '.join(token[1] for token in tokens))
        return self.parser.parse(''.join(token[1] for token in tokens)).pretty() # Devuelve el árbol de análisis
    