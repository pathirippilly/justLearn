def selectionSort(l):
    ln=len(l)
    swap=0
    itr=0

    for i in range(ln-1):
        n=0
        for j in range(i+1,ln):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
                swap=swap+1
                itr = itr+1

    return l,swap,itr

l=[1,5,9,2,7,4,8,3,6,4,5,8,9,7,4,6,3,5,2,6,4,4,2,4,5]
#l=[9,8,7,6,5,4,3,2,1]
out=selectionSort(l)
print("sorted_list:{}".format(out[0]))
print("number of swaps happened: {}".format(out[1]))
print("number of iterations happened: {}".format(out[2]))


