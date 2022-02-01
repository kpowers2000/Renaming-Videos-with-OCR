from UpdateVideoNames import *
from HelperFunctions import *

if __name__=="__main__":
    print("***** STARTING *****")
    #clear() ### 'clear()' will delete all video copies previously created by this program.  First asks for confirmation. ###
    nameOfVideoFolder = "place_videos_here"
    updateVideoNames(nameOfVideoFolder)