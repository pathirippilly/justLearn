class Board:
    numbers=[]
    
    def __init__(self,inp=[]):
        numbers=[]
        if all([True if type(x)==str else False for x in inp])==True:
                
            for i in range(len(inp)):
                l=list(inp[i].strip())
                numbers.append(l)
        elif all([True if type(x)==list else False for x in inp])==True:
            numbers=inp
            
    def rotate(self):
        r=[[0 for x in range(9)] for x in range(9)]
        
        fromrow=list(range(9))
        fromcol=list(range(9))
        torow=list(range(8,-1,-1))
        tocol=list(range(9))
        for row in zip(fromrow,torow):
            for col in zip(fromcol,tocol):
                r[row[1]][col[1]]=self.numbers[row[0]][col[0]]
        return Board(r)
    def swapCols(self,first,second):
        toReturn=Board(self.numbers)
        for row in range(9):
            temp = self.numbers[row][first]
            self.numbers[row][first] = self.numbers[row][second]
            self.numbers[row][second] = temp
        return toReturn;
     
    def swapRows(self,first,second):
        toReturn=Board(self.numbers)
        for col in range(9):
            temp = self.numbers[first][col]
            self.numbers[first][col] = self.numbers[second][col]
            self.numbers[second][col] = temp
        return toReturn;
    
    def swapRowSections(self,first,second):
        toReturn=Board(self.numbers)
        
        for row in range(3):
            for col in range(9):
                temp = self.numbers[row][first*3 + col]
                self.numbers[row][first*3 + col] = self.numbers[row][second*3 + col]
                self.numbers[row][second*3 + col] = temp

        return toReturn;
    
    def swapColSections(self,first,second):
        
        toReturn=Board(self.numbers)
        
        for col in range(3):
            for row in range(9):
                temp = self.numbers[first*3 + row][col]
                self.numbers[first*3 + row][col] = self.numbers[second*3 + row][col]
                self.numbers[second*3 + row][col] = temp

        return toReturn;




b=Board()




#from random import randint
#
#lr=[[0 for x in range(9)] for x in range(9)]
#l=[[randint(1,9) for x in range(9)] for x in range(9)]
#fromrow=list(range(9))
#fromcol=list(range(9))
#torow=list(range(8,-1,-1))
#tocol=list(range(9))
#for row in zip(fromrow,torow):
#    for col in zip(fromcol,tocol):
#                lr[row[1]][col[1]]=l[row[0]][col[0]]
#for i in l:
#    print(i)
#print("\n")
#for i in lr:
#    print(i)
