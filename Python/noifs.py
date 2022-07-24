def add(a,b):
    return a+b
def sub(a,b):
    return a-b
num1=int(input("enter the first num : "))
num2=int(input("enter the second num : "))

choice= int(input("enter 1 for addition and 2 for subtraction : "))
di={1:add, 2:sub}
res= di[choice](num1, num2)
print(res)