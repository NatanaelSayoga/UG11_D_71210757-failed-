num1 = float(input("a : "))
num2 = float(input("b : "))
num3 = float(input("c : "))
D = num2**2 - 4*num1*num3
x1 = (-1*num2 + (num2**2 - 4*num1*num3)**0.5)/(2*num1)
x2 = (-1*num2 - (num2**2 - 4*num1*num3)**0.5)/(2*num1)
if D > 0:
    print("Akar-akar dari persamaan tersebut adalah " + str(x1) + " dan " + str(x2))
elif D == 0:
    print("Fungsi tersebut memiliki akar kembar yaitu " + str(x1))
else:
    print("Fungsi tersebut tidak memiliki akar riil")