# -*- coding: utf-8 -*-

import face_recognition as fr
from utils import check_for_folder, move_to_folder, photo_finder
from tqdm import tqdm

def face_checker(photo_list):
    """Finds pictures with faces in list of photos"""
    face_list = []
    for photo in tqdm(photo_list): # insert loading bar with tqdm here
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

def get_main_face():
    # TODO: get main face to be compared but not from webcam
    pass

def face_match(unknown_image, known_image):
    """Compares main face to faces found in photo. Can be used repeatedly against other faces.
    This module will find matching face despite other faces in photo. So only needs to be used once per photo.
    """
    known_face = find_face(known_image)
    unknown_face = find_face(unknown_image)
    # Need to have at least two faces to compare against for the compare_faces module
    # to get this to work with only one, treat 'known_face' as a list
    results = fr.compare_faces([known_face], unknown_face)
    # Just return results for now. TODO: be more detailed about who is in the picture
    return results

def find_all_faces():
    """Finds photos with faces in current working directory.
    Places said photos in a folder called Faces."""
    photo_list = photo_finder()
    face_list = face_checker(photo_list)
    move_to_folder(face_list)
