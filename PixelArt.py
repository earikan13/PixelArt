#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:10:47 2022

@author: efearikan
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
import imageio.v3 as iio
import time
from pygifsicle import optimize


class PixelArt:

    def __init__(self, img, imgExtension):
        self.imgName = str(img)
        self.img = cv2.imread(self.imgName + '.' + str(imgExtension))
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.imgHeight, self.imgWidth = self.img.shape[:-1]

    def pixelImage(self):
        scale_percent = 3  # percent of original size
        width = int(self.img.shape[1] * scale_percent / 100)
        height = int(self.img.shape[0] * scale_percent / 100)
        self.pixelledImage = cv2.resize(
            self.img, (width, height), interpolation=cv2.INTER_LINEAR)
        self.pixelledImage = cv2.resize(
            self.pixelledImage, (self.imgWidth, self.imgHeight), interpolation=cv2.INTER_NEAREST)

    def combineImages(self, step):
        step = int(self.imgWidth * step / 100)
        tmpPixelImg = self.pixelledImage[:, :step]
        tmpImg = self.img[:, step:]
        self.combinedImg = np.hstack((tmpPixelImg, tmpImg))

    def generateGIF(self, dur=5):
        images = []
        for i in np.arange(0, 100, 5):
            self.combineImages(i)
            images.append(self.combinedImg)
        iio.imwrite('PixelledGIF.gif', images, duration=dur)
        optimize('PixelledGIF.gif')

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


def main():
    start = time.process_time()
    pA = PixelArt("exampleImg", "jpg")
    pA.pixelImage()
    # pA.plotImage()
    pA.generateGIF(0.5)
    print(time.process_time() - start)


main()
