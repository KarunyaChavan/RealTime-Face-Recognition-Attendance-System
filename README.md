
# 🎯 Face Recognition Attendance System  

A real-time **Face Recognition-based Attendance System** that utilizes **OpenCV, face_recognition, and Firebase** to automate attendance marking with live webcam feed and dynamic UI overlays.  

## 🚀 Features  

- **Real-time Face Recognition** 📷 using OpenCV and face_recognition for accurate identification.  
- **Firebase Integration** 🔥 for fetching student data, attendance tracking, and image retrieval.  
- **Excel-based Attendance Logging** 📊 using OpenPyXL for structured record-keeping.  
- **Dynamic UI Overlays** 🎨 with cvzone for an interactive attendance display.  
- **Optimized Face Matching** ⚡ using Euclidean distance-based face encoding and comparison.  

## 🛠️ Tech Stack  

- **Python** 🐍  
- **OpenCV** for image processing  
- **face_recognition** for face matching  
- **Firebase Realtime Database & Storage**  
- **OpenPyXL** for Excel-based record management  
- **cvzone** for enhanced UI overlays  
- **NumPy** for numerical operations  

## 📌 Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/face-attendance.git
   cd face-attendance
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Add your **Firebase service account key** (`serviceAccountKey.json`) to the project root.  
4. Ensure **student images** are uploaded in Firebase Storage under the `Images/` directory.  
5. Run the system:  
   ```bash
   python main.py
   ```
 
