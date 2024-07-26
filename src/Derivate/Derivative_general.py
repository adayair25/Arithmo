from Polynomial import Polynomial
from Polynomial_derivate import Polynomial_derivate
from Trigonometry import Trigonometry
from Exponential import Exponential


def Derivative_general(mode, variable='x', *args, **kwargs):
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

        def Get_function_and_derivative(func, const):
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
                if const != 1:
                    f=f'{const}*{func}({variable})'
                    f_der=Trigonometry(func, variable, const)
                else:
                    f=f'{func}({variable})'
                    f_der=Trigonometry(func, variable, const)
                return f,f_der
            elif func in ['exp', 'log']:
                if func=='exp':
                    if const != 1:
                        f=f'{const}*e^{variable}' 
                        f_der=Exponential(func, variable, const)
                    else:
                        f=f'e^{variable}' 
                        f_der=Exponential(func, variable, const)
                else:
                    if const != 1:
                        f=f'{const}*{func}({variable})' 
                        f_der=Exponential(func, variable, const)
                    else:
                        f=f'{func}({variable})'
                        f_der=Exponential(func, variable, const)
                return f,f_der
            elif isinstance(func, list):
                f=Polynomial(variable, func, const)
                f_der=Polynomial_derivate(variable, func, const)
                return f,f_der
            else:
                raise ValueError("Is needed a valid function")
        
        terms = [Get_function_and_derivative(func, const) for func, const in zip(functions, constants)]
        
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
        
        def get_function_and_derivative(func, const):
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
                if const != 1:
                    f=f'{const}*{func}({variable})'
                    f_dev= Trigonometry(func, variable, const)
                else:
                    f=f'{func}({variable})'
                    f_dev=Trigonometry(func, variable, const)
                return f,f_dev
            elif func in ['exp', 'log']:
                if func=='exp':
                    if const !=1:
                        f=f'{const}*e^({variable})'
                        f_dev=Exponential(func, variable, const)
                    else:
                        f=f'{func}({variable})'
                        f_dev=Exponential(func, variable, const)

                    return f,f_dev
            elif isinstance(func, list):
                f=Polynomial(variable, func, const)
                f_dev=Polynomial_derivate(variable, func, const)
                return f,f_dev
            else:
                raise ValueError("Is needed a valid function")
        
        (f1, f1_derivative), (f2, f2_derivative) = [get_function_and_derivative(func, const) for func, const in zip(functions, constants)]
        
        quotient_derivative = f'(({f2})*({f1_derivative}) - ({f1})*({f2_derivative}))/(({f2})^2)'
        return quotient_derivative

    elif mode == 'chain':
        if len(args) != 2:
            raise ValueError("mode chain need only two functions")
        
        outer_func, inner_func = args
        outer_const = kwargs.get('constant_outer', 1)
        inner_const = kwargs.get('constant_inner', 1)
        
        def get_function_and_derivative(func, const):
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']:
                if const != 1:
                    f=f'{const}*{func}({variable})'
                    f_dev=Trigonometry(func, variable, const)
                else:
                    f=f'{func}({variable})'
                    f_dev=Trigonometry(func, variable, const)
                return f,f_dev
            elif func in ['exp', 'log']:
                if func=='exp':
                    if const !=1:
                        f=f'{const}*e^({variable})'
                        f_dev=Exponential(func, variable, const)
                    else:
                        f=f'{func}({variable})'
                        f_dev=Exponential(func, variable, const)
                    return f,f_dev
            elif isinstance(func, list):
                f=Polynomial(variable, func, const)
                f_dev=Polynomial_derivate(variable, func, const)
                return f,f_dev
            else:
                raise ValueError("Is needed a valid function")
        
        outer_func_str, outer_func_derivative = get_function_and_derivative(outer_func, outer_const)
        inner_func_str, inner_func_derivative= get_function_and_derivative(inner_func, inner_const)
        
        chain_derivative = f'{outer_func_derivative}({inner_func_str}) * {inner_func_derivative}'
        return chain_derivative

    else:
        raise ValueError("mode no valid")

# example
a = Derivative_general('chain', 'x', 'exp', 'sin', constant_outer=1, constant_inner=1)
print(a)
