import math as m

#Getting sides
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

#triangle check
if a + b < c and a + c < b and b + c < a:
    print("this is not a triangle")
    exit()
elif (a + b == c) or (a + c == b) or (b + c == a):
    print("this is a line, not a triangle")
    exit()
#CALCULATIONS:

#perimeter/ semi-perimeter
per = a + b + c
print("Perimeter/Obvod: ", per)
s_per = per/2
print("Semi-perimeter/Polovičný obvod: ", s_per)

#area
ar = m.sqrt(s_per * (s_per - a) * (s_per - b) * (s_per - c))
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

#inradius
r = ar/s_per
print("Inradius: ", r)

#circumradius
R = (a*b*c)/(4*ar)
print("Circumradius: ", R)

#tringle types
if a==b==c:
    print("Trojuholnik je rovnostranny")
elif (a==b) or (b==c) or (c==a):
    print("Trojuholnik je rovnoramenny")

if aa == 90 or ab == 90 or ac == 90:
    print("Trojuholnik je pravouhly")
elif aa < 90 and ab < 90 and ac < 90:
    print("Trojuholnik je ostrouhly")
elif aa > 90 or ab > 90 or ac > 90:
    print("Trojuhlonik je Tupouhly")
