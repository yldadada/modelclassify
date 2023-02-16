import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import cv2

class SVM:
    def __init__(self, directory):
        self.directory = directory

    def get_picture(self, directory=None):
        s = 1
        class_num = 0
        if directory is None:
            directory = self.directory
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                class_num += 1
                

