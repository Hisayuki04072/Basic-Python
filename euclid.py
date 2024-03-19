a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a=int(a)
b=int(b)
r=a%b
while r!=0:    
    a=b
    b=r
    r=a%b
    if r==0:
        print(b)
        