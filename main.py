# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:00:32 2021

@author: brian
"""
import pyautogui as pt
from os import listdir
from os.path import isfile, join

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
    def getImages(self, mypath):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return onlyfiles

if __name__ == '__main__':
    findImages = FindImages()
    files = findImages.getImages('images')
    
    for i in files:
        print(str(i))
        clicker = Clicker('images/' + str(i), speed=.001)
        end = 0
        while True:

            if clicker.nav_to_image() == 0:
                end += 1
            else:
                end = 6
            # End the loop
            if end > 5:
                break
