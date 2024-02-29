#This program shows the records of an employee
#Date : 22/02/2024
#Name : Isaac kiarie
#Employee records

n =input("Name :")
a =input("Age : ")
s =float(input("salary : "))
b =float(input("Bonus : "))

t = s + b 


print("Employee records : ",n) 
print("Age : ",a)
print("Salary : ",s)
print("Bonuses : ",b)
print("Total income :,",t)

s2 =(130/100 * s)
t2 = s2 + b
print("Employee's new bonus :",b)
print("Employee's final total income :",t2)