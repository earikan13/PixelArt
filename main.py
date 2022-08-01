#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:20:41 2022

@author: efearikan
"""

from PixelArt import PixelArt
import time

waitDuration = 0.5


def main():
    pA = PixelArt("exampleImg", "jpg")
    pA.pixelImage()
    pA.generateGIF(waitDuration)


if __name__ == "__main__":
    main()
