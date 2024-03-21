from math import pi, sin
# --example--
# print(sin(0))
# >>> 0
# -----------
a=0
b=pi/2
N=100
h=(b-a)/N
x=0
for k in range(N):
    k=k+1
    x=x+(h*(sin(a+(k-1)*h)+sin(a+k*h)))/2
print(x)
print(k)    