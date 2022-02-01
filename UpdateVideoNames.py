import pytesseract
import cv2
import os
from HelperFunctions import *
from shutil import *



def updateVideoNames(nameOfVideoFolder):
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
                
                text = ocrMain(crop_img)
                newVidName = getVideoFormat(text)

                copyfile(f,'output//%s.mp4' % newVidName)
        count = count + 1
        if count == 3:
            print('Process is going smoothly so far. ')
        if count%100 == 0:
            print('You have successfully updated %d videos' % count)


    print('All %d videos have been updated.\nHooray!!!' % count )
    return

def clear():
    """
    Deletes all files in the images_placed_here and output folders.  Will first ask for confirmation before executing.

    param: none
    returns: none
    """
    response = input("You have enabled the clear() function. Continuing will erase all progress up to this point. Would you like to continue? Type 'y' to continue,'n' to quit: ")
    if response == 'y':
        output_directory= os.path.abspath('output')
        for filename in os.listdir(output_directory):
            f = os.path.join(output_directory, filename)
            if os.path.isfile(f):
                if filename == '.DS_Store':
                    continue
                os.remove(f)

        images_directory = os.path.abspath('images_placed_here')
        for filename in os.listdir(images_directory):
            f = os.path.join(images_directory, filename)
            if os.path.isfile(f):
                if filename == '.DS_Store':
                    continue
                os.remove(f)
    return


    

    


