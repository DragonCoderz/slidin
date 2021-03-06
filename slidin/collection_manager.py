# (Done) TODO: Create service account for S3 to upload images

#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
from pprint import pprint

# (Done) TODO: Implement function to create a collection

def create_collection(collection_id):

    client=boto3.client('rekognition')

    #Create a collection
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')

def add_faces_to_collection(bucket,photo,collection_id,max_faces):
    client=boto3.client('rekognition')

    response=client.index_faces(CollectionId=collection_id,
                                Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                ExternalImageId=photo,
                                MaxFaces=max_faces,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    print ('Results for ' + photo) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return response['FaceRecords']

    
#TODO: Implement function to check face against existing database of faces and return matches

def search_faces_in_collection(face_id,collection_id):
    threshold = 90
    max_faces=2
    client=boto3.client('rekognition')

    response=client.search_faces(CollectionId=collection_id,
                            FaceId=face_id,
                            FaceMatchThreshold=threshold,
                            MaxFaces=max_faces)

                    
    face_matches=response['FaceMatches']
    print ('Matching faces')
    for match in face_matches:
        print ('FaceId:' + match['Face']['FaceId'])
        print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
    return face_matches

