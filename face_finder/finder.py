import cv2
from cv2 import CascadeClassifier
from nptyping import NDArray
from abc import ABC, abstractmethod
from typing import List
import os
import urllib.request


class FaceBoxFinder(ABC):
    """
        FaceBoxFinder interface defines an abstract method `detect`
        
    
    """
    @abstractmethod
    def detect(self, img:NDArray) -> List[List]:
        raise NotImplementedError

    def draw(self, img:NDArray) -> NDArray:
        boxes = self.detect(img)

        for x, y, width, height in boxes:
            x2, y2 = x + width, y + height
            img = cv2.rectangle(img, (x, y), (x2, y2), (255,0,0), 1)

        return img


class CascadeFinder(FaceBoxFinder):

    MODEL_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"

    def __init__(self, model_path = None, model_file_name = None):
        self.path = model_path if model_path \
                    else "./resources/cascade_model"

        self.model_file_name = model_file_name if model_file_name  \
                    else 'haarcascade_frontalface_default.xml'

        self.file_path = os.path.join(self.path, self.model_file_name)

        self._post_init()

    def _post_init(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if not os.path.exists(self.file_path):
            urllib.request.urlretrieve(CascadeFinder.MODEL_URL, self.file_path)

        self.classifier = CascadeClassifier(self.file_path)  

    def detect(self, img:NDArray) -> List[List]:
        return self.classifier.detectMultiScale(img)