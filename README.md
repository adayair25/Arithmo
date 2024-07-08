# Arithmo 

<p>Arithmo es un lenguaje de programación de alto nivel que está diseñado para ser simple y fácil de usar para leer y escribir problemas matemáticos.
</p>

## Guía de inicio

<p>En Arithmo, la declaración de variables es simple, solamente basta con escribir el nombre de la palabra `var` seguido del tipo de datos y posteriormente, el nombre de la variable (es opcional si se quiere inicializar):
</p>

```javascript
var x: srg = "Hello World"; 
```

<p>Tambien se pueden declarar variables que no se les haya asignado un valor del mismo tipo en una sola línea:
</p>

```javascript
var x,y: int;
```

<p>En el caso de las constantes su declaración es similar a la de las variables, solo que en lugar de la palabra `var` se utiliza `const` y el valor de la constante no puede ser modificado:
</p>

```javascript
const x: int = 10;
```

<p>En Arithmo se pueden realizar operaciones aritméticas de manera sencilla, como se muestra a continuación:
</p>

```javascript
var x: int = 10 + 10; //salida: 20 
```

## Tipos de datos

<p>El lenguaje permite el uso de diferentes tipos de datos:
</p>

* `int` : entero
* `flt` : flotante
* `srg` : cadena
* `bool` : booleano
* `dbl` : doble 

## Funciones

<p>En Arithmo, la declaración de funciones es simple,con solo escribir el nombre de la palabra reservada `fn`, posteriormente, el nombre de la función:
</p>

```javascript
fn suma(a: int, b: int): int {
    return a + b;
}
```

## Operadores

<p>El lenguaje está estandarizado en el uso de operadores básicos, tales como:
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

<p>Arithmo permite el uso de estructuras de datos convencionales como lo son:
</p>

* `[]` : array 
* `{}` : diccionario
* `[][]` : matriz

## Bucles
<p>El lenguaje declara de esta forma los ciclos:
</p>

* `while`

```javascript
while () {
    var x: int = 0;
    while x < 10 {
        x++;
    }
}
```

* `do while`

```javascript
do {
    var x: int = 0;
    while x < 10 {
        x++;
    }
} while ();
```

* `for`

```javascript
for (var i: int = 0; i < 10; i++) {
    print(i);
}
```

## Condicionales
<p>Arithmo define dos condicionales de la siguiente manera:
</p>

* `if else`

```javascript
if (x == 10) {
    print("x es igual a 10");
} else if (x != 10) {
    print("x no es igual a 10");
} else {
    return 0;
}
```

* `switch`

```javascript
switch (x) {
    case 1:
        print("x es igual a 1");
        continue;
    case 2:
        print("x es igual a 2");
        continue;
    deft:
        print("x no es igual a 1 o 2");
        break;
}
```

## Palabras reservadas

<p>Las palabras reservadas de Arithmo se mencionan como sigue, y <b>éstas no deben ser utizadas para nombrar variables</b>:
</p>

* `var` : variable
* `const` : constante
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