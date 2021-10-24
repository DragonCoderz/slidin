from interface import *

class User:
    def __init__(self, username, company, position, pfp, searchable, connections):
        self.username = username
        self.company = company
        self.position = position
        self.searchable = searchable
        self.face_id = add_profile(username, pfp)
        self.connections = []
    
    def find_matches_and_make_connections(self, picture):
        faces_found = upload_picture(picture)
        if faces_found:
            for face in faces_found:
                print('Found {} in this picture!'.format(face))
        else:
            print("Didn't find any faces in this picture.")
