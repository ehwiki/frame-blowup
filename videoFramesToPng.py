"""
videoFramesToPng.py

Contains functions to read in a video file from the command line and turn its frames
	into png files. The files are stored in a subdirectory of this program's directory
"""

import cv2
import os
from sys import argv
from datetime import datetime

#retrieves the filename from command line argments. Assumes two arguments at the moment
def getFilename(args):
	if len(argv) is 2:
		script, filename = args
		return filename
	else:
		print "Need 2 arguments. You have %d" % len(args)
		return False

#Checks if the filename gotten from the arguments is actually a video file by checking
#	the extension
def isValidVideoFile(fname):
	if ".mp4" in f or ".avi" in f or ".mkv" in f or ".mov" in f:
		return True
	else:
		return False

#makes the directory that the .png files get stored in
def makeFolder():
	#gets the date and time to have unique directory name
	now = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
	#checkForExistence because it could already exist?
	#has the name of the program and the time for directory name
	path = 'videoFramesToPng_' + now
	os.makedirs(path)
	#returns the filepath so other methods know where to access
	return path

#converts the frames of the given video file into .png files
def convertFramesToPng(f):
	vidcap = cv2.VideoCapture(f)
	count = 1

	#retval is used for looping
	#frame is what gets written
	if vidcap.isOpened():
		retval, frame = vidcap.read()
	else:
		retval = False

	if retval:
		#fpath: the path where files get placed
		fpath = makeFolder()

		#while the video has frames
		while retval:
			retval, frame = vidcap.read()
			if frame is not None:
				cv2.imwrite(fpath + '/' + str(count) + '.png', frame)
			count = count + 1
			#stop making png files if escape is pressed
			if cv2.waitKey(1) == 27:
				break
		vidcap.release()
		print "Your images are in %s" % fpath
	else:
		print "%s not a valid video file." % f

filename = getFilename(argv)
convertFramesToPng(filename)
