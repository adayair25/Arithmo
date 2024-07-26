def Exponential(funcion, variable, constant=1):
    if not isinstance(constant, (int, float)):
        raise ValueError('The constant must be an integer/float')

    expo_derivatives = {'exp': f'e^{variable}', 'log': f'1/{variable}'}

    if funcion not in expo_derivatives:
        raise ValueError("Is needed an exponential/logarithmic function")

    equivalent = expo_derivatives[funcion]
    if constant != 1:
        equivalent = f'{constant}*{equivalent}'
    return equivalent