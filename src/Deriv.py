# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:13:06 2024

@author: COLOR CENTER
"""

def Poli_Derivative (variable,coefficients=[]):

        for i in range(0,len(coefficients)):
            if i==0:
                term=f'{coefficients[i]}+'
            elif i<len(coefficients):
                term+=f'{coefficients[i]}'+f'{variable}^{i}+'
            else:
                term +=f'{coefficients[i]}'+f'{variable}^{i}'
        
        for j in range(1,len(coefficients)):
            if j==1:
                Derivative=f'{j*coefficients[j]}+'
            elif j<len(coefficients)-1:
                Derivative+=f'{j*coefficients[j]}'+f'{variable}^{j-1}+'
            else:
                Derivative +=f'{j*coefficients[j]}'+f'{variable}^{j-1}'
        return Derivative

"-------------------------------------------------------------------------------------------------------------------"
"""
Derivative of simple trigonometric functions"""
def  Simple_Trig_Derivative(funcion,variable,constant=1):     
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
            '--------------------------------------------------------------------'            
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

"-------------------------------------------------------------------------------------------------------------------"
"""
Derivative of exponential functions
"""
def Derivative_expo(funcion,variable, constant=1):

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
                equivalent=f'{constant}*1/'+variable
                return print(f"{constant}*"+equivalent)
            else: 
                raise ValueError("Is needed an exponential/logarithmic function")


"-------------------------------------------------------------------------------------------------------------------"
"""
Derivative of sum, product, Quotient and chain rule
"""
def Derivative_gerenal(mode,function1=0,function2=0,function3=0,variable='x'):
    if mode=='sum':
        return print('hola')
    elif mode=='product':
        return print('hola')
    elif mode=='quotient':
        return print('hola')
    else:
        raise ValueError("not valid mode")
   
