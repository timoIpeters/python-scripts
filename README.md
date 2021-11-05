# python-scripts

## System Details
A script that provides **system**, **boot**, **CPU**, **RAM**, **SWAP**, **disk**, **GPU** and **network** information

Prerequisites:
> pip install gputil
> pip install psutil

Usage:
    -a --all     **_All Possible Details_**
    -s --system   **_System Details_**
    -b --boot     **_Boot Time_**
    -c --cpu      **_CPU Details_**
    -r --ram      **_RAM Information_**
    -S --swap     **_SWAP Information_**
    -d --disk     **_Disk Information_**
    -g --gpu      **_GPU Details_**
    -n --network  **_Network Information_**

## GIF Creator
A script that generates GIFs from a specified set of images.

Prerequisites:
> pip install Pillow

Usage:
python createGif.py [?args] [?options]

options
    -h --help                         Prints this usage
    -d <ms>
    --duration <ms>                   Set the GIFs duration in ms
    -l <number>
    -loop <number>                    Sets the amount of image loops (0=forever)
    -s <directoryPath>
    --sourcePath <directoryPath>      Sets the directory path of the input images
    -o <directoryPath>
    --destinationPath <directoryPath> Sets the destination directory of the gif
    -f <JPG/PNG>
    --filetype <JPG/PNG>              Sets the file type of the input images
