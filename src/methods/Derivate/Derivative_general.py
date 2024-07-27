#from methods.Derivate.Polynomial import Polynomial
from methods.Derivate.Polynomial_derivate import Polynomial_derivate
from methods.Derivate.Trigonometry import Trigonometry
from methods.Derivate.Exponential import Exponential
from methods.Derivate.utils import get_function_and_derivative,get_derivative

def derivative_general(mode, variable='t', *args, **kwargs): # mode: sum, product, quotient, chain
    if mode == 'sum':
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        derivatives = [] # List of derivatives

        for func, const in zip(functions, constants): # Iterate over the functions
            if func in ['sin', 'cos', 'tan', 'cot', 'csc', 'sec']: # Check if the function is a trigonometric function
                derivatives.append(Trigonometry(func, variable, const)) # Append the derivative to the list
            elif func in ['exp', 'log']: # Check if the function is an exponential function
                derivatives.append(Exponential(func, variable, const)) # Append the derivative to the list
            elif isinstance(func, list): # Check if the function is a polynomial
                derivatives.append(Polynomial_derivate(variable, func, const)) # Append the derivative to the list
            elif func == 0: # Check if the function is a constant
                continue
            else:
                raise ValueError("Is needed a valid function")

        return '+'.join(derivatives) 
    
    elif mode == 'product': 
        functions = args 
        constants = kwargs.get('constants', [1] * len(functions)) # Get the constants
        
        if len(functions) < 2 or len(functions) > 3: # Check if the product has at least two functions
            raise ValueError("Product needed at least two functions") # Raise an error
        
        terms = [get_function_and_derivative(func, const,variable) for func, const in zip(functions, constants)] # Get the functions and their derivatives
        
        if len(terms) == 2: # Check if the product has two functions
            (f1, f1_derivative), (f2, f2_derivative) = terms # Get the functions and their derivatives
            product_derivative = f'({f1})*({f2_derivative}) + ({f1_derivative})*({f2})' # Calculate the derivative of the product
        else:
            (f1, f1_derivative), (f2, f2_derivative), (f3, f3_derivative) = terms # Get the functions and their derivatives
            product_derivative = f'({f1})*({f2})*({f3_derivative}) + ({f1})*({f2_derivative})*({f3}) + ({f1_derivative})*({f2})*({f3})' # Calculate the derivative of the product

        return product_derivative # Return the derivative of the product

    elif mode == 'quotient':
        if len(args) != 2:
            raise ValueError("Quotient needs two functions")
        
        functions = args
        constants = kwargs.get('constants', [1] * len(functions))
        
        (f1, f1_derivative), (f2, f2_derivative) = [get_function_and_derivative(func, const,variable) for func, const in zip(functions, constants)] # Get the functions and their derivatives
        
        quotient_derivative = f'(({f2})*({f1_derivative}) - ({f1})*({f2_derivative}))/(({f2})^2)' # Calculate the derivative of the quotient
        return quotient_derivative

    elif mode == 'chain':
        if len(args) != 2:
            raise ValueError("mode chain need only two functions")
        
        functions = args # Get the functions
        constants = kwargs.get('constants', [1] * len(functions)) # Get the constants
        f=functions[0] # Get the first function
        g=functions[1] # Get the second function
        f_der=get_derivative(f,constants[0],f'{g}({variable})') # Get the derivative of the first function
        g_der=get_derivative(g,constants[1],variable) # Get the derivative of the second function
        chain='('+f_der+')*'+g_der # Calculate the derivative of the chain
        return chain

    else:
        raise ValueError("mode no valid") # Raise an error

"""
sum1=derivative_general('sum','t',[2,2,2,3],'sin')
sum2=derivative_general('sum','t','cos','sin')
prod1=derivative_general('product','k',[0,1],'sin',constants=[2,5])
quotient1=derivative_general('quotient','x','log','exp',constants=[1,9])
chains=derivative_general('chain','z','exp','log',constants=[2,2])

print(sum2)
print(sum1)
print(sum1,'\n',prod1,'\n',quotient1,'\n',chains)
"""