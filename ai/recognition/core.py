import face_recognition as fr
from ai.core.image import Image
from fastapi.exceptions import HTTPException
import PIL.Image , PIL.ImageDraw
import numpy as np
import math
import cv2


GREEN = "#00FF00"

class Recognition:
    def __init__(self, image=None, path=None):
        if image:
            self.image = image
        elif path:
            self.image = Image(path=path)
        else:
            raise HTTPException('you mush load an image')
        

    @staticmethod
    def find_encoding(path):
        _image = Image(path=path).grey()
        encoded_image = fr.face_encodings(_image)
        return encoded_image
    
    @staticmethod
    def find_landmarks(path):
        _image = fr.load_image_file(path)
        face_landmarks_list = fr.face_landmarks(_image)
        pil_image = PIL.Image.fromarray(_image)
        draw_landmarks = PIL.ImageDraw.Draw(pil_image)

        for face_landmarks in face_landmarks_list:
            for facial_features in face_landmarks.keys():

                face_landmarks_max = [[int(j+2) for j in i] for i in face_landmarks[facial_features]]
                face_landmarks_max = [tuple(i) for i in face_landmarks_max]
                face_landmarks_min = [[int(j-2) for j in i] for i in face_landmarks[facial_features]]
                face_landmarks_min = [tuple(i) for i in face_landmarks_min]

                for i in range(len(face_landmarks_min)):
                               draw_landmarks.ellipse((face_landmarks_min[i]+face_landmarks_max[i]), fill=GREEN, outline=None, width=2)

        return pil_image
        
    @staticmethod
    def compare_images(first_image_path, second_image_path, facial_landmarks=True, tolerance=0.45):
        unknown_encoding = Recognition.find_encoding(path=first_image_path)
        original_encoding = Recognition.find_encoding(path=second_image_path)
        if not original_encoding:
            raise HTTPException(status_code=404, detail="Item not found")
        face_matches = fr.compare_faces(original_encoding, unknown_encoding[0], tolerance=tolerance)
        face_distance = fr.face_distance(original_encoding, unknown_encoding[0])
        match_index = np.argmin(face_distance)
        similarity_score = 100.0 if face_distance[match_index] == 0 else max(0.0, -12.285 + 102.993 * math.log(round(face_distance[match_index], 4)))
        similarity_score = round(similarity_score, 2)
        first_image = cv2.imread(str(first_image_path))
        second_image = cv2.imread(str(second_image_path))
        if original_encoding and face_matches[match_index]:
            bound_image = Image(path=second_image_path).grey()
            face_location = fr.face_locations(bound_image)
            y1, x2, y2, x1 = face_location[match_index]
            cv2.rectangle(bound_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        if facial_landmarks:
            face_landmark_image1 = Recognition.find_landmarks(first_image_path)
            face_landmark_image2 = Recognition.find_landmarks(second_image_path)
            landmark_image_url1 = Image.image2url(np.array(face_landmark_image1))
            landmark_image_url2 = Image.image2url(np.array(face_landmark_image2))

        else:
            landmark_image_url1 = None
            landmark_image_url2 = None
        result = {
            "is_similar": bool(face_matches[match_index]),
            "similarity": similarity_score,
            "match_index": match_index + 1,
            "nfaces": len(original_encoding),
            "image1":Image.image2url(first_image),
            "image1_landmark":landmark_image_url1,
            "image2": Image.image2url(second_image),
            "image2_landmark": landmark_image_url2
        }
        return result
