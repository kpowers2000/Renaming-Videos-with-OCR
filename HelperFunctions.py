import pytesseract
import cv2
import os
import csv

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
        and puts it the following format: "YYYY-MM-DD_hh:mm:ss.mp4".  
        For example, example video 02090078 Mac_Nem.mp4 is renamed to "2019-02-09_08:20:01.mp4"

    param text: string; extracted from the bottom of the video using PyTesseract.
    return: string; the title the video will be renamed to.
    """
    temp_date_time = text.split()
    tempF = temp_date_time[0][0]+ temp_date_time[0][1]
    tempF = int(tempF)
    tempC = temp_date_time[1][0]+ temp_date_time[1][1] + 'C'
    date = temp_date_time[2]
    time = temp_date_time[3]
    
    dateLst = date.split('-')
    dateLst = [dateLst[2],dateLst[0],dateLst[1]]
    newDate = '-'.join(dateLst)
    
    newVidName= newDate + '_' + time
    return newVidName


def getTemp(image):
    """
    extracts temperature from generated text
    """
    text = ocrMain(image)
    temp_date_time = text.split()
    tempF = temp_date_time[0][0]+ temp_date_time[0][1]
    tempF = int(tempF)
    
    return tempF


def createTemperatureCSV(nameOfVideoFolder):
    """
    updateVideoNames creates copies of all videos in videoFolder, renamed in the format
        "YYYY-MM-DD-hh-mm-ss.mp4".  Videos with updated names can be found in the output folder

    param nameOfVideoFolder: name of input folder containing all videos to be updated.
    returns: none 
    Copies of all videos in videoFolder, renamed in the format
             "YYYY-MM-DD-hh-mm-ss.mp4"

    """
    directory = os.path.abspath(nameOfVideoFolder)
    # iterates through all videos in place_video_here folder
    count = 0
    rows = []
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            if filename == '.DS_Store':
                continue
            vidcap = cv2.VideoCapture(f)
            success,image = vidcap.read() 
            if success: 
                # save frame as JPEG file
                cv2.imwrite( "images_placed_here//imageOf%s.jpg" % filename, image)     
                crop_img = cropImage(image)
                
                temp = getTemp(crop_img)
                rows.append([filename,temp])
        count = count + 1
        if count == 3:
            print('Process is going smoothly so far. ')
        if count%100 == 0:
            print('You have successfully extracted temperature from %d videos' % count)
        # using csv.writer method from CSV package
    cols = ["Filename", "Temperature"]
    with open('temp.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(cols)
        write.writerows(rows)

    print('All %d temperatures have been added to \'temp.csv\'.\nHooray!!!' % count )
    return
