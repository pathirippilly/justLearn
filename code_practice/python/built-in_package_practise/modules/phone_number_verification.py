import re
phn_str=['123-345-5678','123-345-567','23-345-5678','123-35-5678','123-345-56789','974-506-0076']
for i in phn_str:
    if(re.findall('\d{3}-\d{3}-\d{4}',i)==[i]):
        print(i," : its a valid phone number")
    else :
         print(i," : its an invalid phone number")
    