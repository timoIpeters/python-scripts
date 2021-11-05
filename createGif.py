#!/usr/bin/python
import sys
import glob
import getopt

from PIL import Image
from datetime import datetime

def createGif(source_path, destination_path, duration, loop, filetype):
    images = [Image.open(image) for image in glob.glob(f'{source_path}/*.{filetype}')]
    firstImage = images[0]
    datetimeObj = datetime.now()
    formatDatetime = str(datetimeObj.year) + '-' + str(datetimeObj.month) + '-' + str(datetimeObj.day) + '_' + str(datetimeObj.hour) + '_' + str(datetimeObj.minute) + '_' + str(datetimeObj.second)

    firstImage.save(destination_path + 'generatedGif_' + formatDatetime + '.gif', format='GIF', append_images=images, save_all=True, duration=duration, loop=loop)
    print('Generated GIF saved to ', destination_path)

def printUsage():
    print('Usage:')
    print('python createGif.py [?args] [?options]')
    print('')
    print('options')
    print('    -h --help                         Prints this usage')
    print('    -d <ms>')
    print('    --duration <ms>                   Set the GIFs duration in ms')
    print('    -l <number>')
    print('    -loop <number>                    Sets the amount of image loops (0=forever)')
    print('    -s <directoryPath>')
    print('    --sourcePath <directoryPath>      Sets the directory path of the input images')
    print('    -o <directoryPath>')
    print('    --destinationPath <directoryPath> Sets the destination directory of the gif')
    print('    -f <JPG/PNG>')
    print('    --filetype <JPG/PNG>              Sets the file type of the input images')

def main(argv):
    source_path = './exampleImages'
    destination_path = './'
    duration = 300
    loop = 0
    filetype = 'JPG'

    if argv != []:
        try:
            opts, args = getopt.getopt(argv, 'hd:l:s:o:f:', ['help', 'duration=', 'loop=', 'sourcePath=', 'destinationPath=', 'filetype='])
        except getopt.GetoptError:
            printUsage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                printUsage()
                sys.exit()
            elif opt in ('-d', '--duration'):
                duration = int(arg)
            elif opt in ('-l', '--loop'):
                loop = int(arg)
            elif opt in ('-s', '--sourcePath'):
                source_path = str(arg)
            elif opt in ('-o', '--destinationPath'):
                destination_path = str(arg)
            elif opt in ('-f', '--filetype'):
                filetype = str(arg).upper()

    createGif(source_path, destination_path, duration, loop, filetype)

if __name__ == '__main__':
    main(sys.argv[1:])
