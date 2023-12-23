'''
Problema del FizzBuzz
Autor: Felipe Miranda Rebolledo
'''

#¡ Lista de numeros del 1 al 100
list = range(1,101)

'''
Para encontrar los números que son fizz, debemos iterar a través del array y comprobar qué números son Fizz y Buzz. Para ello
creamos un bucle for que recorra la lista de números y compruebe si el número es divisible por 3 o 5.
'''

#¡ Bucle for
for num in list:
    #? Si el numero es divisible por 3 y 5, entonces es FizzBuzz
    if num % 3 == 0 and num % 5 == 0: 
        print(f"{num} - FizzBuzz")
    #? Si el numero es divisible por 5, entonces es Buzz
    elif num % 5 == 0:
        print(f"{num} - Buzz")
    #? Si el numero es divisible por 3, entonces es Fizz
    elif num % 3 == 0:
        print(f"{num} - Fizz")
    else:
        print(num)
