from lexer.lexer import Lexer
from lexer.tokens import TOKENS # Import the list of TOKENS
from parser.parser import Parser
# testcode = "for (var i: int = 0; i < 10; i++) { print(i);})"

testcode = "Hello, world!"

syntax = '''start: WORD","WORD"!"

            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
         '''
#print(*[token[1] for token in tokens], sep="")

lexer = Lexer()
lexer.add_token(TOKENS)
tokens = lexer.tokenize(testcode)
print(tokens)

parser = Parser(syntax)
print(parser.parsing(tokens))