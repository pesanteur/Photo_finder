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
        #import pdb; pdb.set_trace()
        photo_list = photo_finder()
        face_list = face_checker(photo_list)
        for photo in face_list:
           # This won't work as my_face is not a filename.
           # TODO: change to if photo == args.filename:
            if photo == my_face:
               face_list.remove(photo)
        my_pics = []
        for face in tqdm(face_list):
            face_encoding = find_face(face)
            # Face_match is broken. Standard compare_faces from facial_recognition works great.
            # Either fix face_match or continue using compare_faces
            """
            results = face_match([face_encoding], my_face)
            if results[0] == True:
                print "This works!"
                move_to_folder(face)
            else:
                continue
            """
            results = fr.compare_faces([my_face], face_encoding)
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
