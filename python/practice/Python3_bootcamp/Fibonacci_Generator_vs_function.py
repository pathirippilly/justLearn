#Fibonacci series using a normal function
def fib(max):
    fib_list=[]
    a,b=0,1
    while len(fib_list)<max:
        fib_list.append(b)
        a,b=b,a+b
    return fib_list

#fibonacci series using a generator
def fib_gen(max):
    count,a,b=0,0,1
    while count<max:
        yield b
        a,b=b,a+b
        count+=1
        
#print(fib(10))
#print(list(fib_gen(10)))

for i in fib_gen(10000):
    print (i)
        