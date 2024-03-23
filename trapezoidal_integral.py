from math import pi,sin,e
# --example--
# print(sin(0))
# >>> 0
# -----------
#a=0
#b=pi/2
#N=100
#h=(b-a)/N
def trapezoidal_integral(f,a=0,b=1,n=100):
    x=0.0
    h=(b-a)/n
    for k in range(n):
        k=k+1
        x=x+(h*(f(a+(k-1)*h)+f(a+k*h)))/2
    return x    

def func1(x):
    return 4/(1+x**2)

def func2(x):
    return (pi**(1/2))*(e**(-x**2))

print(trapezoidal_integral(sin,0,pi/2.0,50))
print(trapezoidal_integral(func1,0,1,100))
print(trapezoidal_integral(func2,-100,100,1000))
