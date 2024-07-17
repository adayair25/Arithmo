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
