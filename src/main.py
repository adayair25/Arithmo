import os
from lexer.lexer import Lexer  # Import the lexer
from lexer.tokens import TOKENS  # Import the list of TOKENS
from parser.parser import Parser  # Import the parser
from parser.syntax import SYNTAX  # Import the list of SYNTAX
from st.ast import Interpreter # Interpreter
from input_files.validation import Validation  # Import the input file validation

lexer = Lexer()  # Create a lexer object
lexer.add_token(TOKENS)  # Add the tokens to the lexer

# BETA
"""
directory = "src/input_files" # Directory of the input files
input_file = Validation(directory)  
content = input_file.read_files()   
tokens = lexer.tokenize(content)
"""
# / BETA
parser = Parser(SYNTAX)

interpreter = Interpreter()

print('Arithmo 1.0.0 \n Type "help" for more information.')

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_help():
    help_message = """
    Documentation for Arithmo 1.0.0
    https://happy-pond-08b1f5d10.5.azurestaticapps.net/#more-about-arithmo
    """
    print(help_message)

while True:
        try:
            input_shell = input('> ')
            if input_shell == 'q':
                break
            elif input_shell == 'clear':
                clear_terminal()
            elif input_shell == 'help':
                show_help()
            else:
                tokens = lexer.tokenize(input_shell)
                parsing = parser.parsing(tokens)
                interpreter.get_result(parsing)
        except EOFError:
            break