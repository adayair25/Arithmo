from lexer.tokens import TOKENS  # type: ignore # Import the list of TOKENS

SYNTAX = {
    "VAR": f"""
         ?start: code_block+
         ?code_block: set_var 
         
         ?set_var: VAR IDENTIFIER (COMMA IDENTIFIER)? COLON TYPES EQUALITY VALUE SEMICOLON | VAR IDENTIFIER EQUALITY VALUE SEMICOLON
      
         VAR: /{TOKENS['VAR']}/
         IDENTIFIER: /{TOKENS['IDENTIFIER']}/
         COLON: /{TOKENS['COLON']}/
         TYPES: /{TOKENS['TYPES']}/
         EQUALITY: /{TOKENS['EQUALITY']}/
         VALUE: /{TOKENS['VALUE']}/
         SEMICOLON: /{TOKENS['SEMICOLON']}/
          COMMA: /{TOKENS['COMMA']}/
         
         %ignore " "
       """,
    "FUNCTION": f""" 
         ?start: code_block+
         ?code_block: set_function
         
         ?set_function: FUNCTION IDENTIFIER LPAREN (IDENTIFIER (COMMA IDENTIFIER)+)? RPAREN LBRACE RBRACE SEMICOLON

          FUNCTION: /{TOKENS['FUNCTION']}/
          IDENTIFIER: /{TOKENS['IDENTIFIER']}/
          LPAREN: /{TOKENS['LPAREN']}/
          COMMA: /{TOKENS['COMMA']}/
          RPAREN: /{TOKENS['RPAREN']}/
          LBRACE: /{TOKENS['LBRACE']}/
          RBRACE: /{TOKENS['RBRACE']}/
          SEMICOLON: /{TOKENS['SEMICOLON']}/

           %ignore " "
         """,  # FUNCTION is BETA
}
