from lexer.lexer import Lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser

testcode = "var i: int = 0;"

syntax = '''
         start: declaration
         declaration: VAR IDENTIFIER COLON TYPE EQUALITY VALUE SEMICOLON

         VAR: "var"
         IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
         COLON: ":"
         TYPE: "int" | "float" | "string"
         EQUALITY: "="
         VALUE: /\d+/
         SEMICOLON: ";"
         
         %import common.WORD   // imports from terminal library
         %ignore " "           // Disregard spaces in text
       '''

lexer = Lexer()
lexer.add_token(TOKENS)
tokens = lexer.tokenize(testcode)
#print(tokens)

parser = Parser(syntax)
print(parser.parsing(tokens))