######################################################################################
###         A Practical Introduction to Python Programming  (Heinold)              ###
###                           Chapter 3  -Numbers-                                 ###
######################################################################################



#--------  +++ Ejercicio 1 +++ -------------------------------------------------------------------------------

"""
Write a program that generates and prints 50 random integers, each between 3 and 6

"""


from random import randint
for i in range (1,51):
    print(i, randint(3,6),sep="  ---  ")


#--------  +++ Ejercicio 2 +++ -------------------------------------------------------------------------------


"""
Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x^y

"""

from random import randint
x = randint(1,50)
y = randint(2,5)
print(x,y,x ** y,sep="   ")


#--------  +++ Ejercicio 3 +++ -------------------------------------------------------------------------------

"""
Write a program that generates a random number between 1 and 10 and prints your name
that many times.

"""

from random import randint
r = randint(1,10)
for i in range(1,r):
    print(i,"Mauricio Moscote Alarcon",sep=" -- ")


#--------  +++ Ejercicio 4 +++ -------------------------------------------------------------------------------

"""
Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00

"""


from random import uniform
R = uniform(1,10)                    # la funcion uniform(a,b) extrae aleatoriamente un valor del intervalo (a,b)
print(R, round(R,2), sep=" --- ")


#--------  +++ Ejercicio 5 +++ -------------------------------------------------------------------------------

"""
Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51

"""

from random import randint
for i in range (1,51):
    print(i, randint(1,i+1), sep=" --- ")


#--------  +++ Ejercicio 6 +++ -------------------------------------------------------------------------------


"""
Write a program that asks the user to enter two numbers, x and y, and computes 
|x - y| / (x+y)

"""

x = eval(input("Ingrese el primer número : "))
y = eval(input("Ingrese el segundo número : "))

if (x == 0 and y == 0):
    print("La operacion no puede realizarse.")
else:
    print((abs(x - y))/(x + y))


#--------  +++ Ejercicio 7 +++ -------------------------------------------------------------------------------
  
"""
Write a program that asks the user to enter an angle between -180º and 180º 
Using an expression with the modulo operator, convert the angle to its equivalent 
between 0º and 360º

"""

Angulo = eval(input("Ingrese un angulo entre -180 y 180 grados:  "))
print("El angulo equivalente entre los 0 y 360 grados es:  ", (Angulo + 360) % 360)


