from lexer.lexer import Lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser

testcode = "var i: int = 0;"

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
         
         %import common.WORD   // imports from terminal library
         %ignore " "           // Disregard spaces in text
       '''
#print(syntax)

lexer = Lexer()
lexer.add_token(TOKENS)
tokens = lexer.tokenize(testcode)
#print(tokens)
parser = Parser(syntax)
print(parser.parsing(tokens))