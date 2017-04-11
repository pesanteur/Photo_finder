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

def find_face(image):
    # TODO: Create logic for image upload. Where will the main image be placed or sourced from?
    image = fr.load_image_file(image)
    image_encoding = fr.face_encodings(image)[0]
    return image_encoding

def face_match(unknown_image, known_image):
    """Compares main face to faces found in list of photos.
    This module needs further testing."""
    known_face = find_face(known_image)
    unknown_face = find_face(unknown_image)
    # Need to have at least two faces to compare against for the compare_faces module
    # to get this to work with only one, treat 'known_face' as a list
    results = fr.compare_faces([known_face], unknown_face)
    # Just return results for now. TODO: be more detailed about who is in the picture
    return results

if __name__ == "__main__":
    photo_list = photo_finder()
    face_list = face_checker(photo_list)
    move_to_folder(face_list)
