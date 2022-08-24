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
import show

possibleExtensions = [".JPG", ".jpg", ".PNG", ".png", ".JPEG", ".jpeg"]

def main(args):
    #args = sys.argv[1]
    currentDir = os.getcwd()
    photosDir = currentDir + '/' + 'Images'
    path = Path(photosDir)
    while (True):
        for filename in os.listdir(path):
            if filename.endswith(tuple(possibleExtensions)):
                filename, ext = filename.rsplit('.', 1)
                tmpPath = Path(currentDir + '/' + "GIFs" + '/' +
                               "Pixelled" + filename + ".gif")
                #if not os.path.isfile(tmpPath) or args == 1:
                pA = PixelArt(photosDir + '/' + filename, ext)
                pA.pixelImage()
                pA.generateGIF()
                show.main()



if __name__ == "__main__":
    main(1)
    sys.exit(0)
