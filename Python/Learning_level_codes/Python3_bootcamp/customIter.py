class counter:
	def __init__(self,high,low):
		self.current=high
		self.low=low
	def __iter__(self):
		return self
	def __next__(self):
		if self.current<self.low:
			num = self.current
			self.current +=1
			return num
		raise StopIteration 
		
def myFor(iterable,func):
		
		iter(iterable)
		while True:
			try:
				
			    it=next(iterable)
			
			except StopIteration:
				break
			else:
				func(it)
#myFor (counter(10,20),print)
c=counter(10,20)
print(list(c))
