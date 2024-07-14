from lark import Lark #type: ignore

class Parser:
    def __init__(self, syntax):
        self.parser = Lark(syntax) # Recibe la grámatica del lenguaje

    # Analiza la cadena o lista de tokens según la sintaxis
    def parsing(self, tokens):
        return self.parser.parse(''.join(token[1] for token in tokens))
    