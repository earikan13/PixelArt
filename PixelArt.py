#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:10:47 2022

@author: efearikan
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from pathlib import Path

class PixelArt:

    def __init__(self, img, imgExtension, downscalePerc=10):
        self.downscalePerc = downscalePerc
        self.imgName = str(img).rsplit('/', -1)[-1]
        self.path = os.path.dirname(os.path.dirname(img))
        self.img = cv2.imread(img + '.' + str(imgExtension))
        self.imgHeight, self.imgWidth = self.img.shape[:2]
        if self.imgHeight != 320 or self.imgWidth != 480:
            self.imgHeight = 320
            self.imgWidth = 480
            self.img = cv2.resize(
                self.img, (480, 320), cv2.INTER_LINEAR)
            cv2.imwrite(img + '.' + imgExtension, self.img)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = cv2.bitwise_not(self.img)        

    def pixelImage(self):
        scale_percent = 3 * self.downscalePerc  # percent of original size
        width = int(self.img.shape[1] * scale_percent / 100)
        height = int(self.img.shape[0] * scale_percent / 100)
        self.pixelledImage = cv2.resize(
            self.img, (width, height), interpolation=cv2.INTER_LINEAR)
        self.pixelledImage = cv2.resize(
            self.pixelledImage, (self.imgWidth, self.imgHeight), interpolation=cv2.INTER_NEAREST)

    def combineImages(self, step, direction):
        if direction == 0:  # Left to right
            step = int(self.imgWidth * step / 100)
            tmpPixelImg = self.pixelledImage[:, :step]
            tmpImg = self.img[:, step:]
            combinedImg = np.hstack((tmpPixelImg, tmpImg))
        elif direction == 1:  # Right to left
            step = int(self.imgWidth * step / 100)
            tmpPixelImg = self.pixelledImage[:,
                                             self.pixelledImage.shape[1]-step:]
            tmpImg = self.img[:, :self.pixelledImage.shape[1]-step]
            combinedImg = np.hstack((tmpImg, tmpPixelImg))
        elif direction == 2:  # Down to up
            step = int(self.imgHeight * step / 100)
            tmpPixelImg = self.pixelledImage[self.pixelledImage.shape[0]-step:]
            tmpImg = self.img[:self.pixelledImage.shape[0]-step]
            combinedImg = np.vstack((tmpImg, tmpPixelImg))
        elif direction == 3:  # Up to down
            step = int(self.imgHeight * step / 100)
            tmpPixelImg = self.pixelledImage[:step]
            tmpImg = self.img[step:]
            combinedImg = np.vstack((tmpPixelImg, tmpImg))
        return combinedImg
    
    def generateGIF(self, dur):
        directory = Path(self.path + "/Out/" + self.imgName)
        if not os.path.exists(directory):
            os.makedirs(directory)
        direction = self.generateDirection()
        for i in np.arange(0, 105, 5):
            img_name = str(directory) + '/' + self.imgName + '-' +str(i) + ".png"
            cv2.imwrite(img_name, self.combineImages(i, direction))
        

    def generateDirection(self):
        rng = np.random.default_rng()
        # 0->left, 1->right, 2->up, 3->down
        direction = rng.integers(low=0, high=4, size=1)
        return direction

    def plotImage(self):
        fig, ax = plt.subplots()
        imgPlt = ax.imshow(self.combinedImg)
        imgPlt.set_cmap('hot')
        ax.axis("off")
        fig.savefig("Pixelled" + self.imgName + '.' + 'png',
                    bbox_inches='tight', pad_inches=0, dpi=300)
