from lexer.tokens import TOKENS # Import the list of TOKENS

SYNTAX = f'''
         start: declaration
         declaration: VAR IDENTIFIER COLON TYPES EQUALITY VALUE SEMICOLON

         VAR: /{TOKENS['VAR']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         COLON: /{TOKENS['COLON']}/
         TYPES: /{TOKENS['TYPES']}/
         EQUALITY: /{TOKENS['EQUALITY']}/
         VALUE: /{TOKENS['VALUE']}/
         SEMICOLON: /{TOKENS['SEMICOLON']}/
         
         %ignore " "           // Disregard spaces in text
       '''

