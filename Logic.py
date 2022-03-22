import numpy as np
from PIL import Image




def AND(input_image1,input_image2):
    img1 = input_image1.resize((400,400), Image.ANTIALIAS)
    img_array1 = np.array(img1)

    img2 = input_image2.resize((400,400), Image.ANTIALIAS)
    img_array2 = np.array(img2)
    print(img_array2)

    # Logic AND
    and_image = img_array1*img_array2
    and_image = np.multiply(img_array1,img_array2)
    print(and_image.shape)
     
    print(type(and_image))
    
    Output_image = Image.fromarray(and_image)  
    images = []
    images.append(img1)
    images.append(img2)
    images.append(Output_image)
    return images

def OR(input_image1,input_image2):
    img1 = input_image1.resize((400,400), Image.ANTIALIAS)
    img_array1 = np.array(img1)

    img2 = input_image2.resize((400,400), Image.ANTIALIAS)
    img_array2 = np.array(img2)

    # Logic OR
    and_image = img_array1+img_array2
    print(and_image.shape)
     
    print(type(and_image))
    
    Output_image = Image.fromarray(and_image)  
    images = []
    images.append(img1)
    images.append(img2)
    images.append(Output_image)
    return images

def XOR(input_image1,input_image2):
    img1 = input_image1.resize((400,400), Image.ANTIALIAS)
    img_array1 = np.array(img1)

    img2 = input_image2.resize((400,400), Image.ANTIALIAS)
    img_array2 = np.array(img2)

    # Logic XOR
    and_image = np.logical_xor(img_array1,img_array2) 
    print(and_image.shape)
     
    print(type(and_image))
    
    Output_image = Image.fromarray(and_image)  
    images = []
    images.append(img1)
    images.append(img2)
    images.append(Output_image)
    return images