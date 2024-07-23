# -*- coding: utf-8 -*-

"""
Created on Sat Jul 20 13:13:06 2024

@author: Eduardo Centeno
"""

def Poli(variable,coefficients=[],constant=1):
        if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients):
            raise ValueError('Is needed a polynomial function')
        if isinstance(constant, (int,float)):
            
            for i in range(0,len(coefficients)):
                if i==0:
                    term=f'{coefficients[i]}+'
                elif i<len(coefficients)-1:
                    if len(coefficients)==2:
                        term+=f'{coefficients[i]}'+f'{variable}^{i}'
                    else:
                        term+=f'{coefficients[i]}'+f'{variable}^{i}+'
                else:
                    term +=f'{coefficients[i]}'+f'{variable}^{i}'
            return term
#  Derivada de polinomios
def Poli_Derivative (variable,coefficients=[],constant=1):
        if not isinstance(coefficients, list) or not all(isinstance(i, (int, float)) for i in coefficients):
            raise ValueError('Is needed a polynomial function')
        if isinstance(constant, (int,float)):
            if constant==1:   
                if len(coefficients)==1:
                    a='0'
                    return a
                elif len(coefficients)>1:
                    for j in range(1,len(coefficients)):
                        if j==1:
                            if len(coefficients)==2:
                                Derivative=f'{j*coefficients[j]}'
                            else:
                                Derivative=f'{j*coefficients[j]}+'
                        elif j<len(coefficients)-1:
                            if len(coefficients)==2:
                                Derivative+=f'{j*coefficients[j]}'+f'{variable}^{j-1}'
                            else:
                                Derivative+=f'{j*coefficients[j]}'+f'{variable}^{j-1}+'
                        else:
                            Derivative +=f'{j*coefficients[j]}'+f'{variable}^{j-1}'
            else:
                if len(coefficients)==1:
                    a='0'
                    return a
                elif len(coefficients)>1:
                    for j in range(1,len(coefficients)):
                        if j==1:
                            if len(coefficients)==2:
                                Derivative=f'({constant})*('+f'{j*coefficients[j]})'
                            else:
                                Derivative=f'({constant})*('+f'{j*coefficients[j]}+'
                        elif j<len(coefficients)-1:
                            Derivative+=f'{j*coefficients[j]}'+f'{variable}^{j-1}+'
                        else:
                            Derivative +=f'{j*coefficients[j]}'+f'{variable}^{j-1})'
        else:
            raise ValueError('The constant must be an integer or float')
        return Derivative

#------------------------------------------------------------------------------------------------------------------------------------
"""
Derivative of simple trigonometric functions"""
def  Simple_Trig_Derivative(funcion,variable,constant=1):     
    if isinstance(constant, (int,float)):
        if constant ==1:
            if funcion=='sin':
                equivalent='cos('+variable+')'
                return equivalent
            elif funcion=='cos':
                equivalent='-sin('+variable+')'
                return  equivalent
            elif funcion=='tan':
                equivalent='sec^2('+variable+')'
                return  equivalent
            elif funcion=='cot':
                equivalent='-csc^2('+variable+')'
                return  equivalent
            elif funcion=='sec':
                equivalent='sec('+variable+')tan('+variable+')'
                return  equivalent
            elif funcion=='csc':
                
                equivalent='-scs('+variable+')cot('+variable+')'
                return  equivalent
            else:
                raise ValueError("Is needed a trigonometric function")
        else:
            if funcion=='sin':
                equivalent=f'{constant}'+'*cos('+variable+')'
                return  equivalent
            elif funcion=='cos':
                equivalent=f'-{constant}'+'*sin('+variable+')'
                return  equivalent
            elif funcion=='tan':
                equivalent=f'{constant}'+'*sec^2('+variable+')'
                return  equivalent
            elif funcion=='cot':
                equivalent=f'-{constant}'+'*csc^2('+variable+')'
                return  equivalent
            elif funcion=='sec':
                equivalent=f'{constant}'+'*sec('+variable+')'+'tan('+variable+')'
                return  equivalent
            elif funcion=='csc':
                equivalent=f'-{constant}'+'csc('+variable+')cot('+variable+')'
                return  equivalent
            else:
                raise ValueError("Is needed a trigonometric function")
    else:
         raise ValueError('The constant must be an integer or float')

