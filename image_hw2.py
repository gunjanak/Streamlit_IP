
import numpy as np
import streamlit as st
import cv2
from PIL import Image
from urllib.request import urlopen

import Morphology
import Logic
import Frequency
import Derivative
import Spatial
import Basic


Output_image = 350


def main():
    @st.cache
    def load_image(img):
        image = Image.open(img)
        image = image.convert('L')
        newsize = (400,400)
        image = image.resize(newsize)
        return image

    image = load_image('cover.png')
    #image = Image.fromarray(image)
    st.title('Filter Selector')
    st.sidebar.title('Sidebar')

    menu = ['None','Basic','Spatial','Derivative','Frequency','Morphology','Logical']

    op = st.sidebar.selectbox('Option',menu)

    if op == 'Basic':
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])

        if img is not None:
            image = Image.open(img)
            image = image.convert('L')
            #st.sidebar.text('Original Image')
            #st.sidebar.image(image,width=200)
        
        filters = st.sidebar.radio('Basic',['None','Bit Plane','Log Transform',
        'Power Transform','Threshold','Negative','Histogram Eq'])
        if filters == 'Bit Plane':
            img_convert = image.convert('L')
            gray_image = img_convert
            slide = st.sidebar.slider('Bit',0,8,1)
            output_image = Basic.Bit_Plane(gray_image,slide)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        
        elif filters == 'Log Transform':
            img_convert = image.convert('L')
            gray_image = img_convert

            output_image = Basic.Log_transform(gray_image)

            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Power Transform':
            img_convert = image.convert('L')
            gray_image = img_convert
            gamma = st.sidebar.slider('Gamma',0.0,2.0,0.1)
            st.write(str(gamma))
            output_image = Basic.Power_transform(gray_image,gamma)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Threshold':
            threshold = st.sidebar.slider('Threshold',10,200,10)
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Basic.Threshold(gray_image,threshold)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        
        elif filters == 'Negative':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Basic.Negative(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        
        elif filters == 'Histogram Eq':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Basic.Histogram_equalization(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)








    elif op == 'Spatial':
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])

        if img is not None:
            image = Image.open(img)
            image = image.convert('L')
            #st.sidebar.text('Original Image')
            #st.sidebar.image(image,width=200)
        
        filters = st.sidebar.radio('Spatial',['None','Smooth','Sharp','Min','Max','Median','High Boost'])
        if filters == 'Smooth':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.smooth_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Sharp':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.sharp_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Min':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.min_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Max':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.max_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Median':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.median_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'High Boost':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Spatial.high_boost(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)



    elif op == 'Derivative':
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])

        if img is not None:
            image = Image.open(img)
            image = image.convert('L')
            #st.sidebar.text('Original Image')
            #st.sidebar.image(image,width=200)
        
        filters = st.sidebar.radio('Derivative',['None','Prewitt_horizontal','Prewitt_vertical',
        'Sobel_horizontal','Sobel_vertical','Sobel 45','Sobel 225',
        'Laplacian'])

        if filters == 'Prewitt_horizontal':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Prewitt_Operator_horizontal(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Prewitt_vertical':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Prewitt_Operator_vertical(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Sobel_horizontal':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Sobel_Operator_horizontal(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Sobel_vertical':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Sobel_Operator_vertical(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Sobel 45':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Sobel_Operator_45(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)

        elif filters == 'Sobel 225':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Sobel_Operator_225(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        elif filters == 'Laplacian':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Derivative.Laplacian_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)




        


    elif op == 'Frequency':
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])

        if img is not None:
            image = Image.open(img)
            image = image.convert('L')
            #st.sidebar.text('Original Image')
            #st.sidebar.image(image,width=200)
        
        filters = st.sidebar.radio('Frequency',['None','Frequency','Low Pass','High Pass'])

        if filters == 'Frequency':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Frequency.frequency_image(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header("Frequency")
            col2.image(output_image[1],width=Output_image)
        
        elif filters == 'Low Pass':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Frequency.low_pass_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        
        elif filters == 'High Pass':
            img_convert = image.convert('L')
            gray_image = img_convert
            output_image = Frequency.high_pass_filter(gray_image)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(output_image[0],width=Output_image)
            col2.header(filters)
            col2.image(output_image[1],width=Output_image)
        

        else:
            img_convert = image.convert('L')
            st.image(img_convert,width=Output_image)
        


    elif op == 'Morphology':
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])

        if img is not None:
            image = Image.open(img)
            image = image.convert('L')
            #st.sidebar.text('Original Image')
            #st.sidebar.image(image,width=200)
            
            

            
        filters = st.sidebar.radio('Morphology',['None','Erosion','Dilation','Opening','Closing','Morphological_gradient'])

        if filters == 'Erosion':
            
            Kernel_value = st.sidebar.slider('Kernel',0,50,1)
            img_convert = image.convert('L')
            gray_image = img_convert
            images = Morphology.Erosion(gray_image,Kernel_value)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(images[0],width=Output_image)
            col2.header(filters)
            col2.image(images[1],width=Output_image)
          
        elif filters == 'Dilation':
            Kernel_value = st.sidebar.slider('Kernel',0,50,1)
            img_convert = image.convert('L')
            gray_image = img_convert
            images = Morphology.Dilation(gray_image,Kernel_value)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(images[0],width=Output_image)
            col2.header(filters)
            col2.image(images[1],width=Output_image)
        
        elif filters == 'Opening':
            Kernel_value = st.sidebar.slider('Kernel',0,50,1)
            img_convert = image.convert('L')
            gray_image = img_convert
            images = Morphology.Open(gray_image,Kernel_value)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(images[0],width=Output_image)
            col2.header(filters)
            col2.image(images[1],width=Output_image)

       
        
        elif filters == 'Closing':
            #Dilation followed by Erosion
            Kernel_value = st.sidebar.slider('Kernel',0,50,1)
            img_convert = image.convert('L')
            gray_image = img_convert
            images = Morphology.Close(gray_image,Kernel_value)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(images[0],width=Output_image)
            col2.header(filters)
            col2.image(images[1],width=Output_image)

        elif filters == 'Morphological_gradient':
            #It is the difference between dilation and erosion of an image.
            Kernel_value = st.sidebar.slider('Kernel',0,50,1)
            img_convert = image.convert('L')
            gray_image = img_convert
            images = Morphology.MG(gray_image,Kernel_value)
            col1, col2 = st.columns(2)
            col1.header("Original")
            col1.image(images[0],width=Output_image)
            col2.header(filters)
            col2.image(images[1],width=Output_image)



        else:
            img_convert = image.convert('L')
            st.image(img_convert,width=Output_image)

    elif op=='Logical':
        img1  = st.file_uploader('Upload first image',type=['jpg','png','jpeg'])
        img2 = st.file_uploader('Upload second image',type=['jpg','png','jpeg'])


        #if (img1 is not None) and (img2 is not None) :
           
            
            
        filters = st.sidebar.radio('Logic',['None','AND','OR','XOR'])
        if (img1 is not None) and (img2 is not None):
            image1 = Image.open(img1)
            image1 = image1.convert('L')

            image2 = Image.open(img2)
            image2 = image2.convert('L')

            if filters == 'AND':
                img_convert1 = image1.convert('L')
                gray_image1 = img_convert1
                img_convert2 = image2.convert('L')
                gray_image2 = img_convert2
                images = Logic.AND(gray_image1,gray_image2)
                col1, col2, col3 = st.columns(3)
                col1.header("Original 1")
                col1.image(images[0],width=200)
                col2.header("Original 2")
                col2.image(images[1],width=200)
                col3.header(filters)
                col3.image(images[2],width=200)

            elif filters == 'OR':
                img_convert1 = image1.convert('L')
                gray_image1 = img_convert1
                img_convert2 = image2.convert('L')
                gray_image2 = img_convert2
                images = Logic.OR(gray_image1,gray_image2)
                col1, col2, col3 = st.columns(3)
                col1.header("Original 1")
                col1.image(images[0],width=200)
                col2.header("Original 2")
                col2.image(images[1],width=200)
                col3.header(filters)
                col3.image(images[2],width=200)
            
            elif filters == 'XOR':
                img_convert1 = image1.convert('L')
                gray_image1 = img_convert1
                img_convert2 = image2.convert('L')
                gray_image2 = img_convert2
                images = Logic.XOR(gray_image1,gray_image2)
                col1, col2, col3 = st.columns(3)
                col1.header("Original 1")
                col1.image(images[0],width=200)
                col2.header("Original 2")
                col2.image(images[1],width=200)
                col3.header(filters)
                col3.image(images[2],width=200)



        else:
            img_convert = image.convert('L')
            st.image(img_convert,width=Output_image)
         






    else:
        img  = st.file_uploader('Upload an image',type=['jpg','png','jpeg'])







if __name__ == '__main__':
    main()