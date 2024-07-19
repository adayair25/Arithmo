"""
Polynomial derivative
"""
class Poli_Derivative:
    def __init__(self,coefficients,variable):
        self.coefficients=coefficients
        self.variable=variable
        termo=''
        term=''
        for i in range(0,len(coefficients)):
            if i==0:
                term=f'{self.coefficients[i]}+'
            elif i<len(coefficients):
                term+=f'{self.coefficients[i]}'+f'{self.variable}^{i}+'
            else:
                term +=f'{self.coefficients[i]}'+f'{self.variable}^{i}'
        
        for j in range(1,len(coefficients)):
            if j==1:
                termo=f'{j*self.coefficients[j]}+'
            elif j<len(coefficients)-1:
                termo+=f'{j*self.coefficients[j]}'+f'{self.variable}^{j-1}+'
            else:
                termo +=f'{j*self.coefficients[j]}'+f'{self.variable}^{j-1}'

        return print('the derivative of '+term +'is: '+termo)
"""
Derivative of simple trigonometric functions"""
class Simple_Trig_Derivative:
    def __init__(self,funcion,variable,constant=1):
        self.funcion=funcion
        self.variable=variable
        self.constant=constant
        if constant ==1:
            if funcion=='sin':
                self.equivalent='cos('
                return  print(self.equivalent+self.variable+')')
            elif funcion=='cos':
                self.equivalent='-sen('
                return  print(self.equivalent+self.variable+')')
            elif funcion=='tan':
                self.equivalent='sec^2('
                return  print(self.equivalent+self.variable+')')
            elif funcion=='cot':
                self.equivalent='-csc^2('
                return  print(self.equivalent+self.variable+')')
            elif funcion=='sec':
                self.equivalent='sec('+self.variable+')tan('+self.variable
                return  print(self.equivalent+')')
            elif funcion=='csc':
                self.equivalent='-scs('+self.variable+')cot('+self.variable
                return  print(self.equivalent+')')
            else:
                return print("this is not a trigonometric function ")
        else:
            if funcion=='sin':
                self.equivalent='cos('
                return  print(f"{self.constant}*"+self.equivalent+self.variable+')')
            elif funcion=='cos':
                self.equivalent='-sen('
                return  print(f"{self.constant}*"+self.equivalent+self.variable+')')
            elif funcion=='tan':
                self.equivalent='sec^2('
                return  print(f"{self.constant}*"+self.equivalent+self.variable+')')
            elif funcion=='cot':
                self.equivalent='-csc^2('
                return  print(f"{self.constant}*"+self.equivalent+self.variable+')')
            elif funcion=='sec':
                self.equivalent='sec('+self.variable+')tan('+self.variable
                return  print(f"{self.constant}*"+self.equivalent+')')
            elif funcion=='csc':
                self.equivalent='-scs('+self.variable+')cot('+self.variable
                return  print(f"{self.constant}*"+self.equivalent+')')
            else:
                return print("this is not a trigonometric function")
"""
Derivative of exponential functions
"""
class Derivative_expo:
    def __init__(self,funcion,variable, constant=1):
        self.funcion=funcion
        self.variable=variable
        self.constant=constant
        if constant==1:
            if funcion=='exp':
                self.equivalent='exp('+self.variable
                return  print(self.equivalent+')')
            elif funcion=='log':
                self.equivalent='1/'+self.variable
                return print(self.equivalent)
        else:
            if funcion=='exp':
                self.equivalent='exp('+self.variable
                return  print(f"{self.constant}*"+self.equivalent+')')
            elif funcion=='log':
                self.equivalent='1/'+self.variable
                return print(f"{self.constant}*"+self.equivalent)
            else: 
                return print ("this is not an exponential, logarithmic function")
            
            
            
        
poli = Poli_Derivative([3,2,1],'x')    
trigo=Simple_Trig_Derivative('cos', 'k',4) 
trigo2=Simple_Trig_Derivative('son', 'm',1)       
expo=Derivative_expo('log','x',4)
expo2=Derivative_expo('logi','s',4)

