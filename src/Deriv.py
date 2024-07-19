"""
Derivada de polinomios
"""
class Derivada_poli:
    def __init__(self,coeficientes,variable):
        self.coeficientes=coeficientes
        self.variable=variable
        termo=''
        term=''
        for i in range(0,len(coeficientes)):
            if i==0:
                term=f'{self.coeficientes[i]}+'
            elif i<len(coeficientes):
                term+=f'{self.coeficientes[i]}'+f'{self.variable}^{i}+'
            else:
                term +=f'{self.coeficientes[i]}'+f'{self.variable}^{i}'
        
        for j in range(1,len(coeficientes)):
            if j==1:
                termo=f'{j*self.coeficientes[j]}+'
            elif j<len(coeficientes)-1:
                termo+=f'{j*self.coeficientes[j]}'+f'{self.variable}^{j-1}+'
            else:
                termo +=f'{j*self.coeficientes[j]}'+f'{self.variable}^{j-1}'

        return print('la derivada de '+term +'es: '+termo)
"""
Derivada de funciones trigonométricas
"""
class Derivada_trig_simple:
    def __init__(self,funcion,variable,constante=1):
        self.funcion=funcion
        self.variable=variable
        self.constante=constante
        if constante ==1:
            if funcion=='sin':
                self.equivalente='cos('
                return  print(self.equivalente+self.variable+')')
            elif funcion=='cos':
                self.equivalente='-sen('
                return  print(self.equivalente+self.variable+')')
            elif funcion=='tan':
                self.equivalente='sec^2('
                return  print(self.equivalente+self.variable+')')
            elif funcion=='cot':
                self.equivalente='-csc^2('
                return  print(self.equivalente+self.variable+')')
            elif funcion=='sec':
                self.equivalente='sec('+self.variable+')tan('+self.variable
                return  print(self.equivalente+')')
            elif funcion=='csc':
                self.equivalente='-scs('+self.variable+')cot('+self.variable
                return  print(self.equivalente+')')
            else:
                return print("no es una función trigonométrica")
        else:
            if funcion=='sin':
                self.equivalente='cos('
                return  print(f"{self.constante}*"+self.equivalente+self.variable+')')
            elif funcion=='cos':
                self.equivalente='-sen('
                return  print(f"{self.constante}*"+self.equivalente+self.variable+')')
            elif funcion=='tan':
                self.equivalente='sec^2('
                return  print(f"{self.constante}*"+self.equivalente+self.variable+')')
            elif funcion=='cot':
                self.equivalente='-csc^2('
                return  print(f"{self.constante}*"+self.equivalente+self.variable+')')
            elif funcion=='sec':
                self.equivalente='sec('+self.variable+')tan('+self.variable
                return  print(f"{self.constante}*"+self.equivalente+')')
            elif funcion=='csc':
                self.equivalente='-scs('+self.variable+')cot('+self.variable
                return  print(f"{self.constante}*"+self.equivalente+')')
            else:
                return print("no es una función trigonométrica")
"""
Derivada de funciones exponenciales
"""
class Derivada_expo:
    def __init__(self,funcion,variable, constante=1):
        self.funcion=funcion
        self.variable=variable
        self.constante=constante
        if constante==1:
            if funcion=='exp':
                self.equivalente='exp('+self.variable
                return  print(self.equivalente+')')
            elif funcion=='log':
                self.equivalente='1/'+self.variable
                return print(self.equivalente)
        else:
            if funcion=='exp':
                self.equivalente='exp('+self.variable
                return  print(f"{self.constante}*"+self.equivalente+')')
            elif funcion=='log':
                self.equivalente='1/'+self.variable
                return print(f"{self.constante}*"+self.equivalente)
            else: 
                return print ("no es una función exponencial/logaritmica")
            
            
            
        
poli = Derivada_poli([3,2,1],'x')    
trigo=Derivada_trig_simple('cos', 'k',1) 
trigo2=Derivada_trig_simple('son', 'm',1)       
expo=Derivada_expo('log','x',4)
expo2=Derivada_expo('logi','s',4)