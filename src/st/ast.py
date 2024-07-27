from lark import Transformer, v_args
from methods.Derivate.Derivative_general import derivative_general as dev
class Interpreter:
    def __init__(self):
        self.vars = {}

    def get_result(self, tree):
        method_name = tree.data # Get the object's data
        method = getattr(self, method_name) # Get the method
        return method(tree) # Return the method
    
    def deriv_gen(self, tree): # Search for the nodes to get the values and call the derivative function
        MODE = None 
        FUNCTIONS = [] 
        VARIABLE = None 
        CONSTANTS = [] 
        constant = False 

        def handle_modes(child):
            nonlocal MODE
            MODE = child.value

        def handle_identifier(child):
            nonlocal VARIABLE
            VARIABLE = child.value

        def handle_list_poly(child):
            if constant:
                CONSTANTS.append(eval(child.value))
            else:
                FUNCTIONS.append(eval(child.value))

        def handle_function_exp(child):
            FUNCTIONS.append(child.value)

        def handle_constants(child):
            nonlocal constant
            constant = True
        
        actions = {
            "MODES": handle_modes,
            "IDENTIFIER": handle_identifier,
            "LIST_POLY": handle_list_poly,
            "FUNCTION_EXP": handle_function_exp,
            "CONSTANTS": handle_constants
        }

        for child in tree.children:
            action = actions.get(child.type)
            if action:
                action(child)

        return print(dev(MODE, VARIABLE, FUNCTIONS[0], FUNCTIONS[1])) # Return the derivative
    
    def set_var(self, tree): # Search for the nodes to get the values and assign the variable
        variable_name = None # Initialize the variable name
        assigned_value = None # Initialize the assigned value
        function_bool = False
        concat = None
        print(tree)
        for children in tree.children: # Iterate over the children
            if children.type == "IDENTIFIER": # Check if the child is an identifier
                variable_name = children.value # Get the variable name
            elif children.type == "VALUE": # Check if the child is a value
                assigned_value = children.value # Get the assigned value
            elif children.type == "FUNCTIONS_CALL":
                function_bool = True
            elif (children.type == "SEMICOLON") and function_bool:
                function_bool = False
            
            if function_bool:
                concat = ''.join(children.value)
                
        if children.type == "FUNCTIONS_CALL":
            self.vars[variable_name] = concat
        else:
            self.vars[variable_name] = assigned_value

    def show_var(self, tree):
        for children in tree.children:
            if children.type == "IDENTIFIER":
                print(self.vars[children.value])
        #print(tree) #sum,t,[2,2,3],sin