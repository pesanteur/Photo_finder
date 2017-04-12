import face_recognition as fr
from utils import check_for_folder
from face_finder import face_checker
from utils import photo_finder
from utils import move_to_folder

if __name__ == "__main__":
    """Finds photos with faces in current working directory and
    Places said photos in folder called Faces."""
    photo_list = photo_finder()
    face_list = face_checker(photo_list)
    move_to_folder(face_list)
