#Return list of all possible sublist from a list as input
def getAllSublist(inpL):
    outL=[]
    for i in range(len(inpL)):
        for j in range(len(inpL)+1):
            outSubL=inpL[i:j]
            if outSubL:
                outL.append(outSubL)
    return outL