def Polynomial_derivate(variable, coefficients=[], constant=1):
    if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients):
        raise ValueError('Is needed a polynomial function')
    if not isinstance(constant, (int, float)):
        raise ValueError('The constant must be an integer/float')

    if len(coefficients) == 1:
        return '0'

    derivative = ''
    for j in range(1, len(coefficients)):
        term = f'{j * coefficients[j]}{variable}^{j - 1}'
        if constant != 1:
            term = f'({constant})*({term})'
        derivative += term
        if j < len(coefficients) - 1:
            derivative += '+'
    return derivative