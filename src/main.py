from lexer.lexer import Lexer

testcode = "for (var i: int = 0; i < 10; i++) { print(i);})"

lexer = Lexer()
tokens = lexer.tokenize(testcode)
print(tokens)