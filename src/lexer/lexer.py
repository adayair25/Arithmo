import re
import os
class Lexer:
    def __init__(self):
        self.tokens = []
    
    def add_token(self, tokens_list):
        for name, pattern in tokens_list.items(): # Unpack the token tuple
            self.tokens.append((name, re.compile(pattern))) # Compile the regular expression pattern

    def tokenize(self, input_string):
        tokens = []
        while len(input_string) > 0:
            match = None # Initialize match to None
            input_string = input_string.strip(" \n") # Remove leading whitespace
            for name, regex in self.tokens: 
                match = regex.match(input_string) # Match the pattern against the input string
                if match:
                    value = match.group() # Get the matched value
                    tokens.append((name, value)) # Append the token to the list
                    input_string = input_string[len(value):] # Remove the token from the input string
                    break
            if not match:
                print(f"Unexpected character: '{input_string[0]}'") # Added for debugging
                raise Exception(f'Error: unexpected character "{input_string[0]}" at position {len(input_string)}') # Raise an exception if an unexpected character is encountered
        return tokens # Return the list of tokens
    
