from lexer.lexer import Lexer # Import the lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser # Import the parser
from parser.syntax import SYNTAX # Import the list of SYNTAX

lexer = Lexer() # Create a lexer object
lexer.add_token(TOKENS) # Add the tokens to the lexer

route = 'src/input_files/input.ar'
input_string = lexer.tokenize_file(route)

for key in TOKENS.keys():
    if key == input_string[0][0]:
        parser = Parser(SYNTAX[key])
        break
    
print(parser.parsing(input_string)) # Parse the tokens
