# Tesseract Project: Reading Text and Renaming Videos
This project uses an optical character recognition algorithm to rename videos in the **place_videos_here** folder based on the date and time the video occurs.  The new name follows the format "YYYY-MM-DD_hh_mm_ss.mp4" and is in the output folder after execution.

## Motivation
This project was created in partnership with Doris Duke Professor of Conservation Stuart Pimm and Duke Associate in Research Ryan Huang for Saving Nature: an NGO devoted to saving vanishing ecosystems, preventing biodiversity loss, and rescuing communities from the aftermath of environmental destruction.  Currently, Saving Nature is developing AI techniques to identify animals "captured" by camera traps in wildlife corridors worldwide.  This method provides a low-impact and sustainable way to acquire and analyze wildlife data, an essential part of creating a sustainable future.


## Modules 
#### Main.py
Run this module to execute the program.  A clear() function is included (initially commented out).  Clear deletes all files in output and images_placed_here folders. It first asks for confirmation before erasure.  
#### UpdateVideoNames
Contains updateVideoNames(nameOfVideoFolder) and clear().  

#### HelperFunctions
Contains getVideoFormat(text). cropImage(image), and ocrMain(image).

