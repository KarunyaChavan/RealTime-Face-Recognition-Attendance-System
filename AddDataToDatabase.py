import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionrealtime-e783a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

#Setting Data Values
data = {
    "21005":
        {
            "Name":"Shruti Bachal",
            "Department":"Computer",
            "Class":"SE",
            "Div":"A",
            "Total Attendance" :0,
            "last_attendance_time":"2024-4-6 13:54:34",
        },
    "21012":
        {
            "Name":"Karunya Chavan",
            "Department":"Computer",
            "Class":"SE",
            "Div":"A",
            "Total Attendance":0,
            "last_attendance_time":"2024-4-6 13:44:34",
        },
    "21013":
        {
            "Name":"Hemant Choudhary",
            "Department":"Computer",
            "Class":"SE",
            "Div":"B",
            "Total Attendance" : 0,
            "last_attendance_time":"2024-4-6 14:54:34",
        },
    "21020":
        {
            "Name":"Sankalp Gaikwad",
            "Department":"Computer",
            "Class":"SE",
            "Div":"A",
            "Total Attendance" : 0,
            "last_attendance_time":"2024-4-6 13:54:34",
        }
}

for key,value in data.items():
    ref.child(key).set(value)
