import re # Import the regular expression module

TOKENS = [
    ('VAR', r'^var'), # variable declaration
    #('INT', r'\d+'), # integer
    #('FLOAT', r'\d+\.\d+'),
    ('COLON', r':'), # search for :
    ('TYPES', r'\b(int|float|double|bool)\b'), # search for int, float, double, bool              
    ('EQUAL', r'='), # search for =
    ('VALUE', r'(\"\w+\"|\d+\.?\d+)'), # search for value
    ('SEMICOLON', r';$'), # search for ;
    ('PLUS', r'\+'), # search for +
    ('VAR_DECLARED', r'(\w+)'), # search for variable name

    # EXPERIMENTAL TOKENS
    ('MINUS', r'-'), # search for -
    ('MULTIPLY', r'\*'), # search for *
    ('DIVIDE', r'/'), # search for /
    ('LPAREN', r'\('), # search for (
    ('RPAREN', r'\)'), # search for )
    ('LBRACE', r'{'), #
]

def lexer(input_string):
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

# Test the lexer function
print(lexer('var MyVar: float = 34.0;')) 
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