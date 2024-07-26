from Polynomial import Polynomial
from Polynomial_derivate import Polynomial_derivate
from Trigonometry import Trigonometry
from Exponential import Exponential


def get_function_and_derivative(func, const, variable="y"):
    if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
        if const != 1:
            f = f'{const}*{func}({variable})'
            f_der = Trigonometry(func, variable, const)
        else:
            f = f'{func}({variable})'
            f_der = Trigonometry(func, variable, const)
        return f, f_der
    elif func in ['exp', 'log']:
        if func == 'exp':
            if const != 1:
                f = f'{const}*e^{variable}'
                f_der = Exponential(func, variable, const)
            else:
                f = f'e^{variable}'
                f_der = Exponential(func, variable, const)
        else:
            if const != 1:
                f = f'{const}*{func}({variable})'
                f_der = Exponential(func, variable, const)
            else:
                f = f'{func}({variable})'
                f_der = Exponential(func, variable, const)
        return f, f_der
    elif isinstance(func, list):
        f = Polynomial(variable, func, const)
        f_der = Polynomial_derivate(variable, func, const)
        return f, f_der
    else:
        raise ValueError("Is needed a valid function")

def get_derivative(func, const, variable="y"):
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
                if const != 1:
                    f_der = Trigonometry(func, variable, const)
                else:
                    f_der = Trigonometry(func, variable, const)
                return f_der
            elif func in ['exp', 'log']:
                if func == 'exp':
                    if const != 1:
                        f_der = Exponential(func, variable, const)
                    else:
                        f_der = Exponential(func, variable, const)
                else:
                    if const != 1:
                        f_der = Exponential(func, variable, const)
                    else:
                        f_der = Exponential(func, variable, const)
                return f_der
            elif isinstance(func, list):
                f_der = Polynomial_derivate(variable, func, const)
                return f_der
            else:
                raise ValueError("Is needed a valid function")