######################################################################################
###         A Practical Introduction to Python Programming  (Heinold)              ###  
###                       Chapter 1  -Getting Started-                             ###
######################################################################################



#--------  +++ Ejercicio 1 +++ -------------------------------------------------------------------------------

"""
Print a box like the one below.

*******************
*******************
*******************
*******************

"""



print("*******************")                 # Variante 1
print("*******************")
print("*******************")
print("*******************")


for i in range(4):                           # Variante 2 (Uso loop for)
    print("*******************")
    
 
for i in range(4):                           # Variante 3 (Uso loop for --forma simplificada--)                   
    print("*" * 19)
    


#--------  +++ Ejercicio 2 +++ -------------------------------------------------------------------------------

"""
Print a box like the one below.

*******************
*                 *
*                 *
*******************

"""

print("*******************")
print("*                 *")
print("*                 *")
print("*******************")


print("*" * 19)                             # Variante 1 (Uso loop for)
for i in range(2):
    print("*", " " * 15, "*")    
print("*" * 19)    



#--------  +++ Ejercicio 3 +++ -------------------------------------------------------------------------------

"""
Print a triangle like the one below.

*
**
***
****    

"""

print("*")
print("**")
print("***")
print("****")


for i in range(4):                           # Variante 1 (Uso loop for)
    print("*" * (i+1))
    
    
#--------  +++ Ejercicio 4 +++ -------------------------------------------------------------------------------

""" 
Write a program that computes and prints the result of
512 -282/47.48+5. It is roughly .1017. 

"""

x = 512 - 282
y = (47*48) + 5
print(x / y)


#--------  +++ Ejercicio 5 +++ -------------------------------------------------------------------------------

"""
Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.

Enter a number: 5
The square of 5 is 25.

"""


x = eval(input("Ingrese un numero: "))
print("El cuadrado de ", x, " es ", x*x, ".", sep = " ")


#--------  +++ Ejercicio 6 +++ -------------------------------------------------------------------------------

"""
Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.

Enter a number: 7
7---14---21---28---35

"""
y = eval(input("Ingrese un numero: "))
print(y, 2*y, 3*y, 4*y, 5*y, sep = " --- ")


#--------  +++ Ejercicio 7 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user for a weight in kilograms and converts it to pounds. 
There are 2.2 pounds in a kilogram.

"""

kg = eval(input("Ingrese su peso en Kilogramos: "))
print("Su peso en libras es ", 2.2 * kg, ".", sep = " ")


#--------  +++ Ejercicio 8 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user to enter three numbers (use three separate input statements).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.

"""


x1 = eval(input("Ingrese el primer numero: "))
x2 = eval(input("Ingrese el segundo numero: "))
x3 = eval(input("Ingrese el tercer numero: "))
total = x1 + x2 + x3
print("La suma de las tres cantidades es ", total, " y el promedio de los tres numeros es ", round(total / 3, 3))


#--------  +++ Ejercicio 9 +++ -------------------------------------------------------------------------------

"""
A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.

"""


Valor_cena = eval(input("Ingrese el valor de la cena: $ "))
Propina = eval(input("Ingrese el valor porcentual de la propina (un numero entre 0 y 100): "))
print("La propina es de $", (Valor_cena * Propina)/ 100, " y el costo total de la cena es de: $",Valor_cena + (Valor_cena * Propina) / 100)
