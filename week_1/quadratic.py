#program to solve the quadratic equation
#Date:20/2/2024
#Nmae :Isac kiarie
import math

a = float (input ("Enter the coefficient of fisrt term:") )
b = float(input ("Enter the coefficient of second term:") )
c = float(input ("Enter the  constant :") )

d = (float(b)**2) - 4 * (float (a))  * (float(c))
        
x_1 = ((-b + math.sqrt(d)) / 2 * a)
x_2 = ((-b + math.sqrt(d)) / 2 * a)

print("The solution of the quadratic equation :",x_1)
print("The solution of the quadratic equation :",x_2)

