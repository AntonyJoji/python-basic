import json

jdata ='''
{
  "people": [
    {
      "name": "devin",
      "phone": 1234567899,
      "email": "devin@gmail.com",
      "has_licence": true
    },
    {
      "name": "dainty",
      "phone": 1234444444,
      "email": "sdcsd@gmail.com",
      "has_licence": false
    },
    {
      "name": "sonu",
      "phone": 1233453444,
      "email": "sdfs@gmail.com",
      "has_licence": false
    },
    {
      "name": "manu",
      "phone": 123323424,
      "email": "efsds@gmail.com",
      "has_licence": true
    },{
      "name": "monu",
      "phone": 12342342424,
      "email": null,
      "has_licence": true
    }
  ]
}
'''
# data=json.loads(jdata)
# print(data)
# name = []
# for i in data['people']:
#    print (i['name'],i['phone'],i['email']) 


## to find the number of licence
# data=json.loads(jdata)
# count =0
# for i in data['people']:
#     if i['has_licence']==True:
#         count = count+1
# print(count)
 

####or###
# data=json.loads(jdata)
# count =sum([1 for p in data ['people']if p ['has_licence']])
# print(count)


######################
### find the the longest name ######
# data=json.loads(jdata)
# longest =max(data['people'],key=lambda p:len(p['name']))
# print(longest['name'])
# print(longest)

#####################################################################

# with open ('states.json') as f:
#     data = json.load(f)
#     print (data)
###################################################################
# import json
# with open ('states.json') as f:
#     data = json.load(f)
# names = [person["name"] for person in data["states"]]
# print(names)

# data = json.loads(jdata)
# for person in data ['people']:
#     del person['phone']
# newdata =json.dumps(data,indent=3,sort_keys=True) ## DUMPS conver to json string format
# print(newdata)

###dump save to json file

# import json

# with open('states.json') as f:
#     data = json.load(f)

# # Collect all names into a list
# val = [{'Names':i['name'] }for i in data['states']]

# # Save the list into a new file
# with open('statesname.json', 'w') as new_f:
#     json.dump(val, new_f, indent=2)


#################################################################

###to extract only those states whose areacode list has exactly ONE value.


# import json

# with open("states.json") as f:
#     data = json.load(f)  # <-- use load() not loads()

# # Select states with exactly one area code
# val = {'States': [i for i in data["states"] if len(i["areacode"]) == 1]}

# # Write to new JSON file
# with open("states1.json", 'w') as new_f:
#     json.dump(val, new_f, indent=2)



##########################################################################################

########## rename the key name to state_name

# import json

# with open("states.json")as f:
#     data =json.load(f)


# for state in data ['states']:
#    state['state_name']=state.pop('name')


# with open ("state_rename.json",'w') as new_f:
#     json.dump(data,new_f,indent=2)


# import json

# # Read file
# with open("states.json") as f:
#     data = json.load(f)

# # Delete the 'areacode' field
# for i in data["states"]:
#     del i["areacode"]

# # Write updated data to a new file
# with open("states3.json", "w") as newf:
#     json.dump(data, newf, indent=2)

# print("areacode removed and saved to states3.json")
      

######## CRUD - post,get,put,delete

# import requests as re
# res = re.get("https://jsonplaceholder.typicode.com/todos")
# with open('todos.json','w') as f:
#     f.write(res.text)

# import requests as re
# res = re.get("https://jsonplaceholder.typicode.com/todos")
# data = json.loads(res.text)
# with open('todos.json','w') as f:
#     json.dump(data,f,indent=2)








