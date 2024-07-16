import os
from lexer.lexer import Lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser

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

file_path = r"C:\Users\frank\OneDrive\Documentos\Hackathon\Arithmo\src\input_files\input.ar"
print(f"Ruta del archivo: {file_path}")
print(f"Directorio actual: {os.getcwd()}")

try:
    input_string = lexer.read_file(file_path)
    print("Contenido del archivo:", input_string)  # Imprimir contenido para depuración
    tokens = lexer.tokenize(input_string)
    print("Tokens:", tokens)
    
    parser = Parser(syntax)
    result = parser.parsing(tokens)
    print("Parse Result:", result)

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")

try:
    # Lee el contenido del archivo
    input_string = lexer.read_file(file_path)
    # Tokeniza el contenido leído
    tokens = lexer.tokenize(input_string)
    print("Tokens:", tokens)
    
    parser = Parser(syntax)
    result = parser.parsing(tokens)
    print("Parse Result:", result)

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")