######################################################################################
###         A Practical Introduction to Python Programming  (Heinold)              ###
###                         Chapter 4  -IF Statements-                             ###
######################################################################################



#--------  +++ Ejercicio 1 +++ -------------------------------------------------------------------------------


"""
Write a program that asks the user to enter a length in centimeters. 
If the user enters a negative length, the program should tell the user 
that the entry is invalid. Otherwise, the program should convert the 
length to inches and print out the result. There are 2.54 centimeters in an
inch.


"""


cm = eval(input("Ingrese la medida en centimetros a convertir a pulgadas: "))
if cm < 0.0:
    print("La cantidad es negativa. No puede convertirse a pulgadas")
else:
    print("La medida en pulgadas es ",round(cm / 2.54, 3))




#--------  +++ Ejercicio 2 +++ -------------------------------------------------------------------------------

"""
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, 
the temperature is in. Your program should convert the temperature to the other unit. 
The conversions are 


F = (9/5)C + 32   and 

C = (5/9) (F - 32)

"""


Temp = eval(input("Ingrese la temperatura a convertir: "))
opcion = eval(input("Escoja la unidad de temperatura a ser convertida: (1)Celsius   (2)Fahrenheit   "  ))

if opcion == 1:
    print("La temperatura en grados Fahrenheit es ", round(((9/5)*Temp) + 32, 3))
elif opcion == 2:
    print("La temperatura en grados Celsius es ", round((5/9)*(Temp - 32), 3))
else:
    print("Opcion erronea.")



#--------  +++ Ejercicio 3 +++ -------------------------------------------------------------------------------

"""
Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
    
• If the temperature is less than -273.15, print that the temperature is invalid because it is
  below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point.

"""


Temp = eval(input("Ingrese la temperatura en grados Celsius: "))
if Temp < -273.15:
    print("Rango de temperatura no correcto")
elif Temp == -273.15:
    print("Esa temperatura corresponde al cero absoluto")
elif  -273.15 < Temp < 0.0:
    print("Esa temperatura esta por debajo del nivel de congelacion")
elif Temp == 0.0:
    print("Esta temperatura corresponde al punto de congelacion")
elif 0.0 < Temp < 100:
    print("Esta temperatura esta en el rango normal")
elif Temp == 100:
    print("Esta temperatura corresponde al punto de ebullicion ")
else:
    print("Temperatura por encima del punto de ebullicion")




#--------  +++ Ejercicio 4 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user how many credits they have taken. If they 
have taken 23 or less, print that the student is a freshman. If they have taken
between 24 and 53, print that they are a sophomore. The range for juniors 
is 54 to 83, and for seniors it is 84 and over.

"""


Credits = eval(input("How many University credits have You take? "))
if Credits <= 0:
    print("Wrong number of credits")
elif 0 < Credits <= 23:
    print("You are a Freshman student")
elif 24 <= Credits < 53:
    print("You are a sophomore student")
elif 53 <= Credits < 83:
    print("You are a junior student")
else:
    print("You are a senior student")



#--------  +++ Ejercicio 5 +++ -------------------------------------------------------------------------------

"""
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.

"""


from random import randint
num = randint(1,10)
guess = eval(input("Ingrese un número entero entre 1 y 10: "))
if guess == num:
    print("Haz adivinado el número")
else:
    print("No has adivinado el numero generado aleatoriamente por la maquina. ese número es ",num)



#--------  +++ Ejercicio 6 +++ -------------------------------------------------------------------------------

"""
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. 
Write a program that asks the user how many items they are buying and prints the total cost

"""


item = eval(input("Ingrese la cantidad de articulos comprados: "))
if item < 0:
    print("Cantidad no correcta de articulos")
elif 0 <= item < 10:
    print("Dado que la cantidad de articulos es ",item, " el costo total es ",12 * item," dolares ($12/unidad)")
elif 10 <= item <= 99:
    print("Dado que la cantidad de articulos es ",item, " el costo total es ",10 * item," dolares ($10/unidad)")
else:
    print("Dado que la cantidad de articulos es ",item, " el costo total es ",7 * item," dolares ($7/unidad)")



#--------  +++ Ejercicio 7 +++ -------------------------------------------------------------------------------

"""
Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise

"""

x1 = eval(input("Ingrese el primer número: "))
x2 = eval(input("Ingrese el segundo número: "))
if abs(x1 - x2) <= 0.001:
    print(x1," y ",x2," son cercanos (su diferencia es inferior a 0.001)")
else:
    print(x1," y ",x2," no son cercanos (su diferencia es mayor a 0.001)")


#--------  +++ Ejercicio 8 +++ -------------------------------------------------------------------------------

"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 
are not leap years unless they are also divisible by 400. Write a program that asks 
the user for a year and prints out whether it is a leap year or not

"""


