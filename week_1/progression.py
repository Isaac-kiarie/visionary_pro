#This program is calculate terms on a sequence
#Date : 22/02/2024
#Name : Isaac kiarie 
import math 
#arithmetic sequence
a =int(input("The first term of the sequence :"))
n =int(input("The number of sequence :"))
d =int(input("The common diff :"))

an =a+(n-1)*d

print("The term in the arithmetic :",an)

#Geometric sequence

a = int(input("The first term of sequence  :"))
n = int(input("The number of sequence :"))
r = int(input("The common ratio :"))

ar =a*r**(n-1)

print("The term in the geometric :",ar)