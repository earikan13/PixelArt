#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:20:41 2022

@author: efearikan
"""

from PixelArt import PixelArt
import sys
import os
from pathlib import Path

waitDuration = 5
possibleExtensions = [".JPG", ".jpg", ".PNG", ".png", ".JPEG", ".jpeg"]


def main():
    currentDir = os.getcwd()
    photosDir = currentDir + '/' + 'Images'
    path = Path(photosDir)
    for filename in os.listdir(path):
        if filename.endswith(tuple(possibleExtensions)):
            filename, ext = filename.rsplit('.', 1)
            tmpPath = Path(currentDir + '/' + "GIFs" + '/' +
                           "Pixelled" + filename + ".gif")
            if not os.path.isfile(tmpPath):
                pA = PixelArt(photosDir + '/' + filename, ext)
                pA.pixelImage()
                pA.generateGIF(waitDuration * 1000)


if __name__ == "__main__":
    main()
    sys.exit(0)
