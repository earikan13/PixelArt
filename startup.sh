#!/bin/bash
sleep 15
source /home/efe/anaconda3/etc/profile.d/conda.sh
conda activate pixelart
cd /home/efe/Desktop/PixelArt
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`
echo "$TIMESTAMP - Running the script " >> Logfile.log
python3 main.py
sleep 1
if [ $? != 0 ];
then
	TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`
	echo "$TIMESTAMP - Exit 1" >> Logfile.log
fi
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`
echo "$TIMESTAMP - Script done. Opening GIFs" >> Logfile.log
sleep 5
DISPLAY=:0
cd /home/efe/Desktop/PixelArt/GIFs
eog --fullscreen --display=:0 PixelledexampleImg.gif
