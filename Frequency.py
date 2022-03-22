from scipy import fftpack
import numpy as np

from PIL import Image, ImageDraw


def frequency_image(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    image_array = np.array(img)
    fft1 = fftpack.fftshift(fftpack.fft2(image_array))
    magnitude_spectrum = 20*np.log(np.abs(fft1))
    freq_image = Image.fromarray(magnitude_spectrum)  
    freq_image = freq_image.convert("L")
    output = []
    output.append(img)
    output.append(freq_image)
    return output



def low_pass_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    #convert image to numpy array
    image1_np=np.array(img)
    #fft of image
    fft1 = fftpack.fftshift(fftpack.fft2(image1_np))
    #Create a low pass filter image
    x,y = image1_np.shape[0],image1_np.shape[1]

    #defining filter
    #size of circle
    e_x,e_y=50,50
    #create a box 
    bbox=((x/2)-(e_x/2),(y/2)-(e_y/2),(x/2)+(e_x/2),(y/2)+(e_y/2))
    low_pass=Image.new("L",(image1_np.shape[0],image1_np.shape[1]),color=0)
    draw1=ImageDraw.Draw(low_pass)
    draw1.ellipse(bbox, fill=1)
    low_pass_np=np.array(low_pass)
    low_pass_np = low_pass_np.T
    #end of defining filter

    #multiply both the images
    filtered=np.multiply(fft1,low_pass_np)

    #inverse fft
    ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(filtered)))
    ifft2 = np.maximum(0, np.minimum(ifft2, 255))
    data = Image.fromarray(ifft2)  
    data = data.convert("L") 
    output = []
    output.append(img)
    output.append(data)

    return output

def high_pass_filter(input_image):

    img = input_image.resize((400,400), Image.ANTIALIAS)
    #converting image to array
    image_array = np.array(img)

    #sending image to low pass filter
    lowpass_image = low_pass_filter(input_image)
    #converting image to array
    lowpass_image_array = np.array(lowpass_image[1])
    print(lowpass_image_array.shape)
   


    #subtracting lowpass image from original to obtain highpass image
    high_pass_array = image_array - lowpass_image_array
    print(high_pass_array.shape)


    #array to image
    high_pass_image = Image.fromarray(high_pass_array)  
    high_pass_image = high_pass_image.convert("L")
    output = []
    output.append(img)
    output.append(high_pass_image)

    return output