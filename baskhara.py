import math

## -b +- Raiz (b² - 4 *a *c) / 2 * a

a = float(input("Digite o valor de a:"))
b = float (input("Digite o valor de b"))
c = float (input("Digite o valor de c"))
delta = (b ** 2) - (4 * a * c)

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(f"0 x1 é {x1} e o x2 {x2}")