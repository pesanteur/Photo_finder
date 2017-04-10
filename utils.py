# -*- coding: utf-8 -*-

import os
import shutil

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
    face_dir = work_dir + '/' + 'Faces'
    for photo in face_list:
        path = work_dir + '/' + photo
        shutil.copy(path, face_dir)
