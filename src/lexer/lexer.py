from .tokens import TOKENS # Import the list of TOKENS
import re # Import the regular expression module

class Lexer:
    def __init__(self) -> None:
        pass

    def tokenize(self, input_string):
        tokens = []
        while len(input_string) > 0:
            match = None # Initialize match to None
            input_string = input_string.strip(" ") # Remove leading whitespace
            for token in TOKENS: 
                name, pattern = token # Unpack the token tuple
                regex = re.compile(pattern) # Compile the regular expression pattern
                match = regex.match(input_string) # Match the pattern against the input string
                if match:
                    value = match.group() # Get the matched value
                    tokens.append((name, value)) # Append the token to the list
                    input_string = input_string[len(value):] # Remove the token from the input string
                    break
            if not match:
                raise Exception('Error: unexpected character %s' % input_string[0]) # Raise an exception if an unexpected character is encountered
        return tokens # Return the list of tokens

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