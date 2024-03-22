a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
for n in [int(a),int(b)]:
    if n < 2:
        print("{}は素数ではない".format(n))
    else:
        i=2
        while i*i <= n:
            if n%i == 0:
                print("{}は素数ではない".format(n))
                b=1
                break
            i+=1
        if b!=1:    
            print("{}は素数".format(n)) 
