def richiesta():
    n=int(input("Dammi un numero: "))

    return n


def fibonacci(n):
    fibonacci=[0,1]

    if n == 0:
        print(fibonacci[0])
    elif n == 1:
        print(fibonacci)
        
    else:
        f=0
        while True:
            f=fibonacci[-1]+fibonacci[-2]
            if f<n:
                fibonacci.append(f)
            else:
                break

    print(fibonacci)         





n=richiesta()

fibonacci(n)