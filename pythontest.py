#!/usr/bin/env python
import os

file_list=os.listdir(os.getcwd())
array=[]

for i in file_list:
 if i.startswith(".sh_history"):
  print i
  array.append(i)

