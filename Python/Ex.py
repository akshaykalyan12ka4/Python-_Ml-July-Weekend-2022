def add():
    x = int(input("Enter Number1:"))
    y = int(input("Enter Number2:"))


    s1 = x+y
    s2 = x-y
    s3 = x*y
    s4 = x/y

try:
    add()
    

except BaseException as be:
    print(f"Exception Occured= {be}")

finally:
    add()