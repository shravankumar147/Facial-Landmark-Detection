# Facial Landmark Detection 

# Overview
In this demo we will find the facial landmarks, such as eyes, nose, mouth, ears, jaw-line using the popular [dlib](http://dlib.net/) library

# Dependencies
```pip install -r requirements.txt```

You also need shape detector, you can download it by 
```
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
```
# Usage
 ```
 python facelandmarkdetect.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/face1.jpg
```

Results: ![Alt](results/result_m.png "Title")





Credits: My Guru: Adrian Rosebrock 
