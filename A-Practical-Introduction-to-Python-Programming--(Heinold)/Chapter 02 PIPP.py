######################################################################################
###         A Practical Introduction to Python Programming  (Heinold)              ###  
###                          Chapter 2  -For Loops-                                ###
######################################################################################



#--------  +++ Ejercicio 1 +++ -------------------------------------------------------------------------------

"""
Write a program that prints your name 100 times

"""


for i in range(100):
    print("Mauricio Moscote Alarcon")

    
#--------  +++ Ejercicio 2 +++ -------------------------------------------------------------------------------

"""
Write a program to fill the screen horizontally and vertically with your name.
 [Hint: add the option end='' into the print function to fill the screen horizontally.]

"""

for i in range(200):
    print("Mauricio Moscote Alarcon", end=" ")
    

#--------  +++ Ejercicio 3 +++ -------------------------------------------------------------------------------

"""
Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
output should look like the output below.
1 Your name
2 Your name
3 Your name
4 Your name
...
100 Your name

"""

for i in range(100):
    print(i+1, "Mauricio Moscote Alarcon")


#--------  +++ Ejercicio 4 +++ -------------------------------------------------------------------------------

"""
Write a program that prints out a list of the integers from 1 to 20 and their squares. The output
should look like this:
1 --- 1
2 --- 4
3 --- 9
...
20 --- 400

"""

for i in range(20):
    print( i+1,(i+1)*(i+1),sep=" ---- ")
    
    
for i in range(20):                         #  Segunda version
    print( i+1,(i+1)**2,sep=" ---- ")    

    

#--------  +++ Ejercicio 5 +++ -------------------------------------------------------------------------------

"""
Write a program that uses a for loop to print the numbers 
8, 11, 14, 17, 20, . . . , 83, 86, 89

"""


for i in range(8,90,3):
    print(i,end="  ")
print(end="\n")


#--------  +++ Ejercicio 6 +++ -------------------------------------------------------------------------------

"""
Write a program that uses a for loop to print the numbers 
100, 98, 96, . . . , 4, 2

"""

for i in range(100,1,-2):
    print(i,end="  ")
print(end="\n")


#--------  +++ Ejercicio 7 +++ -------------------------------------------------------------------------------

"""
Write a program that uses exactly four for loops to print the sequence of letters below.

AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

"""


for i in range(10):
    print("A",end="")
for i in range(7):
    print("B",end="")
for i in range(4):
    print("CD",end="")
print("E",end="")
for i in range(6):
    print("F",end="")
print("G",end="")
print(end="\n")



#--------  +++ Ejercicio 8 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user for their name and how many times to print it. 
The program should print out the user’s name the specified number of times.

"""


name = input("Ingrese su nombre: ")
number = eval(input("Ingrese las veces que quiere que su nombre se imprima en pantalla: "))
for i in range(number):
    print(name)
    

#--------  +++ Ejercicio 9 +++ -------------------------------------------------------------------------------
           
"""
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .

"""


print("+++++ Numeros de Fibonacci +++++",end="\n \n")
n = eval(input("Ingrese la cantidad de numeros de Fibonacci que desea que aparezcan en la pantalla: "))

a = 1
b = 0
c = 0
for i in range(n):
    print(a, end="  ")
    c = b
    b = a
    a = c + b
print(end="\n")



#--------  +++ Ejercicio 10 +++ -------------------------------------------------------------------------------

"""
Use a for loop to print a box like the one below. Allow the user to specify how wide 
and how high the box should be. [Hint: print('*'*10) prints ten asterisks.]

*******************
*******************
*******************
*******************

"""

b = eval(input("Ingrese el valor entero correspondiente al ancho de la caja: "))
h = eval(input("Ingrese el valor entero que corresponde al alto de la caja: "))
         
for i in range(h):
    print("*"*b)


#--------  +++ Ejercicio 11 +++ -------------------------------------------------------------------------------

"""
Use a for loop to print a box like the one below. Allow the user to specify how wide 
and how high the box should be.

*******************
*                 *
*                 *
*******************

"""


b = eval(input("Ingrese el ancho de la caja (cantidad de (*)): "))
h = eval(input("Ingrese la altura de la caja: "))
print("*" * b)
for i in range(h):
    print("*","*",sep=" " * (b-2))
print("*" * b)



#--------  +++ Ejercicio 12 +++ -------------------------------------------------------------------------------

"""
Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.

*
**
***
****

"""


h = eval(input("Ingrese la altura del triángulo (valor entero positivo): "))
for i in range(h):
    print("*" *(i+1))



#--------  +++ Ejercicio 13 +++ -------------------------------------------------------------------------------

"""
Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.

****
***
**
*

"""

h = eval(input("Ingrese la altura del triángulo invertido: "))
for i in range(h,0,-1):
    print("*" * i)



#--------  +++ Ejercicio 14 +++ -------------------------------------------------------------------------------

"""
Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

       *
      ***
     *****
    *******
     *****
      ***
       *

"""

n = eval(input("Ingrese la altura del diamante: "))
for i in range(n):
    print("-" * ((n-i)) ,"*" * (2 * i + 1),"-" * ((n-i)))
for i in range(n,-1,-1):
    print("-" * ((n-i)) ,"*" * (2 * i + 1),"-" * ((n-i)))
    


#--------  +++ Ejercicio 15 +++ -------------------------------------------------------------------------------

"""

Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.

     *
    * *
   *****
  *     *
 *       *

"""



# Ejercicio en construccion

n = eval(input("Ingrese la altura de la letra A: "))
print( end="\n")
for i in range(n - 3):
    print("-" * ((n-i)) ," " * (2 * i + 1),"-" * ((n-i)))
    
print("-"  * (2* n +  3))    
    

n = eval(input("Ingrese la altura del diamante: "))
for i in range(n):
    print("-" * ((n-i)) ,"*" * (2 * i + 1),"-" * ((n-i)))    
    