#--------  +++ Ejercicio 8 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. 
[Hint: Use the // operator to get minutes and the % operator to get seconds.]

"""

seg = eval(input("Ingrese la cantidad de segundos a convertir: "))
print("El tiempo corresponde a ",seg // 60, " minutos y ",seg % 60," segundos")


#--------  +++ Ejercicio 9 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.
An example is shown below

Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock

"""

Hora = eval(input("Ingrese la hora (valor entero entre 1 y 12): "))
Hora01 = eval(input("Ingrese la hora adelante en el futuro (entero entre 1 y 12): "))

Nueva_Hora = (Hora + Hora01)%12
if Nueva_Hora == 0:
    print("La nueva hora es ",12)
else:
    print("La nueva hora es ",Nueva_Hora)
   

#--------  +++ Ejercicio 10 +++ ------------------------------------------------------------------------------

"""
(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power

"""

x = eval(input("Ingrese un número entero positivo: "))
print("El resultado de elevar 2 a la potencia ", x, "es ", 2 ** x)
print("El último digito de elevar 2 a la potencia ", x, "es ", (2 ** x) % 10)




"""
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power

"""

y = eval(input("Ingrese un número entero positivo: "))
print("El resultado de elevar 2 a la potencia ", y, "es ", 2 ** y)
print("Los últimos dos dígitos de elevar 2 a la potencia ", y, "son ", (2 ** y) % 100)




"""
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.

"""


z = eval(input("Ingrese un número entero positivo: "))
print("El resultado de elevar 2 a la potencia ", z, "es ", 2 ** z)
w = eval(input("¿Cuántos dígitos de la potencia desea conocer? (entero positivo): "))
print("Los últimos", w , " dígitos de elevar 2 a la potencia ", z, "son ", (2 ** z) % (10 ** w))



#--------  +++ Ejercicio 11 +++ ------------------------------------------------------------------------------

"""
Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound

"""

kg = eval(input("Ingrese su peso en Kilogramos: "))
print("Su peso en libras es ", round(2.2 * kg, 2), sep="")



#--------  +++ Ejercicio 12 +++ ------------------------------------------------------------------------------

"""
Write a program that asks the user for a number and prints out the factorial 
of that number

"""


from math import factorial 
f = eval(input("Ingrese un número natural: "))    
print("El factorial de ", f, "es ",factorial(f))


f = eval(input("Ingrese un número natural: "))    # Calculo del factorial de un numero natural usando for loop
p = 1
for i in range(1,f+1):
    p = p*i
    
print("El Factorial de ", f, "es ", p)   



#--------  +++ Ejercicio 13 +++ ------------------------------------------------------------------------------

"""
Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number

"""


from math import *

q = eval(input("Ingrese un número real cualquiera: "))

print("sen(",q,")= ",sin(q))
print("cos(",q,")= ",cos(q))
print("tan(",q,")= ",tan(q))



#--------  +++ Ejercicio 14 +++ ------------------------------------------------------------------------------

"""
Write a program that asks the user to enter an angle in degrees and prints out the
sine of that angle

"""

from math import *
Angulo= eval(input("Ingrese el ángulo en grados sexagesimales: "))
Angulo_radianes = (pi * Angulo) / 180
print("El valor de sen(",Angulo,") es igual a ", round(sin(Angulo_radianes),5))



#--------  +++ Ejercicio 15 +++ ------------------------------------------------------------------------------

"""
Write a program that prints out the sine and cosine of the angles ranging from 0º to 345º
in 15º increments. Each result should be rounded to 4 decimal places. Sample output is shown
below:
    
0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659

"""

from math import *
for i in range(0,346,15):
    print(i,round(sin((pi * i) / 180), 4),round(cos((pi * i) / 180), 4), sep=" ---- ")



#--------  +++ Ejercicio 16 +++ ------------------------------------------------------------------------------

"""

Below is described how to find the date of Easter in any year. Despite its intimidating appearance,
this is not a hard problem. Note that [[x]] is the floor function, which for positive numbers
just drops the decimal part of the number. For instance [[3.14]] = 3. The floor function is part
of the math module

C = century (1900’s --> C = 19)
Y = year (all four digits)
m = (15 + C - [[C/4]] -  [[ (8C + 13) / 25]]) mod 30
n = (4 + C - [[C/4]]) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d = (19c + m) mod 30
e = (2a + 4b + 6d + n) mod 7

Easter is either March (22 + d + e) or April ( d + e - 9). There is an exception if d = 29 
and e = 6. In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
18. Write a program that asks the user to enter a year and prints out the date of Easter in that
year. (See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)

"""


Year = eval(input("Ingrese el año: "))

C = Year // 100                # C contiene las primeras dos cifras del año contenido en la variable Year
m = (15 + C - (C // 4) - (((8*C) + 13) // 25)) % 30
n = (4 + C - (C // 4)) % 7
a = Year % 4
b = Year % 7
c = Year % 19
d = ((19*c) + m) % 30
e = ((2*a) + (4*b) + (6*d) + n) % 7

print(C,m,n,a,b,c,d,e, sep=" -- ")
print(22+d+e)
print(d+e-9)




 
#--------  +++ Ejercicio 17 +++ ------------------------------------------------------------------------------


"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year

"""

Year = eval(input("Ingrese un año mayor a 1600: "))

s = 0
for i in range(1600, Year + 1):
    if (i % 4 == 0) or (i % 400 == 0):
        s = s + 1
        print(i,end= " ")

print(end="\n")
        
print("Hay un total de ",s, "años que son bisiestos desde 1600 hasta el año ", Year)   




#--------  +++ Ejercicio 18 +++ ------------------------------------------------------------------------------
     
"""
Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]

"""

Change = eval(input("Ingrese un valor entero entre 0 y 99: "))
# Change corresponde a la cantidad de dineo recibida inferior a $1.00
if (Change < 0 or Change > 99):
    print("Rango erroneo de cambio a convertir")

else:
      Quater = Change // 25         # $1.00 <--> 4 Quarters  
      Dime =   Change // 10         # $1.00 <--> 10 Dimes           
      Nickel = Change // 5          # $1.00 <--> 20 Nickels  
      Penny =  Change // 1          # $1.00 <--> 100 Pennies

print("Quater = ",Quater, "Dimes = ", Dime, "Nickel = ", Nickel, "Penny = ", Penny)



#--------  +++ Ejercicio 19 +++ ------------------------------------------------------------------------------

"""
Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 x 5
rectangle and a 4 x 8.

0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1


"""

A = eval(input("Ingrese el valor correspondiente al ancho del rectangulo: "))
H = eval(input("Ingese el valor del alto del rectangulo: "))
for j in range(0, (A * H),A):
    print("")
    for i in range(j,A + j):
        print(i % 10, end=" ")