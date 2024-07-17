from lexer.lexer import Lexer # Import the lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser # Import the parser
from parser.syntax import SYNTAX # Import the list of SYNTAX

#testcode = "var i: int = 000000007654.2345678;" # Test object code

lexer = Lexer() # Create a lexer object
lexer.add_token(TOKENS) # Add the tokens to the lexer
#tokens = lexer.tokenize(testcode) # Tokenize the test code
parser = Parser(SYNTAX["STATEMENT_WITH_TYPE"]) # Create a parser object


route = 'src/input_files/input.ar'
input_string = lexer.tokenize_file(route)
print(parser.parsing(input_string)) # Parse the tokens
