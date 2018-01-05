#!/usr/bin/env python
import os,pwd

file_list=os.listdir(os.getcwd())
filenames=[]
filenames=[ i for i in file_list if i.startswith(".sh_history") ]
users=[]
dates=[]
names=[]


#Generates arrays with usernames+dates
for x in filenames: 
 razdelen=x.split(".")
 users.append(razdelen[2])
 dates.append(razdelen[3])

names=[ pwd.getpwnam(i).pw_gecos for i in users ]
print str(names)

#Prints usernames + dates:
print "-----------------------------"
print "  User   |   Date  |  Name  | "
print "-----------------------------"

for x in xrange(len(filenames)):
 print "| %s | %s | %s |" % (users[x], dates[x], names[x])

print "--------------------"
#for i in file_list:
# if i.startswith(".sh_history"):
#  print i
#  filenames.append(i)

