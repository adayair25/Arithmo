def Trigonometry(funcion, variable, constant=1):
    if not isinstance(constant, (int, float)):
        raise ValueError('The constant must be an integer/float')

    trig_derivatives = {'sin': 'cos', 'cos': '-sin', 'tan': 'sec^2', 'cot': '-csc^2', 'sec': 'sec*tan',
                        'csc': '-csc*cot'}

    if funcion not in trig_derivatives:
        raise ValueError("Is needed a trigonometric function")

    equivalent = f'{trig_derivatives[funcion]}({variable})'
    if constant != 1:
        equivalent = f'{constant}*{equivalent}'
    return equivalent