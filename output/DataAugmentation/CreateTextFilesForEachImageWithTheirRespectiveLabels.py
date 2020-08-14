# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:16:48 2020

@author: Shruti
"""
import glob
import os

#print(glob.glob("D:/LincodeLabsInternship-CatalerProject/Stage1/OCR/ClovaaiModel/2/training/*.png")) #Gives the whole path along with filename.
file_name_list = next(os.walk('E:\BatchWiseData\FilteredData\Output'))[2] #gives only filenames
file_path_list = glob.glob("E:\\BatchWiseData\\FilteredData\\Output\\*")
print(len(file_path_list))
#print(file_name_list)

#to get labels out of each of the filenames
file_name_list1 = []
file_name_list2 = []

#print(file_name_list1)
for i in file_name_list :    
    file_name_list1.append(i.split('.')[0])
    
#print(file_name_list1)

for j in file_name_list1 :    
    file_name_list2.append(j.split('_')[2])

#print(file_name_list2)

i = 0
with open("E:\\LincodeLabs\\gt_filter_test.txt", "w") as f:   # Opens file and casts as f 
    for path in file_path_list :
        #print(file)
        f.write("{}\t{}\n".format(path,file_name_list2[i]))
        i+=1
        
print(i)
    