#------------------------------------------------------------------------------------------------------------------
"""
Derivative of exponential functions
"""
def Derivative_expo(funcion,variable, constant=1):
    if isinstance(constant, (int,float)):
        if constant==1:
            if funcion=='exp':
                equivalent='e^'+variable
                return  equivalent
            elif funcion=='log':
                equivalent='1/'+variable
                return equivalent
        else:
            if funcion=='exp':
                equivalent=f'{constant}*e^'+variable
                return  equivalent
            elif funcion=='log':
                equivalent=f'{constant}*(1/'+variable
                return equivalent
            else: 
                raise ValueError("Is needed an exponential/logarithmic function")
    else:
       raise ValueError('The constant must be an integer or float')


#--------------------------------------------------------------------------------------------------------------------
"""
Derivative of sum, product, Quotient and chain rule
"""

"""
SUM
"""
def Derivative_general(mode,variable='x',function1=0,function2=0,function3=0,constantf1=1,constantf2=1,constantf3=1):
    if mode=='sum':
        if (function1!=0 and function2!=0 and function3!=0):
            if function1 in ['sin','cos','tan','cot','csc','sec']:
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif function2 in ['exp','log']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif isinstance(function2,list):
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")  
            elif function1 in ['exp','log']:
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif function2 in ['exp','log']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif isinstance(function2,list):
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")
            elif isinstance(function1,list):
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif function2 in ['exp','log']:
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                    else:
                        raise ValueError("Is needed a valid function")
                elif isinstance(function2,list):
                    if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                    elif function3 in ['exp','log']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                    elif isinstance(function3,list):
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")
            else:
               raise ValueError("Is needed a valid function") 
            return a
#--------------------------------------------------------------------------------------------------------------------------
        elif (function1!=0 and function2!=0):
            if function1 in ['sin','cos','tan','cot','csc','sec']:
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)
                elif function2 in ['exp','log']:
                    a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)
                elif isinstance(function2,list):
                    a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)
                else:
                    raise ValueError("Is needed a valid function")  
            elif function1 in ['exp','log']:
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)
                elif function2 in ['exp','log']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)
                elif isinstance(function2,list):
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)
                else:
                    raise ValueError("Is needed a valid function")  
            elif isinstance(function1,list):
                if function2 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Simple_Trig_Derivative(function2,variable,constantf2)
                elif function2 in ['exp','log']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Derivative_expo(function2,variable,constantf2)
                elif isinstance(function2,list):
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Poli_Derivative(variable,function2,constantf2)
                else:
                    raise ValueError("Is needed a valid function")
            else:
               raise ValueError("Is needed a valid function") 
            return a
