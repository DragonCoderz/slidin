from collection_manager import *

id_to_username = {}
bucket = 'testimages-h'
collection_id='collectionhackGT2021testing'

def add_profile(username, pfp):
    face = add_faces_to_collection(bucket,pfp,collection_id,1)
    id_to_username[face[0]['Face']['FaceId']] = username

def upload_picture(photo):
    detected_faces=add_faces_to_collection(bucket,photo,collection_id,5)
    faces_found = []
    for face in detected_faces:
        face_id = face['Face']['FaceId']
        matched_faces=search_faces_in_collection(face_id, collection_id)
        for match in matched_faces:
            match = match['Face']['FaceId']
            if match in id_to_username:
                id_to_username[face_id] = id_to_username[match]
                faces_found.append(id_to_username[face_id])
                break

    return faces_found

