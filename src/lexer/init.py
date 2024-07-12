from lexer import Lexer

print("Hello, world from Arithmo!)")

# Test the lexer function
test = "for (var i: int = 0; i < 10; i++) { print(i);})"

lexer = Lexer()

tokens = lexer.tokenize(test)

print(tokens) 