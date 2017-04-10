# -*- coding: utf-8 -*-

import face_recognition as fr
from utils import check_for_folder
from utils import move_to_folder
import os

def photo_finder():
    """Finds png, jpeg files in folder in current working directory."""
    photo_list = []
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            photo_list.append(filename)

    return photo_list

def face_checker(photo_list):
    """Finds pictures with faces in list of photos"""
    face_list = []
    for photo in photo_list:
        image = fr.load_image_file(photo)
        face_locations = fr.face_locations(image)
        if face_locations:
            face_list.append(photo)

    return face_list

def face_count(photo):
    """Only works when photo is in current directory"""
    image = fr.load_image_file(photo)
    face_locations = fr.face_locations(image)
    face_count = len(face_locations)
    return face_count

if __name__ == "__main__":
    photo_list = photo_finder()
    face_list = face_checker(photo_list)
    move_to_folder(face_list)
