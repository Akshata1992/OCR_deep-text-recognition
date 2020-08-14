#Apply Image filters
import glob
f = open('gt_filter_train.txt','w')
#28
#26
gt_dir = 'E:\BatchWiseData\FilteredData\filterImg_input\*'
gtimg_ls = glob.glob(gt_dir)
#print(gtimg_ls)
for image in gtimg_ls:
    print(image)
    f.write(image+'	'+image[46:-4]+"\n")
    #f.close()