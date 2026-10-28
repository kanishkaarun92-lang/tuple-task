"""
#Tuple search
a = (101,202,303,404)
target = 303
index=0
for i in a:
    if i == target:
        print("element found at index:",index)
  index = index + 1
    
# tuple sorting
a = (50,10,40,20,30)
result = sorted(a)
print(tuple(result))

# find maximun , minimum
a = (15,82,24,95,23)
max = a[0]
min = a[0]
for i in a:
    if i > max:
        max = i
    if  i < min:
        min = i
print("max:",max)
print("min:",min)


# count the duplicate
a = (10,20,10,30,20,10)
for i in set(a):
    print(i,":",a.count(i))

#remove duplicate values
a = (1,2,2,3,4,4,5)
result = tuple(set(a))
print(result)

# tuple comparsion
a = (1,2,3)
b = (3,2,1)
print(set(a)==set(b))

#find common element
a = (10,20,30,40)
b = (30,40,50,60)
for i in a:
    if i in b:
        print(i)

#student ranking
marks= (78,92,85,88,95,60)
a = sorted(marks,reverse = True)
print(a[:3])

#Tuple of Employee Record
employees = (("E101","Arun",45000),("E102","Priya",95000),("E103","Kumar",48000))
highest_salary = employees[0]
for emp in employees:
    if highest_salary[2]<emp[2]:
        highest_salary=emp
print(highest_salary)
"""
#Sort Employee Records
employees = (("E101","Arun",45000),("E102","Priya",95000),("E103","Kumar",48000))
sorted_salary = employees
for emp in employees:
     result=sorted_salary
     sorted_salary 
print(sorted_salary)
