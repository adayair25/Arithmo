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
import os
from lexer.lexer import Lexer
from lexer.tokens import TOKENS


syntax = f'''
         start: declaration
         declaration: VAR IDENTIFIER COLON TYPES EQUALITY VALUE SEMICOLON

         VAR: /{TOKENS['VAR']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         COLON: /{TOKENS['COLON']}/
         TYPES: /{TOKENS['TYPES']}/
         EQUALITY: /{TOKENS['EQUALITY']}/
         VALUE: /{TOKENS['VALUE']}/
         SEMICOLON: /{TOKENS['SEMICOLON']}/

         %import common.WORD   // importa de la biblioteca terminal
         %ignore " "           // Ignorar espacios en el texto
       '''

lexer = Lexer()
lexer.add_token(TOKENS)
route = 'input_files/input.ar'
input_string = lexer.tokenize_file(route)

print(input_string)
