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

def check_for_folder():
    """Checks to see if target download folder is created. If not creates the folder"""
    work_dir = os.getcwd()
    # The following only walks folders. Ignores files
    dir_list = os.walk(work_dir).next()[1]
    count = 0
    for folder in dir_list:
        if folder != 'Faces':
            continue
        else:
            count += 1
    if count == 0:
        os.mkdir('Faces')

def move_to_folder(face_list):
    """Moves photos with Faces to Faces Folder"""
    check_for_folder()
    work_dir = os.getcwd()
    face_dir = 'Faces'
    face_dir_path = work_dir + '/' + face_dir
    for photo in face_list:
        path = work_dir + '/' + photo
        shutil.copy(path, face_dir)

def navigator(folder):
    """For a given folder locates all"""
    pass
