class fibonacci:
 def __init__(self,outbound=1):
  self.outbound=outbound
 def __iter__(self):
  self.n=1
  self.prev=1
  self.current=1
  return self
 def __next__(self):
  if self.n<=self.outbound:
   if self.outbound==0:
    raise StopIteration
   elif self.n<=2:
    self.n=self.n+1
    return self.current
   else:
    self.out = self.prev + self.current
    self.prev,self.current=self.current,self.out
    self.n=self.n+1
    return self.out
  else:
   raise StopIteration

a=fibonacci(50)

for i in a:
    print(i)