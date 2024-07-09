import re # Import the regular expression module

TOKENS = [
    ('NUMBER', r'\d+(\.\d*)?'),  # search for numbers
    ('STRING', r'\".*?\"'),      # search for strings
]

def lexer(input_string):
    tokens = []
    while len(input_string) > 0:
        match = None
        input_string = input_string.strip(" ")  # Remove leading whitespace
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
print(lexer('35 "Hello" "from" "GPT-4" 3.14')) # "Hello World from GPT-4 3.14" -> [('NUMBER', '35'), ('STRING', '"Hello"'), ('STRING', '"from"'), ('STRING', '"GPT-4"'), ('NUMBER', '3.14')]