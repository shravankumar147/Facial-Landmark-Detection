from parallel_sync import wget
import os

target_path = os.getcwd()

url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"

wget.download(target_path, urls=url)