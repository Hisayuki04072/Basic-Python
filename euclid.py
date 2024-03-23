a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a=int(a)
b=int(b)
#r=a%b
def euclid(a,b):
    r=a%b
    while True: 
        if r==0:
            return b
            #print(b)
            #break
        else:
            a=b
            b=r
            r=a%b
            

def relatively_prime(a,b):
    if (euclid(a,b))==1:
        return True
    else:
        return False

print(euclid(a,b))
print(relatively_prime(a,b))        