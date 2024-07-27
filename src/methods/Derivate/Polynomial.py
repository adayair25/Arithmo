def Polynomial(variable, coefficients=[], constant=1): # Define the function
    if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients): # Check if the coefficients are a list of integers or floats
        raise ValueError('Is needed a polynomial function') # Raise an error
    if not isinstance(constant, (int, float)): # Check if the constant is an integer or a float
        raise ValueError('The constant must be an integer or float') # Raise an error

    term = f'{coefficients[0]}+' # Initialize the term
    for i in range(1, len(coefficients)): # Iterate over the coefficients
        term += f'{coefficients[i]}{variable}^{i}' # Add the term to the polynomial
        if i < len(coefficients) - 1: # Check if the term is not the last term
            term += '+' # Add a plus
    return term # Return the polynomial