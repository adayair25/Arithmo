from Polynomial import Polynomial
from Polynomial_derivate import Polynomial_derivate
from Trigonometry import Trigonometry
from Exponential import Exponential
from utils import get_function_and_derivative,get_derivative

def derivative_general(mode, variable='t', *args, **kwargs):
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
        
        terms = [get_function_and_derivative(func, const,variable) for func, const in zip(functions, constants)]
        
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
        
        (f1, f1_derivative), (f2, f2_derivative) = [get_function_and_derivative(func, const,variable) for func, const in zip(functions, constants)]
        
        quotient_derivative = f'(({f2})*({f1_derivative}) - ({f1})*({f2_derivative}))/(({f2})^2)'
        return quotient_derivative

    elif mode == 'chain':
        if len(args) != 2:
            raise ValueError("mode chain need only two functions")
        
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        f=functions[0]
        g=functions[1]
        f_der=get_derivative(f,constants[0],f'{g}({variable})')
        g_der=get_derivative(g,constants[1],variable)
        chain='('+f_der+')*'+g_der
        return chain

    else:
        raise ValueError("mode no valid")

sum1=derivative_general('sum','t',[2,2,2,3],'sin')
prod1=derivative_general('product','k',[0,1],'sin',constants=[2,5])
quotient1=derivative_general('quotient','x','log','exp',constants=[1,9])
chains=derivative_general('chain','z','exp','log',constants=[2,2])

print(sum1,'\n',prod1,'\n',quotient1,'\n',chains)