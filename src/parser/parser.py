from lark import Lark #type: ignore
import sys
sys.path.append('src/lexer')

from lexer import Lexer

lexer = Lexer()
testcode = "Hello, world!"
tokens = lexer.tokenize(testcode)

#print(*[token[1].strip() for token in tokens], sep=" ")

"""
string = ""
for token in tokens:
   if token != " ":
        
    string += token[1]

print(string, sep=" ")
"""
l = Lark('''start:WORD","WORD"!"

            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
         ''')

print( l.parse("hello, world!") )