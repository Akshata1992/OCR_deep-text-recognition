import random
import string
import PIL
import glob
import cv2
import numpy as np
from PIL import ImageOps
from PIL import ImageFilter
from PIL import Image
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from tqdm import tqdm
from resizeimage import resizeimage

# get a list of characters and numbers to be used in creating dataset
char_list = []
for char in string.ascii_uppercase:
    char_list.append(char)
	
for num in string.digits:
    char_list.append(num)

	
#Get list of background images
col_dir = 'E:/LincodeLabs/filter*.jpg'
img_ls = glob.glob(col_dir)

#Calculate contrast of background image
def ImgContrast(image):
    img = cv2.imread(image)
    Y = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0]

    # compute min and max of Y
    min = np.min(Y)
    max = np.max(Y)

    # compute contrast
    contrast = (max-min)/(max+min)
    return contrast
    
# get font list
font_lst = ['msyi'] 
font_size = 50
# generate images for each fonts

for fonts in font_lst:
    for i in tqdm(range(100)):
        for image in img_ls:
            contrastValue = ImgContrast(image)
            j = 1
            for i in range(len(char_list)):
                word_size = 1

				#random.randrange(4:5)
                char_list_copy = char_list.copy()
                char_list_copy.remove(char_list[i])
                new_word = char_list[i]
                for _ in range(word_size):
                    new_word +=random.choice(char_list_copy)
				
				#filter image -1
                if contrastValue > 1.0 and contrastValue < 2.0:
                    fontColor = (130, 108, 85)
                    Greybackground = False
				#filter image -2
                elif contrastValue > 0.0 and contrastValue < 0.9:
                    fontColor = (67, 54, 45)
                    Greybackground = False
				#filter image -4
                elif contrastValue > 2.0 and contrastValue < 2.5:
                    fontColor = (137, 138, 133)
                    Greybackground = False
				#filter Image -5
                elif contrastValue > 0.9 and contrastValue < 1.0:
                    fontColor = (127, 115, 93)
                    Greybackground = False	
                #filter image -3					
                else:
                    fontColor = (80, 80, 64)
                    Greybackground = True
                font = ImageFont.truetype(fonts+".ttf",font_size)
                font_ = ImageFont.truetype(fonts+".ttf",52) 
                img = Image.open(image)
                draw = ImageDraw.Draw(img)
                (w,h) = draw.textsize(new_word,font)
                img = img.resize((w+20,h+20))
                draw = ImageDraw.Draw(img)
                draw.text((5,7),new_word,(0,0,0),font=font_)
                #draw.text((28,12),new_word,(0,0,0),font=font_)
                if Greybackground == True:
                    draw.text((5,6),new_word,(61, 59, 58),font=font_)
                else:
                    draw.text((5,8),new_word,(255,255,255),font=font_)					
                draw.text((5,8),new_word,fontColor,font=font_)
                img.save('E:/BatchWiseData/Batch11/batch11_{}_{}.jpg'.format(j,new_word))
                j = j+1
"""
# Open text file to write in gt file
f = open('gt.txt','w')
gt_dir = 'E:\data\OCR*.png'
gtimg_ls = glob.glob(gt_dir)
for image in gtimg_ls:
    #img = image[3:]
    f.write(image+'	'+image[12:-4]+"\n")
    #f.close()
"""
				
                

