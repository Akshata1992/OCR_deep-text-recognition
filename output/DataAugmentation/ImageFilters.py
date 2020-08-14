#Apply Image filters
import glob
import cv2
from PIL import Image, ImageOps


#Collect all output images to apply filters
out_dir = 'E:/LincodeLabs/FIlter_classifier/Good_prediction/Train/augment/*'
outimg_ls = glob.glob(out_dir)
#print(outimg_ls)
alpha = 1.3 # Contrast control (1.0-3.0)
beta = 5 # Brightness control (0-100)
count = 1
#def imagefilter(newword)
for img in outimg_ls:
    #print(img)
    image = cv2.imread(img)
    image = cv2.GaussianBlur(image,(11,11),0)
    image = cv2.medianBlur(image,13)
    """
    image = cv2.blur(image,(5,5))
    #image = cv2.bilateralFilter(image,9,75,75)
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    """
    #image = ImageOps.mirror(image)
    #image  = cv2.flip(image, 1)
    cv2.imwrite("E:/LincodeLabs/FIlter_classifier/Good_prediction/Train/Blur/{}.png".format(img[63:-4]),image)
