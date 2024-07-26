from lexer.lexer import Lexer  # Import the lexer
from lexer.tokens import TOKENS  # Import the list of TOKENS
from parser.parser import Parser  # Import the parser
from parser.syntax import SYNTAX  # Import the list of SYNTAX
from st.ast import CalculateTree
from input_files.validation import Validation  # Import the input file validation

lexer = Lexer()  # Create a lexer object
lexer.add_token(TOKENS)  # Add the tokens to the lexer

directory = "src/input_files"
input_file = Validation(directory)
content = input_file.read_files()
tokens = lexer.tokenize(content)
parser = Parser(SYNTAX, CalculateTree())

print(parser.parsing(tokens))  # TEST CODE 

"""
parser = None
for key in TOKENS.keys():
    if key == tokens[0][0]:
        parser = Parser(SYNTAX[key])
        break

print(parser.parsing(tokens))  # Parse the tokens
"""
