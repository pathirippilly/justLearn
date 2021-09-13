def fibonacci(n):
    n1=0
    n2=1
    counter=1
    while counter<=n:
        if counter==1:
            yield n1
        elif counter==2:
            yield n2
        else:
            nth=n1+n2
            yield nth
            n1=n2
            n2=nth
        counter+=1
print(list(fibonacci(10)))
