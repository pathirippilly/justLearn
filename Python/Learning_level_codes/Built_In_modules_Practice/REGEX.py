import re
strn='we need to inform him the latest information'
strn1='12Sat 12mat rat1234 hat1234'
strn2='rat hat cat mat'
strn3='\\iniesta'
randstr='''
hi whats the weather today
looks like sunny
have a good day
'''


randstr1='123456789'
randstr2='123 1234 12345 123456 123457 12345678 123456789 @'
#searching for a string
print ((re.search('inform',strn)).span())
print(strn.index('inform'))

#finding all matches
print(re.findall('inform',strn))
print((strn[strn.find('inform'):(strn.find('inform')+len('inform'))]))

#find starting and ending index of the matching object
for i in re.finditer('inform',strn):
    print (i.span())
#find one on any of several letters(basically a pattern)
print(re.findall('[Shmp]at',strn1))

#match series of range of characters
print(re.findall('[aA-zZ]at',strn1)) #match all the words/strings starting with an alpha (irrespective of case) and ending with string 'at'
print(re.findall('[aA-zZ]at[0-9][0-9]*',strn1)) #match all the words/strings starting with an alpha (irrespective of case) , having the string 'at' and ending with a number
print(re.findall('[0-9][0-9]*[aA-zZ]at',strn1))#match all the words/strings starting with a number , having the string 'at' prefixed by atleast  an alphabet and ending with a number
print(re.findall('[^0-9]',strn1))#match all the words/strings which are not in the given range

#replace a string
strn2 = re.compile("[r]at").sub("food",strn2) #replace rat with food
print(strn2)
print(re.search(r'\\iniesta',strn3)) #use r to include all backslash
#how to deal with white spaces..etc
print (randstr)#simply print the string
randstr=re.compile('\n').sub(' ',randstr)#replace new line with white space
print (randstr)#print the replaced string
#\b=backspace
#\f=formfeed
#\r=carriage return
#\t=tab
#\v=vertical tab

#Match a single character
print(re.findall('\D',randstr1))#This will return everything except a number

print(re.findall('\d',randstr1))#This will return everything that is a number
print(re.findall('\d{3}',randstr1))#this will exactly matches all  combinations  with 3 numbers in it and return as a list
print(re.findall('\d{3,5}',randstr2))#this will return all number combinations in sequence which is having 3 to 5 number of digits
print(re.findall('\w{3,5}',randstr2)) # \w  equals [a-zA-Z0-9_]  and here it return as previous example
print(re.findall('\W{1}',randstr2))#\W equals [^a-zA-Z0-9_] and here it return all matches with atleast 1 occurance

#apart from this
# \s equals [\f\n\r\t\v]
# \S equals [^\f\n\r\t\v]