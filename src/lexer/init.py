import re # Import the regular expression module

TOKENS = [
    ('VAR', r'^var'),
    ('INT', r'\d+'),
    ('FLOAT', r'\d+\.\d*'),
    ('COLON', r':'),
    ('TYPES', r'\b(int|float|double|bool)\b'),              
    ('VAR_DECLARED', r'\b(\w+)\b'),
    ('EQUAL', r'='),
    ('VALUE', r'(\"\w+\")'),
    ('SEMICOLON', r';$'),
    ('PLUS', r'\+'),            
]

def lexer(input_string):
    tokens = []
    while len(input_string) > 0:
        match = None
        input_string = input_string.strip(" ") # Remove leading whitespace
        for token in TOKENS:
            name, pattern = token
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group()
                tokens.append((name, value))
                input_string = input_string[len(value):]
                break
        if not match:
            raise Exception('Error: unexpected character %s' % input_string[0])
    return tokens

# Test the lexer function
print(lexer('var MyVar: int = "Hiiii";'))