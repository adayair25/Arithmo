from lexer.tokens import TOKENS # Import the list of TOKENS

SYNTAX = {
    'STATEMENT_WITH_TYPE': f'''
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
       ''',
    'STATEMENT_WITHOUT_TYPE': f'''
         start: declaration
         declaration: VAR IDENTIFIER EQUALITY VALUE SEMICOLON

         VAR: /{TOKENS['VAR']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         COLON: /{TOKENS['COLON']}/
         TYPES: /{TOKENS['TYPES']}/
         EQUALITY: /{TOKENS['EQUALITY']}/
         VALUE: /{TOKENS['VALUE']}/
         SEMICOLON: /{TOKENS['SEMICOLON']}/
         
         %ignore " "           // Disregard spaces in text
       ''',
    'FUNCTION': f'''
         start: declaration
         declaration: FUNCTION IDENTIFIER LPAREN RPAREN LBRACE RBRACE

         FUNCTION: /{TOKENS['FUNCTION']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         LPAREN: /{TOKENS['LPAREN']}/
         RPAREN: /{TOKENS['RPAREN']}/
         LBRACE: /{TOKENS['LBRACE']}/
         RBRACE: /{TOKENS['RBRACE']}/
         
         %ignore " "           // Disregard spaces in text
       '''
}