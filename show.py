#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:18:02 2022

@author: efearikan
"""

import os
from pathlib import Path
import subprocess
from time import sleep

currentDir = os.getcwd() + "/Out"
path = Path(currentDir)

def create_piclist():
    pngs = str(os.getcwd()) + "/*.png >"
    piclist = str(os.getcwd()) + "/piclist.txt"
    _ = subprocess.run(["ls", "-1v", "-1", pngs, piclist],shell=True)

def kill_fbi():
    _ = subprocess.run(["killall", "-9", "fbi"])
    
def sleep_for_dur(sleep_dur):
    sleep(sleep_dur * 21)
    
def animate(sleep_dur):
    _ = subprocess.run(["sudo", "fbi", "-d", "/dev/fb0", "-T", "1", "-t", str(sleep_dur), "--noverbose", "--once", "--list", "piclist.txt"])
    
def main():
    subprocess.run(["killall", "-9", "fbi"])
    for filename in os.listdir(path):
      if os.path.isdir(Path(currentDir + '/'  + filename)):
         os.chdir(Path(currentDir + '/'  + filename))
         create_piclist() 
         animate(120)
         sleep_for_dur(120)
         _ = subprocess.run(["killall", "-9", "fbi"])
