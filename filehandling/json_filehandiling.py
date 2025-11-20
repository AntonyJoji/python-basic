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
data=json.loads(jdata)
longest =max(data['people'],key=lambda p:len(p['name']))
print(longest['name'])