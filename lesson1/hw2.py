# ax**2 + bx + c = 0
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b**2 - 4 * a * c
x1 = (-b + D**0.5)/2 * a
x2 = (-b -D**0.5)/2 * a
show = f"x1 = {x1}; x2 = {x2}"
print(show)
