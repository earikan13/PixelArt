#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:18:02 2022

@author: efearikan
"""

import os
from pathlib import Path

currentDir = os.getcwd() + "/Out"
path = Path(currentDir)

def create_piclist():
    pwd = os.getcwd()
    os.system("ls -1v -1 " + pwd +"/*.png > " +pwd + "/piclist.txt")

def kill_fbi():
    os.system("sudo killall -15 fbi")
    
def animate(dur=2):
    os.system("fbi -d /dev/fb0 -T 1 -t " + str(dur) + " -cachemem 0 --noverbose --list piclist.txt")
    pass

def main():
    for filename in os.listdir(path):
        tmp=os.chdir(Path(currentDir + '/'  + filename))
        create_piclist()
        animate()
        kill_fbi()

