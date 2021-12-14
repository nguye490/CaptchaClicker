# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:00:32 2021

@author: brian
"""
import pyautogui as pt
import os
from os import listdir
from os.path import isfile, join
import tensorflow as tf
from keras.preprocessing import image
import numpy as np

IMAGE_FOLDER = 'images/'

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            x, y = pt.locateCenterOnScreen(self.target_png, confidence=.25)
            pt.moveTo(x, y, duration=self.speed)
            pt.click()
        except:
            print('No image found...')
            return 0
        
class FindImages:
    def __init__(self, fPath):
        self.mypath = fPath
    def getImages(self):
        onlyfiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        return onlyfiles
    
    def ml(self, filename, search):
       model = tf.keras.models.load_model('model.h5')
       path = os.path.join(self.mypath, filename)
       img = image.image.load_img(path, target_size=(32, 32))
       x = image.img_to_array(img)
       x = np.expand_dims(x, axis=0)
       captcha = model.predict(x)
       
       if captcha[0:search].any:
           return True
       else:
           return False

if __name__ == '__main__':
    findImages = FindImages(IMAGE_FOLDER)
    files = findImages.getImages()
    print('What is captcha searching for?\n'  
          "0 is airplane\n"
          "1 is automobile or car\n"
          "2 is bird\n"
          "3 is cat\n"
          "4 is deer\n"
          "5 is dog\n"
          "6 is frog\n"
          "7 is horse\n"
          "8 is ship or boat\n"
          "9 is truck or bus\n")
   
    search = input()
    
    for i in files:
        clicker = Clicker(IMAGE_FOLDER + str(i), speed=.001)
        end = 0
        while findImages.ml(str(i), int(search)) == True:

            if clicker.nav_to_image() == 0:
                end += 1
            else:
                end = 6
            # End the loop
            if end > 5:
                break
