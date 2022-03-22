from scipy import fftpack
import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw




def Erosion(input_image,Kernel_value):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    img_array = np.array(img)
    kernel = np.ones((Kernel_value,Kernel_value),np.uint8)
    erosion = cv.erode(img_array,kernel,iterations = 1)
    Output_image = Image.fromarray(erosion)  
    images = []
    images.append(img)
    images.append(Output_image)
    return images

def Dilation(input_image,Kernel_value):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    img_array = np.array(img)
    kernel = np.ones((Kernel_value,Kernel_value),np.uint8)
    dilation = cv.dilate(img_array,kernel,iterations = 1)
    Output_image = Image.fromarray(dilation)  
    images = []
    images.append(img)
    images.append(Output_image)

    return images

def Open(input_image,Kernel_value):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    img_array = np.array(img)
    kernel = np.ones((Kernel_value,Kernel_value),np.uint8)
    opening = cv.morphologyEx(img_array,cv.MORPH_OPEN,kernel)
    Output_image = Image.fromarray(opening)  
    images = []
    images.append(img)
    images.append(Output_image)

    return images
    
def Close(input_image,Kernel_value):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    img_array = np.array(img)
    kernel = np.ones((Kernel_value,Kernel_value),np.uint8)
    closing = cv.morphologyEx(img_array,cv.MORPH_CLOSE,kernel)
    Output_image = Image.fromarray(closing)  
    images = []
    images.append(img)
    images.append(Output_image)
    return images

def MG(input_image,Kernel_value):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    img_array = np.array(img)
    kernel = np.ones((Kernel_value,Kernel_value),np.uint8)
    closing = cv.morphologyEx(img_array,cv.MORPH_GRADIENT,kernel)
    Output_image = Image.fromarray(closing)  
    images = []
    images.append(img)
    images.append(Output_image)


    return images




