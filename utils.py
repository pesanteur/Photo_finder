# -*- coding: utf-8 -*-

import os
import shutil

def photo_finder():
    """Finds png, jpeg files in folder in current working directory."""
    photo_list = []
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.JPG'):
            photo_list.append(filename)

    return photo_list

def check_for_folder(face_dir='Faces'):
    """Checks to see if target download folder is created. If not creates the folder"""
    work_dir = os.getcwd()
    dir_list = os.walk(work_dir).next()[1] # The following only walks folders. Ignores files NOTE: Only works in python2, os.walk is generator in python3
    if 'Faces' not in dir_list:
        os.mkdir(face_dir)

def move_to_folder(face_list, face_dir='Faces'):
    """Moves photos with Faces to Faces Folder"""
    # TODO: This function needs to be more generalized so that it can be used in other loops
    check_for_folder()
    work_dir = os.getcwd()
    for photo in face_list:
        path = work_dir + '/' + photo
        shutil.copy(path, face_dir)
