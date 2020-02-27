from imutils.video import VideoStream
import cv2

# grab the reference to the webcam
vs = VideoStream(src=0).start()

# keep looping
while True:
	# grab the current frame
	frame = vs.read()
  
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' or ESC key is pressed, stop the loop
	if key == ord("q") or key == 27:
		break
 
# close all windows
cv2.destroyAllWindows()
