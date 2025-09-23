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

#medians
ma = 1/2 * m.sqrt(2*(b**2) + 2*(c**2) - a**2)
mb = 1/2 * m.sqrt(2*(a**2) + 2*(c**2) - b**2)
mc = 1/2 * m.sqrt(2*(b**2) + 2*(a**2) + c**2)

print(f"Medians/Tiažnice: a={ma}, b={mb}, c={mc}")

#altitudes
ha = (2*ar)/a
hb = (2*ar)/b
hc = (2*ar)/c

print(f"Altitudes/Výšky: Va={ha}, Vb={hb}, Vc={hc}")

#angles
aa = m.degrees(m.acos(((b**2)+(c**2)-(a**2))/(2*b*c)))
ab = m.degrees(m.acos(((a**2)+(c**2)-(b**2))/(2*a*c)))
ac = m.degrees(m.acos(((a**2)+(b**2)-(c**2))/(2*b*a)))

print(f"Angles/Uhly (Degrees/Stupne): α:{aa}, β:{ab}, γ:{ac}")