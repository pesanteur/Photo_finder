# Photo_finder
Finds photos with faces in the current working directory, then copies these photos into a folder. More specific "me" command
finds photos of a particular person.

# Usage
```
python photo_finder me -f /path/to/filename.jpg

python photo_finder all
```
Using the command 'python photo_finder me -f /path/to/filename.jpg' the script is able to find photos in the working directory
that contain the face in '/path/to/filename.jpg'. These photos are then placed in a directory called Faces. 

If the command 'python photo_finder all' is used the code finds all photos with faces in them and places them in the Faces directory.

# Motivation
I created this project as a means of getting to know the facial_recognition project. 
