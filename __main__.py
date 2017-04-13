from utils import check_for_folder
from utils import photo_finder
from utils import move_to_folder
from face_finder import face_checker
from face_finder import find_face
from face_finder import face_match


def get_args_parser():
    import argparse
    from arggparse import  RawTextHelpFormatter
    p = argparse.ArgumentParser(description, formatter_class=RawTextHelpFormaatter)
    subparsers = p.add_subparsers(dest='command')
    all_parser = subparsers.add_parser('all')
    #TODO: Add more to parser
    me_parser = subparsers.add_parser('me')
    me_parser.add_argument('--filename','-f', required=True,
                            help='Filename of main photo')
    return p

def main():
    parser = get_args_parser()
    args = parser.parse_args()
    if args.command == "me":
        my_face = find_face(args.filename)
        photo_list = photo_finder()
        face_list = face_checker(photo_list)
        for face in face_list:
            results = face_match(face, my_face)
            if results:
                move_to_folder(face)
            else:
                continue
    elif args.command == "all":
        find_all_faces()
    else:
        parser.print_help()
        parser.exit(1)
