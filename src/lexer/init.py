import re

TOKENS = [
    ('NUMBER', r'\d+(\.\d*)?'), # search for numbers
    ('STRING', r'\".*?\"'),
]

def lexer(input_string):
    tokens = []
    while len(input_string) > 0:
        match = None
        for token in TOKENS:
            name, pattern = token
            regex = re.compile(pattern)
            match = regex.match(input_string)
            if match:
                value = match.group(0)
                tokens.append((name, value))
                input_string = input_string[len(value):]
                return tokens
                break
        if not match:
            raise Exception('Error: unexpected character %s' % input_string[0])
   

lexer('hola')
