from methods.Derivate.Polynomial import Polynomial
from methods.Derivate.Polynomial_derivate import Polynomial_derivate
from methods.Derivate.Trigonometry import Trigonometry
from methods.Derivate.Exponential import Exponential

def get_function_and_derivative(func, const, variable="y"): # Define the function
    if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']: # Check if the function is a trigonometric function
        if const != 1: # Check if the constant is different from 1
            f = f'{const}*{func}({variable})' # Define the function 
            f_der = Trigonometry(func, variable, const) # Get the derivative of the function
        else:
            f = f'{func}({variable})' # Define the function
            f_der = Trigonometry(func, variable, const) # Get the derivative of the function
        return f, f_der
    elif func in ['exp', 'log']: # Check if the function is an exponential function
        if func == 'exp': # Check if the function is an exponential function
            if const != 1: # Check if the constant is different from 1
                f = f'{const}*e^{variable}' # Define the function
                f_der = Exponential(func, variable, const) # Get the derivative of the function
            else:
                f = f'e^{variable}' # Define the function
                f_der = Exponential(func, variable, const) # Get the derivative of the function
        else:
            if const != 1: # Check if the constant is different from 1
                f = f'{const}*{func}({variable})' # Define the function
                f_der = Exponential(func, variable, const) # Get the derivative of the function
            else: 
                f = f'{func}({variable})' # Define the function
                f_der = Exponential(func, variable, const) # Get the derivative of the function
        return f, f_der # Return the function and its derivative
    elif isinstance(func, list):  # Check if the function is a polynomial
        f = Polynomial(variable, func, const) # Define the function
        f_der = Polynomial_derivate(variable, func, const) # Get the derivative of the function
        return f, f_der
    else:
        raise ValueError("Is needed a valid function") # Raise an error

def get_derivative(func, const, variable="y"): # Define the function
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']: # Check if the function is a trigonometric function
                if const != 1: # Check if the constant is different from 1
                    f_der = Trigonometry(func, variable, const) # Get the derivative of the function
                else:
                    f_der = Trigonometry(func, variable, const) # Get the derivative of the function
                return f_der
            elif func in ['exp', 'log']: # Check if the function is an exponential function
                if func == 'exp': # Check if the function is an exponential function
                    if const != 1:
                        f_der = Exponential(func, variable, const) # Get the derivative of the function
                    else:
                        f_der = Exponential(func, variable, const) # Get the derivative of the function
                else:
                    if const != 1:
                        f_der = Exponential(func, variable, const) # Get the derivative of the function
                    else:
                        f_der = Exponential(func, variable, const) # Get the derivative of the function
                return f_der
            elif isinstance(func, list): # Check if the function is a polynomial
                f_der = Polynomial_derivate(variable, func, const) # Get the derivative of the function
                return f_der
            else:
                raise ValueError("Is needed a valid function") # Raise an error