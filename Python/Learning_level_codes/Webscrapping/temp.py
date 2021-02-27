
    N = int(input())
    l=[]
    for _ in range(N):
        action,*sublist=input().split()
        sublist=[int(x) for x in sublist if len(sublist)>0]
        if action!='print':
           exec("l.{}(*sublist)".format(action))
        else:
            print(l)


    def repeating(c):
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j and a[i] == a[j]:
                    break
