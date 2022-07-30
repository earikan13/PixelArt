#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:10:47 2022

@author: efearikan
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np


class PixelArt:

    def __init__(self, img, imgExtension):
        self.imgName = str(img)
        self.img = cv2.imread(self.imgName + '.' + str(imgExtension))
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.imgHeight, self.imgWidth = self.img.shape[:-1]
        print((self.imgHeight, self.imgWidth))

    def pixelImage(self):
        scale_percent = 3  # percent of original size
        width = int(self.img.shape[1] * scale_percent / 100)
        height = int(self.img.shape[0] * scale_percent / 100)
        self.pixelledImage = cv2.resize(
            self.img, (width, height), interpolation=cv2.INTER_LINEAR)
        self.pixelledImage = cv2.resize(
            self.pixelledImage, (self.imgWidth, self.imgHeight), interpolation=cv2.INTER_NEAREST)
        print(self.pixelledImage.shape)

    def combineImages(self):
        tmpPixelImg = self.pixelledImage[:, :self.imgWidth//2]
        tmpImg = self.img[:, self.imgWidth//2:]
        self.combinedImg = np.hstack((tmpPixelImg, tmpImg))

    def generateDirection(self):
        rng = np.random.default_rng()
        # 0->left, 1->right, 2->up, 3->down
        direction = rng.integers(low=0, high=4, size=1)

    def plotImage(self):
        fig, ax = plt.subplots()
        imgPlt = ax.imshow(self.combinedImg)
        imgPlt.set_cmap('hot')
        ax.axis("off")
        fig.savefig("Pixelled" + self.imgName + '.' + 'png',
                    bbox_inches='tight', pad_inches=0, dpi=300)
