from Polynomial import Polynomial
from Polynomial_derivate import Polynomial_derivate
from Trigonometry import Trigonometry
from Exponential import Exponential
from utils import get_function_and_derivative


def derivative_general(mode, variable='x', *args, **kwargs):
    if mode == 'sum':
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        derivatives = []

        for func, const in zip(functions, constants):
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
                derivatives.append(Trigonometry(func, variable, const))
            elif func in ['exp', 'log']:
                derivatives.append(Exponential(func, variable, const))
            elif isinstance(func, list):
                derivatives.append(Polynomial_derivate(variable, func, const))
            elif func == 0:
                continue
            else:
                raise ValueError("Is needed a valid function")

        return '+'.join(derivatives)
    
    elif mode == 'product':
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        
        if len(functions) < 2 or len(functions) > 3:
            raise ValueError("Product needed at least two functions")
        
        terms = [get_function_and_derivative(func, const) for func, const in zip(functions, constants)]
        
        if len(terms) == 2:
            (f1, f1_derivative), (f2, f2_derivative) = terms
            product_derivative = f'({f1})*({f2_derivative}) + ({f1_derivative})*({f2})'
        else:
            (f1, f1_derivative), (f2, f2_derivative), (f3, f3_derivative) = terms
            product_derivative = f'({f1})*({f2})*({f3_derivative}) + ({f1})*({f2_derivative})*({f3}) + ({f1_derivative})*({f2})*({f3})'

        return product_derivative

    elif mode == 'quotient':
        if len(args) != 2:
            raise ValueError("Quotient needs two functions")
        
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        
        (f1, f1_derivative), (f2, f2_derivative) = [get_function_and_derivative(func, const) for func, const in zip(functions, constants)]
        
        quotient_derivative = f'(({f2})*({f1_derivative}) - ({f1})*({f2_derivative}))/(({f2})^2)'
        return quotient_derivative

    elif mode == 'chain':
        if len(args) != 2:
            raise ValueError("mode chain need only two functions")
        
        outer_func, inner_func = args
        outer_const = kwargs.get('constant_outer', 1)
        inner_const = kwargs.get('constant_inner', 1)
        
        outer_func_str, outer_func_derivative = get_function_and_derivative(outer_func, outer_const)
        inner_func_str, inner_func_derivative= get_function_and_derivative(inner_func, inner_const)
        
        chain_derivative = f'{outer_func_derivative}({inner_func_str}) * {inner_func_derivative}'
        return chain_derivative

    else:
        raise ValueError("mode no valid")


# example
a = derivative_general('chain', 'x', 'exp', 'sin', constant_outer=1, constant_inner=1)
print(a)
