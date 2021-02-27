import re
from  itertools import groupbyr
phone_number=re.compile("[A-Za-z]+\s*[A-Za-z]*\n[89]\d{2}[-.]\d{3}[-.]\d{3}")
with open(r"A:\lab\data\Corey_Schafer\REGEX\Personal_Details.txt", "r") as f:
    contents=f.read()
    matches=phone_number.findall(contents)
    positions=phone_number.finditer(contents)
print(list(matches))
print([i.span() for i in positions])
emails="""dfcfcxzc#fvxc.com
ANJASndjd@gamil.com
jdbnsda.ksna@unty.net
dcfas-125-121-dsca@mm-sds.edu
"""
pattern=re.compile("[A-Za-z0-9.-]*@[A-Za-z-]*\.[A-Za-z]*")
pattern.
matches=pattern.findall(emails)
matches2=pattern.match(emails) # return the first match.
# But only check the beginning of the string for the match if we do not specify a start pos
matches3=pattern.search(emails) # return the first match. unlike .match() , it will search entire string

raise Exception()
print(matches3)
print(list(matches))

urls="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)') #groups can be captured in circular braces as here
matches=pattern.finditer(urls)
matches1=pattern.findall(urls) #tuple of all groups

print(matches1)
print([i.group(2)+ i.group(3) for i in matches]) # group(0) is always entire string , group(1) is the first group and so on
url1=pattern.sub(r'\2\3',urls) #replace the string with a concatenation of group1 and group2
print(url1)





