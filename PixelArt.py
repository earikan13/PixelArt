#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:10:47 2022

@author: efearikan
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from PIL import Image, ImageEnhance

class PixelArt:

    def __init__(self, img, imgExtension, downscalePerc=10):
        self.downscalePerc = downscalePerc
        self.imgName = str(img).rsplit('/', -1)[-1]
        self.path = os.path.dirname(os.path.dirname(img))
        self.img = Image.open(img + '.' + str(imgExtension))
        self.imgWidth, self.imgHeight = self.img.size[:2]
        if self.imgHeight != 320 or self.imgWidth != 480:
            self.imgHeight = 320
            self.imgWidth = 480
            self.img = self.img.resize((self.imgWidth, self.imgHeight), Image.BILINEAR)
            self.img.save(img + '.' + imgExtension)
        self.img = self.img.convert('L')
        self.img = Image.eval(self.img, lambda px: (255 - px))
        #self.img = Image.blend(self.img, self.img, 0.4)
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(0.5)
        self.img = Image.eval(self.img, lambda px: (px - 110))
        
    def pixelImage(self):
        scale_percent = 3 * self.downscalePerc  # percent of original size
        width = int(self.img.size[1] * scale_percent / 150)
        height = int(self.img.size[0] * scale_percent / 150)
        self.pixelledImage = self.img.resize(
            (width, height), Image.BILINEAR)
        self.pixelledImage = self.pixelledImage.resize(
            (self.imgWidth, self.imgHeight), Image.NEAREST)

    def combineImages(self, step, direction):
        _image_pix = np.asarray(self.pixelledImage)
        _image = np.asarray(self.img)
        if direction == 0:  # Left to right
            step = int(self.imgWidth * step / 100)
            tmpPixelImg = _image_pix[:, :step]
            tmpImg = _image[:, step:]
            combinedImg = np.hstack((tmpPixelImg, tmpImg))
        elif direction == 1:  # Right to left
            step = int(self.imgWidth * step / 100)
            tmpPixelImg = _image_pix[:,
                                             self.pixelledImage.size[0]-step:]
            tmpImg = _image[:, :self.pixelledImage.size[0]-step]
            combinedImg = np.hstack((tmpImg, tmpPixelImg))
        elif direction == 2:  # Down to up
            step = int(self.imgHeight * step / 100)
            tmpPixelImg = _image_pix[self.pixelledImage.size[1]-step:]
            tmpImg = _image[:self.pixelledImage.size[1]-step]
            combinedImg = np.vstack((tmpImg, tmpPixelImg))
        elif direction == 3:  # Up to down
            step = int(self.imgHeight * step / 100)
            tmpPixelImg = _image_pix[:step]
            tmpImg = _image[step:]
            combinedImg = np.vstack((tmpPixelImg, tmpImg))
        return combinedImg
    
    def generateGIF(self):
        directory = Path(self.path + "/Out/" + self.imgName)
        if not os.path.exists(directory):
            os.makedirs(directory)
        direction = self.generateDirection()
        cnt = 0
        for i in np.arange(0, 105, 5):
            img_name = str(directory) + '/' + self.imgName + '-' + str(cnt) + ".png"
            img = self.combineImages(i, direction)
            Image.fromarray(img).save(img_name)
            cnt += 1

    def generateDirection(self):
        # 0->left, 1->right, 2->up, 3->down
        direction = np.random.choice([0,1,2,3])
        return direction

    def plotImage(self):
        fig, ax = plt.subplots()
        imgPlt = ax.imshow(self.combinedImg)
        imgPlt.set_cmap('hot')
        ax.axis("off")
        fig.savefig("Pixelled" + self.imgName + '.' + 'png',
                    bbox_inches='tight', pad_inches=0, dpi=300)
