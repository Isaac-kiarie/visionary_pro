age=25
if age > 18 :
    print("You are allowed to drive")

salary=45000
if salary > 30000 or salary < 50000 :
    salary =salary * 0.1 + salary
    print(salary)

home_county = "nairobi"

if home_county == "nairobi" or home_county==  "nakuru":
    print("You get a bursary")

grade =70
if grade >= 84 and grade <= 90:
    print("You win a calculator")
elif  grade >=50 and grade <= 83:
    print("You win mathematical set")
else :
    print("You get nothing !")

salary=int(input("Enter employee's salary"))

if salary > 150000 :
    salary=1.05 * salary
    print(salary)

elif salary >= 100000 and salary <= 150000 :
    salary=1.15 * salary
    print(salary)
else :
    salary=1.3 * salary
    print(salary)



    