Year = eval(input("Ingrese un año: "))
if Year < 0.0:
    print("Valor de año equivocado")
else:
    if Year % 4 == 0 or Year % 400 ==0:
        print("El año ",Year, " es bisiesto")
    else:
        print("El año ", Year, " no es bisiesto")
        
        

#--------  +++ Ejercicio 9 +++ -------------------------------------------------------------------------------
    
"""
Write a program that asks the user to enter a number and prints out all the divisors of 
that number. 
[Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]

"""

Num = eval(input("Ingrese un número entero positivo: "))
if Num <= 0.0:
    print("Expresión numérica no válida")
else:
    print("Los divisores de ", Num,"son los siguientes: " )
    print(end="\n")
    for i in range (1, Num + 1):
        if Num % i == 0:
            print(i,end=" ")            
print(end="\n")  



#--------  +++ Ejercicio 10 +++ ------------------------------------------------------------------------------

"""
Write a multiplication game program for kids. The program should give the player 
ten randomly generated multiplication questions to do. After each, the program 
should tell them whether they got it right or wrong and what the correct answer is.


Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.

"""          

from random import  randint

question = 0

for question in range(10):
    a = randint(1, 10)
    b = randint(1, 10)
    print(" Pregunta ",question + 1, ": ", a ," x ",b, " = ? ")
    solution = eval(input("Ingrese la solucion de la multiplicacion:  "))

    if(solution == (a * b)):
      print("Muy bien")
    else:
       print("El valor de ", solution, " es equivocado. El resultado correcto es ", a * b)

    question += 1
    
    

#--------  +++ Ejercicio 11 +++ ------------------------------------------------------------------------------

"""
Write a program that asks the user for an hour between 1 and 12, asks them to enter
am or pm, and asks them how many hours into the future they want to go. 
Print out what the hour will be that many hours into the future, printing am or pm 
as appropriate. An example is shown below.


Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm

"""


Hora = eval(input("Ingrese una hora entre 1 y 12: "))
opcion = eval(input("Escoja el horario : (1)A.M.   (2)P.M.   "  ))
Hora_Futuro = eval(input("Ingrese las horas en el futuro: "))

Nueva_Hora = (Hora + Hora_Futuro) % 12

if opcion == 1:
    if Hora + Hora_Futuro < 12:
       print("La nueva hora es: ",Nueva_Hora, " A.M." )
    elif Hora + Hora_Futuro == 12:
       print("La nueva hora es: ",12, "del dia")
    else:
       print("La nueva hora es: ",Nueva_Hora, " P.M." ) 
    
else:
    if Hora + Hora_Futuro < 12:
       print("La nueva hora es: ",Nueva_Hora, " P.M." )
    elif Hora + Hora_Futuro == 12:
       print("La nueva hora es: ",12, "de la noche")
    else:
       print("La nueva hora es: ",Nueva_Hora, " A.M." ) 
  
    
#--------  +++ Ejercicio 12 +++ ------------------------------------------------------------------------------
    
"""
A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
how much candy is in the bowl, then you win all the candy. You ask the person in charge the
following: If the candy is divided evenly among 5 people, how many pieces would be left
over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
are less than 200 pieces. Write a program to determine how many pieces are in the bowl.


"""
  
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")
    break  


#--------  +++ Ejercicio 13 +++ ------------------------------------------------------------------------------
    
"""
Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie

"""

from random import  randint
game = 0

rock = 1
paper =2
scissors =3
wins =0
loose =0


for game in range(5):
    print("Game",game,"Start")

    my_hand = eval(input("Choose Rock , paper or scissors: "))
    computer_hand = randint(1, 3)
    if my_hand == computer_hand :
        print ("You and Computer Played the same hand its a tie..")
    elif my_hand == rock and computer_hand == scissors:
        print("Yay I crushed the computer scissors")
        wins += 1
    elif my_hand == rock and computer_hand == paper:
        print("Oops Computer Cover my Rock")
        loose += 1
    elif my_hand == paper and computer_hand == rock:
        print("Yay!! I covered computer rock haha")
        wins += 1
    elif  my_hand == paper and computer_hand == scissors:
        print("Oops Computer cut me up into piece")
        loose += 1
    elif my_hand == scissors and computer_hand == rock:
        print("Oops Computer Shattered My scissors")
        loose += 1
    elif my_hand == scissors and computer_hand == paper:
        print("Yay I cut up computer paper into pieces")
        wins += 1

if wins > loose:
    print("You win ", "You Scored ",wins,"Computer Scored",loose)

else:
    print("You loosed Try Again")
