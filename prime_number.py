a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def prime_number(n):
    #for n in m:
    c=None
    if n < 2:
        print("{}は素数ではない".format(n))
    else:
        i=2
        while i*i <= n:
            if n%i == 0:
                c=1
                return False
                    #print("{}は素数ではない".format(n))
                    #b=1
                    #break
            i+=1
        if c!=1:
            return True    
                #print("{}は素数".format(n)) 

print(prime_number(int(a)))
print(prime_number(int(b)))