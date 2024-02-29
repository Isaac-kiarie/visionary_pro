#This program is for a dictionary
#Dated :28\02\2024
#Name : Isaac kiarie 

My_laptop ={"make":"lenovo","colour":"black","weight":"2.5","year":"2020"}

for key, value in  My_laptop.items():
    print(key)
    print("\n")
    print(value)
My_laptop["colour"] = "yellow"
My_laptop["year"] = "2023"
print(My_laptop["make"])
print(My_laptop["weight"])
print(My_laptop["colour"])

My_laptop["size"] = "1200mm x600mm"
print(My_laptop)
del My_laptop["colour"]
print(My_laptop)

siz_laptop = My_laptop.copy
print(siz_laptop)

my_car=