#---------------------------------------------------------------------------------------------------------------------------
        elif (function1!=0 and function3!=0):
            if function1 in ['sin','cos','tan','cot','csc','sec']:
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                    a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                    a=Simple_Trig_Derivative(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")  
            elif function1 in ['exp','log']:
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                        a=Derivative_expo(function1,variable,constantf1)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")  
            elif isinstance(function1,list):
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                        a=Poli_Derivative(variable,function1,constantf1)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")
            else:
               raise ValueError("Is needed a valid function") 
            return a
#---------------------------------------------------------------------------------------------------------------------------
        elif (function2!=0 and function3!=0):
            if function2 in ['sin','cos','tan','cot','csc','sec']:
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                    a=Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                    a=Simple_Trig_Derivative(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")  
            elif function2 in ['exp','log']:
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Derivative_expo(function2,variable,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                        a=Derivative_expo(function2,variable,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                        a=Derivative_expo(function2,variable,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")  
            elif isinstance(function2,list):
                if function3 in ['sin','cos','tan','cot','csc','sec']:
                        a=Poli_Derivative(variable,function2,constantf2)+'+'+Simple_Trig_Derivative(function3,variable,constantf3)
                elif function3 in ['exp','log']:
                        a=Poli_Derivative(variable,function2,constantf2)+'+'+Derivative_expo(function3,variable,constantf3)
                elif isinstance(function3,list):
                        a=Poli_Derivative(variable,function2,constantf2)+'+'+Poli_Derivative(variable,function3,constantf3)
                else:
                    raise ValueError("Is needed a valid function")
            else:
               raise ValueError("Is needed a valid function") 
            return a
#---------------------------------------------------------------------------------------------------------------------------
        else:
            raise ValueError("at least two function must be different of 0") 


#--------------------------    PRODUCT         --------------------------------------------------
        
    elif mode=='product':
        if (function1!=0 and function2!=0 and function3!=0):
            if (function1!=0 and function2!=0 and function3!=0):
                if function1 in ['sin','cos','tan','cot','csc','sec']:
                    if function2 in ['sin','cos','tan','cot','csc','sec']:
                        if function3 in ['sin','cos','tan','cot','csc','sec']:
                            a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*'+function2+f')({variable}))({constantf3}*'+function3+f'({variable}))+({constantf1}*'+ \
                                function1+f'({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+f')({constantf3}*('+function3+f'({variable}))+({constantf1}*'+\
                                function1+f'({variable}))({constantf2}*'+function2+f'({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'
                        elif function3 in ['exp','log']:
                            if function3=='exp':
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*e^{variable})+({constantf1}*'+ \
                                   function1+f'({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*e^{variable})+('+\
                                   function1+f'({variable}))({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                            else:
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*log({variable}))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*log({variable}))+('+\
                                    function1+f'({variable}))({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                        elif isinstance(function3,list):
                            a='('++Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                            +f'({constantf1}*('+Poli(variable,function1,constantf1)+f')({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                            +f'({constantf1}*('+Poli(variable,function1,constantf1)+f')({variable}))({constantf2}*'+function2+f'({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                        else:
                            raise ValueError("Is needed a valid function")
                    elif function2 in ['exp','log']:
                        if function2=='exp':
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*'+function3+f'({variable}))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*'+function3+f'({variable}))+({constantf1}*'+\
                                    function1+f'({variable}))({constantf2}*e^{variable})('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                            elif function3 in ['exp','log']:
                                if function3=='exp':
                                    a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*e^{variable})+({constantf1}*'+\
                                        function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*e^{variable})+({constantf1}*'+\
                                        function1+f'({variable}))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+')'
                                else:
                                    a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*log({variable}))+({constantf1}*'+\
                                        function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*log({variable}))+({constantf1}*'+\
                                        function1+f'({variable}))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*('+Poli(variable,function3,constantf3)+f'))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+f'))+({constantf1}*'+\
                                    function1+f'({variable}))({constantf2}*e^{variable})('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                        elif function2=='log':
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*'+function3+f'({variable}))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*'+function3+f'({variable}))+({constantf1}*'+\
                                    function1+f'({variable}))({constantf2}*log({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                            elif function3 in ['exp','log']:
                                if function3=='exp':
                                    a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*e^{variable})+({constantf1}*'+\
                                        function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*e^{variable})+({constantf1}*'+\
                                        function1+f'({variable}))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                else:
                                    a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*log({variable}))+({constantf1}*'+\
                                        function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*log({variable}))+({constantf1}*'+\
                                        function1+f'({variable}))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+f'))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+f'))+({constantf1}*'+\
                                    function1+f'({variable}))({constantf2}*log({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                    elif isinstance(function2,list):
                        if function3 in ['sin','cos','tan','cot','csc','sec']:
                            a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                              f'+({constantf1}'+function1+f'({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*'+function3+f'({variable}))+'+\
                              f'({constantf1}'+function1+f'({variable}))({constantf2}*('+Poli(variable,function2,constantf2)+'))('+Simple_Trig_Derivative(function3, variable,constantf3)+')'
                        elif function3 in ['exp','log']:
                             if function3=='exp':
                                 a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'({variable}))({constantf3}*e^{variable})+({constantf1}*'+ \
                                    function1+f'({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}e^{variable})+('+\
                                    function1+f'({variable}))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+')'
                             else:
                                 a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'({variable}))({constantf3}*log({variable}))+({constantf1}*'+ \
                                    function1+f'({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*log({variable}))+('+\
                                    function1+f'({variable}))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+')'
                        elif isinstance(function3,list):
                            a='('+Simple_Trig_Derivative(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f')(({constantf3})('+Poli(variable,function3,constantf3)+f')+({constantf1}*'+\
                                function1+f'({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+f'))+({constantf1}*'+\
                                function1+f'({variable}))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Poli_Derivative(variable,function3,constantf3)+')'
                        else:
                            raise ValueError("Is needed a valid function")        

#-------------------------------------------------------------------------------------------------------------------------------

                elif function1 in ['exp','log']:
                    if function1=='exp':
                        if function2 in ['sin','cos','tan','cot','csc','sec']:
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                    f'+({constantf1}*e^{variable})('+Simple_Trig_Derivative(function2,variable,constantf2)+f'){constantf3}*('+function3+f'({variable}))'+\
                                    f'+({constantf1}*e^{variable})(({constantf2}*'+function2+f'({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                if function3=='exp':
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*e^{variable})'+\
                                        f'+({constantf1}*e^{variable})('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*e^{variable})'+\
                                       f'+({constantf1}*e^{variable})('+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                else:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*log({variable}))'+\
                                        f'+({constantf1}*e^{variable})('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*log({variable}))'+\
                                       f'+({constantf1}*e^{variable})({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                   f'+({constantf1}*e^{variable})('+Simple_Trig_Derivative(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                   f'+({constantf1}*e^{variable})({constantf2}*'+function2+f'({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                        elif function2 in ['exp','log']:
                            if function2=='exp':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*e^{variable})({constantf2}*e^{variable})('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*e^{variable})({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*e^{variable})({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*e^{variable})({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+({constantf1}*e^{variable}))({constantf2}*e^{variable})('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                            elif function2=='log':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*e^{variable}))({constantf2}*log({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*e^{variable})({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*e^{variable}))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Derivative_expo(function1,variable,constantf1)+f')({constantf2}*log({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+({constantf1}*e^{variable})('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+({constantf1}*e^{variable})({constantf2}*log({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                        elif isinstance(function2,list):
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Derivative_expo(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                  f'+({constantf1}*e^{variable})('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*'+function3+ f'({variable}))' +\
                                    f'+({constantf1}*e^{variable})({constantf2}*('+Poli(variable,function2,constantf2)+'))('+Simple_Trig_Derivative(function3, variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                  if function3=='exp':
                                      a='('+Derivative_expo(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f')({constantf3}*e^{variable})'+\
                                         f'+({constantf1}*e^{variable})('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*e^{variable})'+\
                                         f'+({constantf1}*e^{variable})(({constantf2})('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+')'
                                  else:
                                      a='('+Derivative_expo(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*log({variable}))'+\
                                      f'+({constantf1}*e^{variable})('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*log({variable}))'+\
                                      f'+({constantf1}*e^{variable})(({constantf2})('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Derivative_expo(function1,variable,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f')(({constantf3})('+Poli(variable,function3,constantf3)+')'+\
                                    f'+({constantf1}*e^{variable})('+Poli_Derivative(variable,function2,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                                    f'+({constantf1}*e^{variable})(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                   
                    
                    
                    else:
                        if function2 in ['sin','cos','tan','cot','csc','sec']:
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*'+function2+f'({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                    f'+({constantf1}*log({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+f'){constantf3}*('+function3+f'({variable}))'+\
                                    f'+({constantf1}*log({variable}))(({constantf2}*'+function2+f'({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                if function3=='exp':
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*'+function2+f'({variable}))({constantf3}*e^{variable})'+\
                                        f'+({constantf1}*log({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*e^{variable})'+\
                                        f'+({constantf1}*log({variable}))(({constantf2})*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                else:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*'+function2+f'({variable}))({constantf3}*log({variable}))'+\
                                        f'+({constantf1}*log({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*log({variable}))'+\
                                       f'+({constantf1}*log({variable}))({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*'+function2+f'({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                   f'+({constantf1}*log({variable}))('+Simple_Trig_Derivative(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                   f'+({constantf1}*log({variable}))({constantf2}*'+function2+f'({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                        elif function2 in ['exp','log']:
                            if function2=='exp':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*e^{variable})({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*log({variable})))({constantf2}*e^{variable})('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*e^{variable})({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*log({variable}))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*e^{variable})({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*log({variable}))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*e^{variable})({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+({constantf1}*log({variable}))({constantf2}*e^{variable})('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                            elif function2=='log':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*log({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+({constantf1}*log({variable}))({constantf2}*log({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*log({variable}))({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*e^{variable})'+\
                                            f'+({constantf1}*log({variable}))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*log({variable}))({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*log({variable}))'+\
                                            f'+({constantf1}*log({variable}))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Derivative_expo(function1,variable,constantf1)+f'))({constantf2}*log({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+({constantf1}*log({variable}))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+({constantf1}*log({variable}))({constantf2}*log({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                        elif isinstance(function2,list):
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Derivative_expo(function1,variable,constantf1)+f'))(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                  f'+({constantf1}*log({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*'+function3+ f'({variable}))' +\
                                    f'+({constantf1}*log({variable}))({constantf2}*('+Poli(variable,function2,constantf2)+'))('+Simple_Trig_Derivative(function3, variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                  if function3=='exp':
                                      a='('+Derivative_expo(function1,variable,constantf1)+f'))(({constantf2})('+Poli(variable,function2,constantf2)+f')({constantf3}*e^{variable})'+\
                                         f'+({constantf1}*log({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}e^{variable})'+\
                                         f'+({constantf1}*log({variable}))(({constantf2})('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+')'
                                  else:
                                      a='('+Derivative_expo(function1,variable,constantf1)+f'))(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*log({variable}))'+\
                                      f'+({constantf1}*log({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}log({variable}))'+\
                                      f'+({constantf1}*log({variable}))(({constantf2})('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Derivative_expo(function1,variable,constantf1)+f'))(({constantf2})('+Poli(variable,function2,constantf2)+f')(({constantf3})('+Poli(variable,function3,constantf3)+')'+\
                                    f'+({constantf1}*log({variable}))('+Poli_Derivative(variable,function2,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                                    f'+({constantf1}*log({variable}))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
#-------------------------------------------------------------------------------------------------------------------------------


                elif isinstance(function1,list):
                        if function2 in ['sin','cos','tan','cot','csc','sec']:
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                    f'+(({constantf1})('+Poli(variable,function1,constantf1)+'))('+Simple_Trig_Derivative(function2,variable,constantf2)+f')({constantf3}*'+function3+f'({variable}))'+\
                                    f'+(({constantf1})('+Poli(variable,function1,constantf1)+f'))({constantf2}*'+function2+f'({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                if function3=='exp':
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*e^{variable})'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*e^{variable})'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                else:
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*'+function2+f'({variable}))({constantf3}*log({variable}))'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Simple_Trig_Derivative(function2,variable,constantf2)+')('+f'{constantf3}*log({variable}))'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*'+function2+f'({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*'+function2+f'({variable}))(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+ \
                                   f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Simple_Trig_Derivative(function2,variable,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                                   f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*'+function2+f'({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")
                        elif function2 in ['exp','log']:
                            if function2=='exp':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*e^{variable})({constantf3}*'+function3+f'({variable}))'+\
                                     f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*'+function3+f'({variable}))'+\
                                     f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*e^{variable})('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*e^{variable})({constantf3}*e^{variable})'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*e^{variable})'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*e^{variable})({constantf3}*log({variable}))'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*log({variable}))'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*e^{variable})('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*e^{variable})({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f')({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*e^{variable})('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                            elif function2=='log':
                                if function3 in ['sin','cos','tan','cot','csc','sec']:
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*log({variable}))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                     f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*log({variable}))('+Simple_Trig_Derivative(function3,variable,constantf3)+')'                         
                                elif function3 in ['exp','log']:
                                    if function3=='exp':
                                        a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*log({variable}))({constantf3}*e^{variable})'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*e^{variable})'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+')'
                                    else:
                                        a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*log({variable}))({constantf3}*log({variable}))'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*log({variable}))'+\
                                            f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*log({variable}))('+Derivative_expo(function3,variable,constantf3)+'))'
                                elif isinstance(function3,list):
                                    a='('+Poli_Derivative(variable,function1,constantf1)+f')({constantf2}*log({variable}))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+ \
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Derivative_expo(function2,variable,constantf2)+f'))({constantf3}*('+Poli(variable,function3,constantf3)+'))'+\
                                        f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2}*log({variable}))('+Poli_Derivative(variable,function3,constantf3)+')'
                                else:
                                    raise ValueError("Is needed a valid function")
                        elif isinstance(function2,list):
                            if function3 in ['sin','cos','tan','cot','csc','sec']:
                                a='('+Poli_Derivative(variable,function1,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*'+function3+f'({variable}))'+\
                                    f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*'+function3+ f'({variable}))' +\
                                    f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Simple_Trig_Derivative(function3, variable,constantf3)+')'
                            elif function3 in ['exp','log']:
                                  if function3=='exp':
                                      a='('+Poli_Derivative(variable,function1,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f')({constantf3}*e^{variable})'+\
                                         f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*e^{variable})'+\
                                         f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+')'
                                  else:
                                      a='('+Poli_Derivative(variable,function1,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f'))({constantf3}*log({variable}))'+\
                                      f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Poli_Derivative(variable,function2,constantf2)+f')({constantf3}*log({variable}))'+\
                                      f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))(({constantf2})*)('+Poli(variable,function2,constantf2)+'))('+Derivative_expo(function3,variable,constantf3)+'))'
                            elif isinstance(function3,list):
                                a='('+Poli_Derivative(variable,function1,constantf1)+f')(({constantf2})('+Poli(variable,function2,constantf2)+f')(({constantf3})('+Poli(variable,function3,constantf3)+')'+\
                                    f'+(({constantf1})*('+Poli(variable,function1,constantf1)+'))('+Poli_Derivative(variable,function2,constantf2)+f')(({constantf3})*('+Poli(variable,function3,constantf3)+'))'+\
                                    f'+(({constantf1})*('+Poli(variable,function1,constantf1)+f'))(({constantf2})*('+Poli(variable,function2,constantf2)+'))('+Poli_Derivative(variable,function3,constantf3)+')'
                            else:
                                raise ValueError("Is needed a valid function")                
                else:
                    raise ValueError("Is needed a valid function")      

        elif (function1!=0 and function2!=0):
            a='hola 2'
        elif (function1!=0 and function3!=0):
            a='hola 3'
        elif (function2!=0 and function3!=0):
            a='hola 4'
        else:
            raise ValueError("at least two function must be different of 0") 
        return a
    elif mode=='quotient':
        return 'hola 3'
    elif mode=='chain':
        return 'hola 4'
    else:
        raise ValueError("not valid mode")



a=Derivative_general('product','x',[0,0,1],'sin','log')
print(a)