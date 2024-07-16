from lexer.lexer import Lexer # Import the lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser # Import the parser
from parser.syntax import SYNTAX # Import the list of SYNTAX

testcode = "var i: int = 000000007654.2345678;" # Test object code

lexer = Lexer() # Create a lexer object
lexer.add_token(TOKENS) # Add the tokens to the lexer
tokens = lexer.tokenize(testcode) # Tokenize the test code
parser = Parser(SYNTAX) # Create a parser object
print(parser.parsing(tokens)) # Parse the tokens