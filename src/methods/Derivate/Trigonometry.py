def Trigonometry(funcion, variable, constant=1): # Define the function
    if not isinstance(constant, (int, float)): # Check if the constant is an integer or a float
        raise ValueError('The constant must be an integer/float') # Raise an error

    trig_derivatives = {'sin': 'cos', 'cos': '-sin', 'tan': 'sec^2', 'cot': '-csc^2', 'sec': 'sec*tan',
                        'csc': '-csc*cot'} # Define the trigonometric derivatives

    if funcion not in trig_derivatives: # Check if the function is a trigonometric function
        raise ValueError("Is needed a trigonometric function") # Raise an error

    equivalent = f'{trig_derivatives[funcion]}({variable})' # Get the equivalent of the function
    if constant != 1: # Check if the constant is different from 1
        equivalent = f'{constant}*{equivalent}' # Multiply the constant by the equivalent
    return equivalent # Return the equivalent