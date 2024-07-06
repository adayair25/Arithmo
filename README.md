# Arithmo 

#### Arithmo is a programing lengauge that is designed to be simple and easy to use. It is a high-level language that is designed to be easy to read and write math problems. 

### Arithmo example code
#### En nuestro lenguaje la declaración de variables es simple solamente basta con escribir el nombre de la palabra `var` seguido del tipo de dato  y posterior el nombre de la variable y puede ser opcional; la manera en la que inicializa.
```javascript
var x: srg = "Hello World"; 
```
### Tambien se pueden declarar variables que no se les haya asignado un valor del mismo tipo en una sola linea, como se muestra en el siguiente ejemplo.
```javascript
var x,y: int;
```

##### En caso de las constantes su declaracion es similar a la de las variables, solo que en vez de la palabra `var` se utiliza `const` y el valor de la constante no puede ser cambiado.
```javascript
const x: int = 10;
```
### En nuestro lenguaje se pueden realizar operaciones aritmeticas de manera sencilla, como se muestra en el siguiente ejemplo.
```java
var x: int = 10 + 10 ; salida: 20 
```
### El lenguaje permite el uso de diferentes tipos de datos, a continuacion se indica la manera en la que usar cada uno:
* `int` : entero
* `flt` : flotante
* `srg` : cadena
* `bool` : booleano
* `dbl` : doble 

### funciones:
#### En nuestro lenguaje la declaración de funciones es simple solamente basta con escribir el nombre de la palabra `fn` posterior el nombre de la función
```rust
fn suma(a: int, b: int): int {
    return a + b;
}
```
### Operadores: 
#### Arithmo esta estandarizado en el uso de operadores basicos tales como: 
* `+` : adición
* `-` : sustraccion 
* `*` : multiplicacion
* `/` : division
* `=` : asignacion
* `==` : comparacion
* `!=` : diferente
* `>` : mayor que
* `<` : menor que
* `>=` : mayor o igual que
* `<=` : menor o igual que
* `%` : modulo
* `\` : raiz
* `^` : potencia 
* `&&` : and
* `||` : or
* `!` : not
* `++` : incremento
* `--` : decremento


###  Estrucuturas de datos:
Arithmo perimite el uso de estructuras de datos convencionals como lo son:
* `[]` : array 
* `{}` : diccionario
* `[][]` : matriz

### Bucles:
#### Asi se veria un par de ciclos
```javascript
while () {
    var x: int = 0;
    while x < 10 {
        x++;
    }
}

do {
    var x: int = 0;
    while x < 10 {
        x++;
    }
} while ();

for (var i: int = 0; i < 10; i++) {
    print(i);
}
```

### Condiciones:
#### Asi se veria una condicion
```javascript
if (x == 10) {
    print("x es igual a 10");
} else if (x != 10) {
    print("x no es igual a 10");
} else {
    return 0;
}

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

### Palabras reservadas: