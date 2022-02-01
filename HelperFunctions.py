import pytesseract
import cv2
import os

#/Users/keenan/CameraTrapPython/images_placed_here/imageOf03250275 Mac_Nem.mp4.jpg


def ocrMain(image):
    """
    ocrMain reads the text from the given image.

    param image: a cropped image from the video containing the date, time, and other data from the video.
    return: string; the date, time, and other data found in image
    """
    text = pytesseract.image_to_string(image, config='--psm 7')
    text = text.strip()
    return text

def cropImage(image):
    
    """
    cropImage crops all but the part of the image containing temperature, date, and time.
        This image is then read using PyTesseract to process the date and time of the image.

    param image- first image of the video filename.
    return: image with all but the bottom part containing the temperature, date, and time of the video.
    """
    start_x = 690
    end_x = 720
    start_y = 400
    end_y = 1280
    crop_img = image[start_x:end_x, start_y:end_y]
    return crop_img

def getVideoFormat(text):
    """
    getVideoFormat takes the text from the bottom of the videos 
        and puts it the following format: "YYYY-MM-DD_hh:mm:ss_XXF.mp4".  
        For example, example video 02090078 Mac_Nem.mp4 is renamed to "2019-02-09_08:20:01_71F.mp4"

    param text: string; extracted from the bottom of the video using PyTesseract.
    return: string; the title the video will be renamed to.
    """
    temp_date_time = text.split()
    tempF = temp_date_time[0][0]+ temp_date_time[0][1] + 'F'
    tempC = temp_date_time[1][0]+ temp_date_time[1][1] + 'C'
    date = temp_date_time[2]
    time = temp_date_time[3]
    
    dateLst = date.split('-')
    dateLst = [dateLst[2],dateLst[0],dateLst[1]]
    newDate = '-'.join(dateLst)
    
    newVidName= newDate + '_' + time + '_' + tempF

    return newVidName


