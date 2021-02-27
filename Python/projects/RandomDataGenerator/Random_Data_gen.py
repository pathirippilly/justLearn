import sys
from random import random
from math import floor

def randomString():
	return ''.join([chr(floor(random()*(91-i))+65) for i in range(65,69)])
def randomElement():
	l=[1,91,92,850]
	return l[(floor(random()*(5-1))+1)-1]

idBeg=int(sys.argv[1])
idEnd=int(sys.argv[2])


def main(idBeg,idEnd):
	l=range(idBeg,idEnd)
	

	lines=[(str(x),randomString(),str(randomElement())) for x in l]

	with open("A:\\randomData.csv",'w') as f:
		for i in lines:
			f.write(','.join(i)+'\n')
if __name__=='__main__':
	main(idBeg,idEnd)





	
	