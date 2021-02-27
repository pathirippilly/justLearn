
x=['963174258',
'178325649',
'254689731',
'821437596',
'496852317',
'735961824',
'589713462',
'317246985',
'642598173']

y=['060104050',
'200000001',
'008305600',
'800407006',
'006000300',
'700901004',
'500000002',
'040508070',
'007206900']
l=[]
#for i in range(9):
#    l=list(x[i].strip())
#    for j in range(9):
#        if y[i][j]=='0':
#            l[j]='0'
#    x[i]=''.join(l)
 
for i in range(9):
    l = list(x[i].strip())
    for j in range(9):
        if y[i][j] != '0' and y[i][j] != x[i][j]:
            temp=l[j]
            ind= l.index(y[i][j])
            l[j]=l[ind]
            l[ind]=temp
    x[i]=''.join(l)

l=[[i,j] for i,j in zip(x,y)]

for i in l:
    print(i)

for i in range(9):
    print(f"column:{i+1}")
    for j in range(9):
        if x[j][i] in [x[k][i] for k in range(1,9) if k != j] and x[j][i] != y[j][i]:
            temp_list=[x[j][i],(j,i)]
            temp=x[j][i]
            

    
    
