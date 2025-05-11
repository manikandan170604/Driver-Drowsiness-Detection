from flask import Flask, render_template, Response,flash,redirect
from flask import *
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import pygame


# camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

app = Flask(__name__)

pygame.init()
song = pygame.mixer.Sound('alarm.wav')

#function to calculate the return the Eye Aspect Ratio (EAR)
def e_a_r(eye):
	L_vertical = distance.euclidean(eye[1], eye[5])
	R_vertical = distance.euclidean(eye[2], eye[4])
	horizontal = distance.euclidean(eye[0], eye[3])
	ratio = (L_vertical + R_vertical) / (2.0 * horizontal)
	return ratio

#the threshold ratio to compare with the calculated EAR
thres = 0.25

#to compare the frame count value to alert
frame_check = 20

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("facialLandmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
print("Camera Loading")

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/display')
def display():
    return render_template('index.html')

@app.route('/video_processing')
def gen_frames():
    while True:
        ret, frame=cap.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)
            eyeL = shape[lStart:lEnd]
            eyeR = shape[rStart:rEnd]
            EAR_l = e_a_r(eyeL)
            EAR_r = e_a_r(eyeR)
            #average of EARs of left and right eyes
            netEAR = (EAR_r + EAR_l) / 2.0
            lHull = cv2.convexHull(eyeL)
            rHull = cv2.convexHull(eyeR)
            cv2.drawContours(frame, [lHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rHull], -1, (0, 255, 0), 1)
            cv2.putText(frame, "------- SAFE :) -------", (10, 325),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            if netEAR < thres:
                flag += 1
                
                if flag >= frame_check:
                    cv2.drawContours(frame, [lHull], -1, (0, 0, 255), 1)
                    cv2.drawContours(frame, [rHull], -1, (0, 0, 255), 1)
                    song.play()				
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10,325),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                   
            else:
                song.stop()			
                flag = 0
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        #to quit the application, assigning 'Q'
        if key == ord("q"):
            print("Camera off")
            print("Application closed")
            break
    
        if not ret:
            break
        else:
            ret,buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cv2.destroyAllWindows()


    

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop')
def stop():
    return render_template('stop.html')

@app.route('/close')
def closing():
    cap.release()
    return render_template('final_page.html')

if __name__ == '__main__':
    app.run(debug=True)