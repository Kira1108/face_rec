import face_recognition
import logging
import os
logger = logging.getLogger(__name__)

class FaceRegister():

    def __init__(self):
        self.known_faces = {}

    def register_from_numpy(self, name, img):
        try:
            encoding = face_recognition.face_encodings(img)[0]
        except:
            logger.info("Unable to locate face in image")
        self.known_faces[name] = encoding


    def register_from_file(self, name, path):
        img = face_recognition.load_image_file(path)
        self.register_from_numpy(name, img)


    def register_from_folder(self, folder_path):
        files = os.listdir(folder_path)

        files = {file.split('.')[0]:os.path.join(folder_path, file) 
                for file in files}
        for name, file_path in files.items():
            self.register_from_file(name, file_path)
        




            

