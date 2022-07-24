
def atm():
    bal = 12000
    print("Welcome to XYZ BANK \nEnter Your Card")
    amount=float(input("Enter Amount to WIthdraw"))
    if amount>bal:
        raise ValueError("Insufficient Balance")
    else:
        bal -= amount
        print(f"Upated Bal = {bal}")


try:
    atm()
except BaseException as be:
    print(be)
