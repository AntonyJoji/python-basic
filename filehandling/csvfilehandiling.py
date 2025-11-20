# import csv 
# with open ('dataone.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    # print(csv_reader)

    # for row in csv_reader:
    #     print(row)
    # print(next(csv_reader))/

# import csv  ## complete data write at same time 
# with open ('dataone.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('newdataone.csv','w') as new_file:
#         csv_writer =csv.writer(new_file)
#         csv_writer.writerows(csv_reader)




# import csv  ## row by row writing data
# with open ('dataone.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('newdata2.csv','w') as new_file:
#         csv_writer =csv.writer(new_file)
#         for line in csv_reader:
#             csv_writer.writerows(line)


# import csv ## it will skip first line and write in the new file 
# with open('dataone.csv','r') as csv_file:
#     csv_reader =csv.reader(csv_file)
#     with open('newdata3.csv','w') as new_file:
#         csv_writer = csv.writer(new_file)
#         print(next(csv_reader))
#         for line in csv_reader:
#             csv_writer.writerow(line)


# import csv
# with open ('dataone.csv','r') as csv_file,open ('firstname.csv','w') as new_file:
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader:
#             new_file.write(row[0]+'\n')



# import csv
# with open ('dataone.csv','r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         names =[]
#         for row in csv_reader:
#             full_name = row[0]+ '  '  + row[1]
#             names.append(full_name)
#         print(names)


# import csv
# with open ('dataone.csv','r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader:
#                 if "devin"in row[2]:
#                         print("user:-",row)


import csv

# data = [
#     ["Name", "age", "city"],
#     ["alice", "25", "new york"],
#     ["bob", "30", "LA"]
# ]

# with open("da.csv", 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(data)


# with open("dataone.csv", 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     print(csv_reader)
#     for i in csv_reader:
#         print (i)



# with open("dataone.csv", 'r') as csv_file:
#     csv_reader= csv.DictReader(csv_file)
#     for i in csv_reader:
#         print(i)


# import csv

# emails = []

# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)  

#     for row in csv_reader:
#         emails.append(row["email"])       

# print(emails)

# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)  
#     with open('one_one.csv','w') as new_file:
#         fieldname =['fname','lname','email']
#         csv_writer = csv.DictWriter(new_file,fieldnames=fieldname,delimiter=';')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)


# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)  
#     with open('one_one2.csv','w') as new_file:
#         fieldname =['fname','lname','email']
#         csv_writer = csv.DictWriter(new_file,fieldnames=fieldname,delimiter=';')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             if line['fname'].startswith('a'):
#                 csv_writer.writerow(line)

###to find gmail users ############

# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)  
#     with open('one_one3.csv','w') as new_file:
#         fieldname =['fname','lname','email']
#         csv_writer = csv.DictWriter(new_file,fieldnames=fieldname,delimiter=';')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             if line['email'].endswith('gmail.com'):
#                 csv_writer.writerow(line)


### only for email #####

import csv

# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open("gmail_only.csv", "w") as new_file:
#         new_file.write("email\n")   # write header

#         for line in csv_reader:
#             if line['email'].endswith('@gmail.com'):   # only gmail users
#                 new_file.write(line['email'] + "\n")   # write only email
 ## or

# with open("dataone.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)  
#     with open('gmail_only1.csv','w') as new_file:
#         fieldname =['email']
#         csv_writer = csv.DictWriter(new_file,fieldnames=fieldname,delimiter=';')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             if line['email'].endswith('gmail.com'):
#                 csv_writer.writerow({'email':line['email']})








