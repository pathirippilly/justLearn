##graph of sine and cosine
#x=np.arange(0,3*np.pi,0.1)
#y=np.sin(x)
#z=np.cos(x)
#plt.plot(x,y)
#plt.plot(x,z)
#plt.show()
#
#
##Exponential and log functions
#x=np.arange(1,10,1)
#print(np.exp(x))
#print(np.log(x))




#generating arrays
#A1=np.array([(1,2,3),(3,4,5)]) #converting list of two tuples in to 2*2 array
#A2=np.zeros((2,2),dtype=int)
#A3=np.arange(10,22,2,dtype=int)
#A4=np.reshape(A1,(3,2))
#A5=np.linspace(1,60,num=15,endpoint=True,retstep=True,dtype=int)
#A6=A1+A1
#A7=np.vstack((A6,A6))
#A8=np.eye(4)
#A9=np.random.randint(1,100,(5,5))
#A10=np.random.randn(5,5)
#A11=A9.copy()
#A12=np.arange(50).reshape(5,10)
#A13=A12[1:3,3:5]
#np.random.seed(10)
#A14=np.random.randint(10,101,(9,10))
#print(A14)
#print(A12)
#print(A13)
#print(f"{A1}\n\n{A2}\n\n{A3}\n\n{A4}")
#print(A1+A1)
#print(A6)
#A7[1][0]=1
#A7[1][1]=1
#print(A3.reshape(3,2))
#print(A1.shape,A1.size,A1.flags)
#print(A10)
#print(A3.reshape(3,2).argmax())
#print(A11)
#print(A11[:1:-1,:1:-1])
#print(A11[A11%2==0])

A1=np.array([1,2,3,4])
print(A1)

print(A1.transpose())

'''
A1=np.array([(1,2,3),(3,4,5)])
A2=np.array([(1,2,3),(3,4,5)])
#reshaping above array of 2 rows and 3 columns to array of 3 rows and 2 columns
print(A1.reshape(3,2))
#indexing and slicing
print(A1[0]) #print the 1st element
print(A1[0:,1]) #print the 2nd element for first and second row
print(A1[::-1]) #print the array in reverse ,same as list and tuple
#linesoace to create an array in Numpy
ar=np.linspace(1,60,num=15,endpoint=False,retstep=True,dtype=float)
print(ar)
#max,min and sum
print(A1.max())
print(A1.min())
print(A1.sum())
#Axis wise sum
print(A1.sum(axis=0)) #calculate column wise sum and return a single row
print(A1.sum(axis=0)) #calculate row wise sum and return a single column
#square root and standard deviation
print(np.sqrt(A1))#return an array of square root of each element
print(np.std(A1))#return the standard deviation of each element from the mean
#sum,div,mul and subtraction of A1 and A2
print(A1+A2)
print(A1/A2)
print(A1*A2)
print(A1-A2)
#Appending of A1 and A2 can be done by vertica stacking and horizontal stacking
print(np.vstack((A1,A2))) #append A2 vertically to A1
print(np.hstack((A1,A2))) #append A2 horizontally to A1
#two dimensional array in to a single column
print(A1.ravel())
'''

'''
#finding the Dimension
print(A1.ndim)
#find the bite size of each element
print(A1.itemsize)
#find the shape of the array
print(A1.shape)
#find the data type of an array
print(A1.dtype)
#find the size of an array
print(A1.size)
'''



'''
#Time consumption
SIZE=10000000
lst_1=range(SIZE)
lst_2=range(SIZE)

A1=np.arange(SIZE)
A2=np.arange(SIZE)

start_time=time.time()

result=[(x,y) for x,y in zip(lst_1,lst_2)]

print ((time.time()-start_time)*1000)

start_time=time.time()

result_np = A1+A2

print ((time.time()-start_time)*1000)
'''

'''Memory occupancy
#a = np.array([(1,2,3),(4,5,6)])
#print(a)

S=range(1000)
print(sys.getsizeof(5)*len(S))
c=np.arange(1000)
#print(len(S))
#print(len(c))
#print(sys.getsizeof(c[5]))
#print(sys.getsizeof(4))
#print(c.itemsize)
print(sys.getsizeof(5)*len(S))
print(c.itemsize*c.size)
'''









