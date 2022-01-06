def sum_nums_gen(num):
    def sums(*args,**kwargs):
        return sum(x for x in range(1,num+1))
    return sums

a=sum_nums_gen(5)
print(a())

def squr(num):
    