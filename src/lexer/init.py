import re

TOKENS = [
    ('NUMBER', r'\d+(\.\d*)?'),  # search for numbers
    ('STRING', r'\".*?\"'),      # search for strings
]

def lexer(input_string):
    tokens = []
    while len(input_string) > 0:
        match = None
        input_string = input_string.lstrip()  # Remove leading whitespace
        for token in TOKENS:
            name, pattern = token
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                tokens.append((name, value))
                input_string = input_string[len(value):]
                break
        if not match:
            raise Exception('Error: unexpected character %s' % input_string[0])
    return tokens

# Test the lexer function
print(lexer('35 "hello" 3.14'))