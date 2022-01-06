def countUptoMax(num):
    count=1
    while count<=num:
        yield count
        count+=1

c=countUptoMax(10)
print(next(c))
print(next(c))
print("\n")
for i in c:
    print (i)
    
    
    