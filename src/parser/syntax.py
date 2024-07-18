from lexer.tokens import TOKENS #type: ignore # Import the list of TOKENS

SYNTAX = {
    'VAR': f'''
         start: code_block+
         code_block: set_var 
         
         set_var: VAR IDENTIFIER COLON TYPES EQUALITY VALUE SEMICOLON | VAR IDENTIFIER EQUALITY VALUE SEMICOLON
      
         VAR: /{TOKENS['VAR']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         COLON: /{TOKENS['COLON']}/
         TYPES: /{TOKENS['TYPES']}/
         EQUALITY: /{TOKENS['EQUALITY']}/
         VALUE: /{TOKENS['VALUE']}/
         SEMICOLON: /{TOKENS['SEMICOLON']}/
         
         %ignore " "           // Disregard spaces in text
       '''
}