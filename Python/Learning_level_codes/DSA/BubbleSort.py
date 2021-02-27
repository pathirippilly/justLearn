def bubbleSort(l):
    ln=len(l)
    swap=0
    itr=0
    swap_happened=True
    while swap_happened:
        swap_happened=False
        itr=itr+1
        for i in range(ln-1):
            if l[i]>l[i+1]:
                tmp=l[i]
                l[i]=l[i+1]
                l[i+1]=tmp
                swap=swap+1
                swap_happened = True
            itr = itr + 1
        ln=ln-1
    return l,swap,itr
l=[1,5,9,2,7,4,8,3,6,4,5,8,9,7,4,6,3,5,2,6,4,4,2,4,5]
out=tuple(bubbleSort(l))
print("sorted_list:{}".format(out[0]))
print("number of swaps happened: {}".format(out[1]))
print("number of iterations happened: {}".format(out[2]))
