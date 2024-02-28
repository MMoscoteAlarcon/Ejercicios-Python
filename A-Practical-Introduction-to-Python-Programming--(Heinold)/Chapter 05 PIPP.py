######################################################################################
###         A Practical Introduction to Python Programming  (Heinold)              ###
###                    Chapter 5  -Miscellaneous topics I-                         ###
######################################################################################



#--------  +++ Ejercicio 1 +++ -------------------------------------------------------------------------------


"""


"""


count = 0
for i in range(1,101):
    if (i**2)%10 == 1:
        count = count + 1
        print(i**2, end=" ")
print(end="\n")        
print("Hay", count, "números entre 1**2 y 100**2 que terminan en 1")   



#--------  +++ Ejercicio 2 +++ -------------------------------------------------------------------------------


count1 = 0
count2 = 0

for i in range(1,101):
    if (i**2)%10 == 4:
        count1 = count1 + 1
        print(i**2,end=" ")
print(end="\n")        
for j in range(1,101):
    if (j**2)%10 == 9:
        count2 = count2 + 1
        print(j**2,end=" ")
print(end="\n")  
      
print("Hay", count1, "números entre 1**2 y 100**2 que terminan en 4")  
print(end="\n")     
print("Hay", count2, "números entre 1**2 y 100**2 que terminan en 9")  
           


#--------  +++ Ejercicio 3 +++ -------------------------------------------------------------------------------


from math import *
s = 0
n = eval(input("Ingrese un número entero positivo n :  "))

if n<=0:
    print("Valor numérico no válido ")
else:
    for i in range(1,n+1):
        s = s + (1/i)

print("Suma:  ", s) 
print(end="\n")
print("Log(n) : ",log(n))
print(end="\n")       
print("Suma - Log(n) : ",s - log(n))        
    


#--------  +++ Ejercicio 4 +++ -------------------------------------------------------------------------------


S = 0
for i in range(1,2001):
    S = S + ((-1)**(i-1))*i
print("1 - 2 + 3 - 4 +.... + 1999 - 2000  =  ",S)    
     



#--------  +++ Ejercicio 5 +++ -------------------------------------------------------------------------------


Sum = 0
N = eval(input("Ingrese un número entero positivo:  "))
if N <= 0:
    print("Valor no válido")
else:
   for i in range(1,N+1):
       if N%i == 0:
           Sum = Sum + i
           print(i,end=" ")
        
   print(end="\n")        
   print("La Suma de los divisores de ",N, " es igual a ", Sum)
   



#--------  +++ Ejercicio 6 +++ -------------------------------------------------------------------------------


def SumDiv(N):
    Sum = 0
    for i in range(1,N):
       if N%i == 0:
           Sum = Sum + i
    return Sum


print(SumDiv(28))

for j in range(1,10001):
    if SumDiv(j) == j:
        print(j,end=" ")
        
        
        

#--------  +++ Ejercicio 7 +++ -------------------------------------------------------------------------------


Num = eval(input("Ingrese un número natural:  "))

Flag = 0
if Num <= 0:
    print("Valor ingresado no válido")
else:
   for i in range(1,Num+1):
       if i!=1 and Num%i == 0 and int(i**(0.5))**2 == i:    # De los tres criterios, el último expresa que un número no es cuadrado perfecto
             Flag = 1 
             print(i,Flag)      
             
if Flag == 1:
    print(Num," posee al menos un divisor cuadrado perfecto distinto de 1")
else:
    print(Num," no posee divisores cuadrados perfectos distintos de 1")
    
    
    
#--------  +++ Ejercicio 8 +++ -------------------------------------------------------------------------------
    


X = eval(input("Ingrese un valor numérico para la variable X =  "))
Y = eval(input("Ingrese un valor numérico para la variable Y =  "))
Z = eval(input("Ingrese un valor numérico para la variable Z =  "))

X,Y = Y,X
X,Z = Z,X

print("X = ", X)
print("Y = ", Y)
print("Z = ", Z)



#--------  +++ Ejercicio 9 +++ -------------------------------------------------------------------------------

count01 = 0
count02 = 0
count03 = 0

for i in range (1,1001):
    if int(i**(0.5))**2 != i:
         count01 = count01 + 1
         print(i,end=" ")
         
print(end="\n")   

for j in range (1,1001):
    if int(j**((1. / 3.)))**3 != j:
         count02 = count02 + 1
         print(j,end=" ")
         
print(end="\n")

for k in range (1,1001):
    if int(k**(0.2))**5 != k:
         count03 = count03 + 1
         print(k,end=" ")
         
print(end="\n")  

print("Hay", count01, "números entre 1 y 1000 que no son cuadrados perfectos")  
print(end="\n")     
print("Hay", count02, "números entre 1 y 1000 que no son cubos perfectos")         
print(end="\n")
print("Hay", count03, "números entre 1 y 1000 que no son perfectas potencias quintas")





#--------  +++ Ejercicio 10 +++ ------------------------------------------------------------------------------



