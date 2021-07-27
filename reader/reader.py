import cv2
from cv2 import imread
import matplotlib.pyplot as plt
from nptyping import NDArray, Bool
from abc import ABC, abstractmethod

class ImReader(ABC):
    @abstractmethod
    def read(self) -> NDArray:
        raise NotImplementedError
        
    def show(self):
        if hasattr(self,'img'):
            plt.imshow(self.img)
            plt.show()

class JPGReader(ImReader):

    def __init__(self, path = None):
        self.path = path

    def read(self):
        if self.path is None:
            raise ValueError("JPG reader missing attribute `path`, use `set_path` method.")

        img = imread(self.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img = img
        return img

    def set_path(self, path):
        self.path = path
        return self