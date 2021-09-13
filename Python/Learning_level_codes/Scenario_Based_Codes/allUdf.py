#Return list of all possible sublist from a list as input
from multipledispatch import dispatch
from functools import wraps
from datetime import time.t
def wrapIt(func):
    @wraps()
    def wrapper(*args,**kwargs):
        t

@dispatch(list)
def getAllSublist(inpL):
    outL=[]
    for i in range(len(inpL)):
        for j in range(len(inpL)+1):
            outSubL=inpL[i:j]
            if outSubL:
                outL.append(outSubL)
    return outL

@dispatch(list,int)
def getAllSublist(inpL,k):
    outL=[]
    for i in range(len(inpL)):
        oddNumCounter=0
        for j in range(len(inpL)+1):
            outSubL=inpL[i:j]
            if outSubL:
                if outSubL[-1]%2!=0:
                    oddNumCounter+=1
                if oddNumCounter<=k:
                    outL.append(outSubL)
                else:
                    break
    return outL





