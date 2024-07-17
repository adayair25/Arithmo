from lexer.lexer import Lexer   # Import the lexer
from lexer.tokens import TOKENS   # Import the list of TOKENS
from parser.parser import Parser   # Import the parser
from parser.syntax import SYNTAX   # Import the list of SYNTAX

lexer = Lexer()  # Create a lexer object
lexer.add_token(TOKENS)  # Add the tokens to the lexer

directory = 'src/input_files'
tokens = lexer.tokenize_files_in_directory(directory)
for token in tokens:
    print(f"Tipo: {token[0]}, Valor: {token[1]}")

parser = None
for key in TOKENS.keys():
    if key == tokens[0][0]:
        parser = Parser(SYNTAX[key])
        break
print(parser.parsing(tokens))
