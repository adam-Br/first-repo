import math as m

#Getting sides
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

#triangle check
if a + b < c:
    print("the sum of sides a and b cannot be less than c")
    exit()
#CALCULATIONS:

#perimeter/ semi-perimeter
per = a + b + c
print("Perimeter/Obvod: ", per)
s_per = per/2
print("Semi-perimeter/Polovičný obvod: ", s_per)

#area
ar = float(m.sqrt(s_per * (s_per - a) * (s_per - b) * (s_per - c)))
print("Area/Obsah: ", ar)

#altitudes
ha = 1/2 * m.sqrt(2*(b**2) + 2*(c**2) - a**2)
hb = 1/2 * m.sqrt(2*(a**2) + 2*(c**2) - b**2)
hc = 1/2 * m.sqrt(2*(b**2) + 2*(a**2) + c**2)

print(f"Altitudes/Výšky: a={ha}, b={hb}, c={hc}")

