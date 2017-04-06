# -*- coding: utf-8 -*-

import os
import face_recognition as fr
import shutil

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

def check_for_folder():
    # TODO: Create logic that allows user to somehow decide where they would like there
    # photos with faces to be stored.
    work_dir = os.getcwd()
    # Check if a 'Faces' folder already exists. This only walks folders not files.
    dir_list = os.walk(work_dir).next()[1]
    count = 0
    for folder in dir_list:
        # Logic here doesn't make sense, creates a whole new folder each time it doesn't find Faces
        if folder != 'Faces':
            continue
        else:
            count += 1
            return True
    if count == 0:
        os.mkdir('Faces')

def move_to_folder(face_list):
    """Moves photos with Faces to Face Folder"""
    check_for_folder()
    work_dir = os.getcwd()
    face_dir = work_dir + '/' + 'Faces'
    for photo in face_list:
        path = work_dir + '/' + photo
        shutil.copy(path, face_dir)

if __name__ == "__main__":
    photo_list = photo_finder()
    face_list = face_checker(photo_list)
    move_to_folder(face_list)
