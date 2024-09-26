import cv2
import os
import face_recognition
import pickle
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionrealtime-e783a-default-rtdb.firebaseio.com/",
    'storageBucket':"facerecognitionrealtime-e783a.appspot.com"
})

'''Importing Images of Students'''
#Importing Modes images into a list 
folderPath = "Images"
PathList = os.listdir(folderPath)
print(PathList)
#List of images of mode
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    
    #Sending images to database
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
    #print("ID : ",os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    #We will loop through each image and encode it
    for img in imagesList:
        #Step 1 : Coverting Color Space (BGR -> RGB)==>OpenCV uses BGR and face_recognition uses RGB
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #Step 2 : Find Encodings
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
print("Encoding Completed")
encodeListKnownWithIds = [encodeListKnown,studentIds]
#Step 3 : Storing the encodings with their respective ids using pickle
file = open("EncodeFile.p","wb")
#Dumping the lists in this file
pickle.dump(encodeListKnownWithIds,file)
file.close
print("File Created")
        