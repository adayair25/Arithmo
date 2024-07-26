def Polynomial(variable, coefficients=[], constant=1):
    if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients):
        raise ValueError('Is needed a polynomial function')
    if not isinstance(constant, (int, float)):
        raise ValueError('The constant must be an integer or float')

    term = f'{coefficients[0]}+'
    for i in range(1, len(coefficients)):
        term += f'{coefficients[i]}{variable}^{i}'
        if i < len(coefficients) - 1:
            term += '+'
    return term