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
    
    def tokenize_files_in_directory(self, directory_path):   # Verification that the directory exists
        if not os.path.isdir(directory_path):
            raise Exception('Error: directory does not exist')
        tokens = []
        for filename in os.listdir(directory_path):   # File extension verification
            if filename.endswith('.ar'):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as file:   # File reading
                    content = file.read().replace('\n', '')
                tokens.extend(self.tokenize(content))
        return tokens


"""
Tokenizes the input string by matching it against a list of predefined tokens.

Args:
    input_string (str): The string to be tokenized.

Returns:
    list: A list of tuples representing the tokens found in the input string. Each tuple
    contains the name of the token and its corresponding value.

Raises:
    Exception: If an unexpected character is encountered in the input string.
"""