# Arithmo 

<p>Arithmo es un lenguaje de programación de alto nivel que está diseñado para ser simple y fácil de usar para leer y escribir problemas matemáticos.
</p>

## Guía de inicio

<p>En Arithmo, la declaración de variables es simple, solamente basta con escribir el nombre de la palabra `var` seguido del tipo de datos y posteriormente, el nombre de la variable:
</p>

```javascript
var x = "Hello World"; 
```
<p>En el caso de querer llamar a la variable anteriormente declarada, se utiliza la siguiente sintaxis:

```javascript
x;  // Salida: "Hello World"
```

<p>Para obtener derivadas simples, como las trigonométricas, de polinomio o exponenciales, se llaman de la siguiente manera:

```javascript
global_deriv([1,2,3],constants=2,y); // Salida: (2)*(2x^0)+(2)*(6x^1)
```

```javascript
global_deriv(cos,constants=1,y); // Salida: -sin(y)
```

</p>

<p>En el caso de derivadas de la cadena, suma, producto o cociente, es como sigue:

```javascript
deriv_gen(chain,z,[1,2,4],cos); // Salida: (2cos(z)^0+8cos(z)^1)*-sin(z)
```
</p>

## Tipos de datos

<p>El lenguaje permite el uso de diferentes tipos de datos:
</p>

* `int` : entero
* `flt` : flotante
* `srg` : cadena
* `bool` : booleano
* `dbl` : doble 


## Operadores

<p>Arithmo está estandarizado en el uso de operadores básicos, tales como:
</p>

* `+` : adición
* `-` : sustracción 
* `*` : multiplicación
* `/` : división
* `=` : asignación
* `==` : comparación
* `!=` : diferente
* `>` : mayor que
* `<` : menor que
* `>=` : mayor o igual que
* `<=` : menor o igual que
* `%` : módulo
* `\` : raíz
* `^` : potencia 
* `&&` : and
* `||` : or
* `!` : not
* `++` : incremento
* `--` : decremento

##  Estrucuturas de datos

<p>El lenguaje permite el uso de estructuras de datos convencionales como lo son:
</p>

* `[]` : array 
* `{}` : diccionario
* `[][]` : matriz

## Palabras reservadas

<p>Las palabras reservadas de Arithmo se mencionan como sigue, y <b>éstas no deben ser utizadas para nombrar variables</b>:
</p>

* `var` : variable
* `fn` : función
* `if` : condición
* `else` : condición
* `while` : ciclo
* `do` : ciclo
* `for` : ciclo
* `switch` : condición
* `case` : condición
* `deft` : condición
* `continue` : condición
* `break` : condición
* `return` : condición
* `print` : imprimir
* `int` : entero
* `flt` : flotante
* `srg` : cadena
* `bool` : booleano
* `dbl` : doble
* `true` : verdadero
* `false` : falso
* `++` : incremento
* `--` : decremento
* `*` : multiplicación
* `/` : división
* `==` : comparación
* `!=` : diferente
* `>=` : mayor o igual que
* `<=` : menor o igual que
* `%` : módulo
* `\` : raíz
* `^` : potencia
* `&&` : and
* `||` : or
* `!` : not
* `[]` : array
* `{}` : diccionario
* `[][]` : matriz