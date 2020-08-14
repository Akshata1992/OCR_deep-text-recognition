# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:16:48 2020

@author: Shruti
"""
import glob
import os

#print(glob.glob("D:/LincodeLabsInternship-CatalerProject/Stage1/OCR/ClovaaiModel/2/training/*.png")) #Gives the whole path along with filename.
path_ = 'E:/LincodeLabs/OCR_BiLSTM/OCR_evaluate/test/*'
#file_name_list = next(os.walk('E:\LincodeLabs\OCR_BiLSTM\train'))[2] #gives only filenames

file_name_list = [os.path.basename(x) for x in glob.glob(path_)] 
#print(file_name_list)		

file_path_list = glob.glob("E:\LincodeLabs\OCR_BiLSTM\OCR_evaluate/test\\*")
#print(file_path_list)
#print(file_name_list)

#to get labels out of each of the filenames
file_name_list1 = []
file_name_list2 = []
'''for i in file_name_list :
    file_name_list1.append(i.split('_')[-1])
    print(file_name_list1)

for j in file_name_list1 :    
    if j.find('JPG')
        file_name_list2.append(j.split('.')[0])'''
        
for i in file_name_list :    
    if 'jpg' in i :
        file_name_list1.append(i.split('_')[1])
    elif 'png' in i :
        file_name_list1.append(i.split('_')[0])
    elif 'jpeg' in i :
        file_name_list1.append(i.split('_')[1])
#print(file_name_list1)

for j in file_name_list1 :    
    file_name_list2.append(j.split('.')[0])
print(file_name_list2)

#print(len(file_name_list2))
i = 0
with open("E:\\LincodeLabs\\gt_test_1.txt", "w") as f:   # Opens file and casts as f 
    for path in file_path_list :
        #print(file)
        f.write("{}\t{}\n".format(path,file_name_list2[i]))
        i+=1

    