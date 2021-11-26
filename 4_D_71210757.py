num1 = float(input("Masukkan bilangan 1: "))
num2 = float(input("Masukkan bilangan 2: "))
num3 = float(input("Masukkan bilangan 3: "))
if num1 > num2 > num3:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num2, num3)
elif num1 == num2 > num3:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num2, num3)
elif num1 > num2 == num3:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num2, num3)
elif num1 > num3 > num2:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num3, num2)
elif num1 == num3 > num2:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num3, num2)
elif num1 > num3 == num2:
    print("Urutan bilangan dari yang terbesar adalah ", num1, num3, num2)
elif num2 > num3 > num1:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num3, num1)
elif num2 == num3 > num1:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num3, num1)
elif num2 > num3 == num1:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num3, num1)
elif num2 > num1 > num3:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num1, num3)
elif num2 == num1 > num3:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num1, num3)
elif num2 > num1 == num3:
    print("Urutan bilangan dari yang terbesar adalah ", num2, num1, num3)
elif num3 > num2 > num1:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)
elif num3 == num2 > num1:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)
elif num3 > num2 == num1:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)
elif num3 > num1 > num2:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num1, num2)
elif num3 == num1 > num2:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)
elif num3 > num1 == num2:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)
else:
    print("Urutan bilangan dari yang terbesar adalah ", num3, num2, num1)