# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:46:32 2020

@author: Shruti
"""


import os
import glob

file_name_list = next(os.walk('E:\BatchWiseData\FilteredData\dummy\\'))[2] #gives only filenames
file_path_list = glob.glob("E:\BatchWiseData\FilteredData\dummy\\*")
directory = 'E:\BatchWiseData\FilteredData\dummy\\'

label_position = 2 #position where the label name exists when we use split underscore (_)
batch_number = 1 #batch number for the set of images.
image_no_starting_pos = 1

#print(file_name_list)
#print(file_path_list)

file_name_list1 = []
file_name_list2 = []
file_format_list = []

for file in file_name_list :
    file_name_list1.append(file.split('.')[0])
    file_format_list.append(file.split('.')[1])
    
#print(file_name_list1)
#print(file_format_list)

for file in file_name_list1 :
    file_name_list2.append(file.split('_')[1])
    
print(file_name_list2)

image_number = image_no_starting_pos
i = 0
for file in file_name_list2 :
    new_file = directory+"batch"+str(batch_number)+"_"+str(image_number)+"_"+file_name_list2[i]+"."+file_format_list[i]
    old_file = file_path_list[i]
    os.rename(old_file, new_file)
    image_number = image_number+1
    i+=1
    
print(i)
