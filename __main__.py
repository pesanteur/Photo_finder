from utils import check_for_folder, photo_finder, move_to_folder
from face_finder import face_checker, find_face, face_match, find_all_faces
from tqdm import tqdm

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
        # me command is broken. Needs to be fixed. Run pdb here.
        my_face = find_face(args.filename)
        photo_list = photo_finder()
        face_list = face_checker(photo_list)
        import pdb; pdb.set_trace()
        for face in tqdm(face_list):
            face_encoding = find_face(face)
            results = face_match(face_encoding, my_face)
            if results[0] == True:
                move_to_folder(face)
            else:
                continue
    elif args.command == "all":
        find_all_faces()
        print "Worked!"
    else:
        parser.print_help()
        parser.exit(1)
        print "Did not work!"

if __name__ == "__main__":
    main()
