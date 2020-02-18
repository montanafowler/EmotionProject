import cv2
import numpy as np
import os.path
import argparse

from cv2 import WINDOW_NORMAL
from face_detection import find_faces
from flask import Flask, request
from markupsafe import escape
from flask import render_template
app = Flask(__name__)
import base64
import csv


ESC = 27
INDEX_DICT = {'happy':0, 'sad':0, 'angry':0, 'afraid':0, 'neutral':0, 'surprised':0, 'disgust':0}

def start_webcam(model_emotion, model_gender, window_size, window_name='live', update_time=50):
    cv2.namedWindow(window_name, WINDOW_NORMAL)
    if window_size:
        width, height = window_size
        cv2.resizeWindow(window_name, width, height)

    video_feed = cv2.VideoCapture(0)
    video_feed.set(3, width)
    video_feed.set(4, height)
    read_value, webcam_image = video_feed.read()

    delay = 0
    init = True
    while read_value:
        read_value, webcam_image = video_feed.read()
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):
          if init or delay == 0:
            init = False
            emotion_prediction = model_emotion.predict(normalized_face)
            gender_prediction = model_gender.predict(normalized_face)
          if (gender_prediction[0] == 0):
              cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (0,0,255), 2)
          else:
              cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (255,0,0), 2)
          cv2.putText(webcam_image, emotions[emotion_prediction[0]], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
        delay += 1
        delay %= 20
        cv2.imshow(window_name, webcam_image)
        key = cv2.waitKey(update_time)
        if key == ESC:
            break

    cv2.destroyWindow(window_name)

def analyze_picture(file_name, model_emotion, model_gender, path, window_size, window_name='static'):
    emotions = ["afraid", "angry", "disgusted", "happy", "neutral", "sad", "surprised"]
    #cv2.namedWindow(window_name, WINDOW_NORMAL)
    #cv2.namedWindow(window_name, WINDOW_NORMAL)
    #if window_size:
        #width, height = window_size
        #cv2.resizeWindow(window_name, width, height)
    emotionsDetected = []
    image = cv2.imread(path, 1)
    for normalized_face, (x, y, w, h) in find_faces(image):
        emotion_prediction = model_emotion.predict(normalized_face)
        gender_prediction = model_gender.predict(normalized_face)
        if (gender_prediction[0] == 0):
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
        else:
            cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(image, emotions[emotion_prediction[0]], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        print(emotions[emotion_prediction[0]])
        emotionsDetected.append(emotions[emotion_prediction[0]])
    
    savedImgPath = "../data/sample/output/"
    savedOutputImgPath = savedImgPath + "output.jpg"
    savedImgPath += file_name
    cv2.imwrite(savedImgPath, image)
    print("wrote image to " + savedImgPath)
    cv2.imwrite(savedOutputImgPath, image)
    print("wrote image to " + savedOutputImgPath)
    imagesToReturn = [savedOutputImgPath]
    
    for e in emotionsDetected:
        csvFilename = e + "Art.csv"
        with open(csvFilename, newline='', encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            #print("INDEX_DICT[" + e + "] = " + INDEX_DICT[e])
            imgURL = list(reader)[INDEX_DICT[e]]["ImageURL"]
            print(imgURL)
            INDEX_DICT[e] += 1 #increment the index of the art
            imagesToReturn.append(imgURL)

    #cv2.imshow(window_name, image)
    
    
    #key = cv2.waitKey(0)
    #if key == ESC:
        #cv2.destroyWindow(window_name)
    return imagesToReturn

#@app.route('/facifier/')
def initializeHomePage():
    return render_template("index.html")


#@app.route('/facifier/image/<imageName>', methods='POST')
#if __name__ == '__main__':
#@app.route('/facifier/image/<imageName>')
@app.route('/startFacifier', methods=['GET','POST'])
def startFacifier():
    # if we are initializing the page, just return the html
    if request.method == 'GET':
        return render_template("index.html")

    # if we have received an image name then save it
    imageName = request.form['imageNameInput']
    print("imageName: " + str(imageName))
    
    # the possible emotions we could detect
    emotions = ["afraid", "angry", "disgusted", "happy", "neutral", "sad", "surprised"]    
    
    # Load model
    fisher_face_emotion = cv2.face.FisherFaceRecognizer_create()
    fisher_face_emotion.read('models/emotion_classifier_model.xml')
    fisher_face_gender = cv2.face.FisherFaceRecognizer_create()
    fisher_face_gender.read('models/gender_classifier_model.xml')

    # Use model to predict
    #choice = input("Use webcam?(y/n) ")
    choice = 'n'
    if (choice == 'y'):
        window_name = "Facifier Webcam (press ESC to exit)"
        start_webcam(fisher_face_emotion, fisher_face_gender, window_size=(1280, 720), window_name=window_name, update_time=15)
    elif (choice == 'n'):
        run_loop = True
        window_name = "Facifier Static (press ESC to exit)"
        print("Default path is set to data/sample/")
        #print("Type q or quit to end program")
        while run_loop:
            run_loop = False
            path = "../data/sample/"
            file_name = imageName
            if file_name == "q" or file_name == "quit":
                run_loop = False
            else:
                path += file_name
                print("path to image: " + path)
                if os.path.isfile(path):
                    print("calling analyze picture")
                    imagesToReturn = analyze_picture(file_name, fisher_face_emotion, fisher_face_gender, path, window_size=(1280, 720), window_name=window_name)
                    #data = emotionsDetectedImg
                    #print("emotionsDetectedImg " + str(emotionsDetectedImg))
                    
                    with open(imagesToReturn[0], "rb") as image_file:
                        img = image_file.read()
                        data = base64.b64encode(img)
                    artImages = imagesToReturn[1:] #remove the output path
                    print("imagesToReturn " + str(imagesToReturn))
                else:
                    print("File not found!")
                    return render_template("index.html")
    else:
        print("Invalid input, exiting program.")
    return render_template("index.html", data=data.decode('utf8'), artImages=artImages)

