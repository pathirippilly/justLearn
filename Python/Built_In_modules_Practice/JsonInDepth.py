import json
import gc


people_string='''
{
"people": [
{"name":"Jhon Smith",
"phone":"615-555-7164",
"emails":["jhonsmith@bogusemail.com","john.smith@work-place.com"],
"has_license":false
},
{"name":"Jan Doe",
"phone":"560-555-5153",
"emails": null,
"has_license":true
}
]
}
'''

js=json.loads(people_string) #converts json string to dict
print(js)

for i in js["people"]:
    del i["phone"]
print(js)
new_string=json.dumps(js,indent=2,sort_keys=True) #converts dict to json string


gc.