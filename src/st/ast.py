from lark import Transformer, v_args
from methods.Derivate.Derivative_general import derivative_general as dev
class Interpreter:
    def __init__(self) -> None:
        pass

    def get_result(self, tree):
        method_name = tree.data # Get the object's data
        method = getattr(self, method_name) # Get the method
        return method(tree) # Return the method
    
    def deriv_gen(self, tree): # Search for the nodes to get the values and call the derivative function
        MODE = None # Initialize the mode
        FUNCTIONS = [] # Initialize the functions
        VARIABLE = None # Initialize the variable
        CONSTANTS = [] # Initialize the constants
        constant = False # Initialize the constant

        for children in tree.children: # Iterate over the children
            if children.type == "MODES": # Check if the child is a mode
                MODE = children.value # Get the mode
            elif children.type == "IDENTIFIER": # Check if the child is an identifier
                VARIABLE = children.value # Get the variable
            elif children.type == "LIST_POLY": # Check if the child is a list of polynomials
                FUNCTIONS.append(eval(children.value)) # Get the functions
            elif children.type == "FUNCTION_EXP": # Check if the child is a function
                FUNCTIONS.append(children.value) # Get the functions
            elif children.type == "CONSTANTS": # Check if the child is a constant
                constant = True # Set the constant to True
            elif children.type == "LIST_POLY" and constant: # Check if the child is a list of polynomials and the constant is True
                CONSTANTS.append(eval(children.value)) # Get the constants
                return print(dev(MODE, VARIABLE, FUNCTIONS[0], FUNCTIONS[1], CONSTANTS[0])) # Return the derivative

        return print(dev(MODE, VARIABLE, FUNCTIONS[0], FUNCTIONS[1])) # Return the derivative
    
    def set_var(self, tree): # Search for the nodes to get the values and assign the variable
        variable_name = None # Initialize the variable name
        assigned_value = None # Initialize the assigned value

        for children in tree.children: # Iterate over the children
            if children.type == "IDENTIFIER": # Check if the child is an identifier
                variable_name = children.value # Get the variable name
            elif children.type == "VALUE": # Check if the child is a value
                assigned_value = children.value # Get the assigned value
        return variable_name, assigned_value # Return the variable name and the assigned value