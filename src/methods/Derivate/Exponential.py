def Exponential(funcion, variable, constant=1): # Define the function
    if not isinstance(constant, (int, float)): # Check if the constant is an integer or a float
        raise ValueError('The constant must be an integer/float')

    expo_derivatives = {'exp': f'e^({variable})', 'log': f'1/{variable}'} # Define the exponential derivatives

    if funcion not in expo_derivatives: # Check if the function is an exponential function
        raise ValueError("Is needed an exponential/logarithmic function")

    equivalent = expo_derivatives[funcion] # Get the equivalent of the function
    if constant != 1: # Check if the constant is different from 1
        equivalent = f'{constant}*{equivalent}' # Multiply the constant by the equivalent
    return equivalent # Return the equivalent

#print(Exponential('exp', 'x', 2)) # Test the function