from utils import check_for_folder, photo_finder, move_to_folder
from face_finder import face_checker, find_face, face_match, find_all_faces
from tqdm import tqdm
import face_recognition as fr

def get_args_parser():
    import argparse
    from argparse import  RawTextHelpFormatter
    desc = 'Finds photos with faces in a folder.'
    desc += '\nCan also find and arrange all photos in which a certain person is featured.'
    desc += '\n These photos will then be placed in a folder.'
    p = argparse.ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
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
        try:
            my_face = find_face(args.filename)
        except IndexError:
            print "There is no face in the picture you chose."
            parser.exit(1)
        photo_list = photo_finder()
        face_list = face_checker(photo_list)
        for photo in face_list:
            if photo == args.filename:
                face_list.remove(photo)
        my_pics = []
        for face in tqdm(face_list):
            face_encoding = find_face(face)
            # Included a tolerance of 0.4 to see if script can differentiate between my brother and I.(not twins)
            results = fr.compare_faces([my_face], face_encoding, 0.4)
            if results[0]:
                my_pics.append(face)
            else:
                continue
        if my_pics:
            move_to_folder(my_pics)
        else:
            print " There were no photos of you found!"
    elif args.command == "all":
        find_all_faces()
        print "Worked!"
    else:
        parser.print_help()
        print "Did not work!"
        parser.exit(1)

if __name__ == "__main__":
    main()
