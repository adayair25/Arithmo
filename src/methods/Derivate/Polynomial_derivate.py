def Polynomial_derivate(variable, coefficients=[], constant=1): # Define the function
    if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients): # Check if the coefficients are a list of integers or floats
        raise ValueError('Is needed a polynomial function') # Raise an error
    if not isinstance(constant, (int, float)): # Check if the constant is an integer or a float
        raise ValueError('The constant must be an integer/float') # Raise an error

    if len(coefficients) == 1: # Check if the polynomial is a constant
        return '0'

    derivative = '' # Initialize the derivative
    for j in range(1, len(coefficients)): # Iterate over the coefficients
        term = f'{j * coefficients[j]}{variable}^{j - 1}' # Calculate the derivative of the term
        if constant != 1: # Check if the constant is different from 1
            term = f'({constant})*({term})' # Multiply the constant by the term
        derivative += term # Add the term to the derivative
        if j < len(coefficients) - 1: # Check if the term is not the last term
            derivative += '+' # Add a plus sign to the derivative
    return derivative # Return the derivative