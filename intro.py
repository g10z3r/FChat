import operator
import shutil
from termcolor import colored

textIntro = ['\t\x1b[0;36m[---]\t\tConsole Chat\x1b[0m \033[93m(FChat)\033[00m\t\t\x1b[0;36m[---]\x1b[0m',
'\t\x1b[0;36m[---]\tCreated by:\x1b[0m \033[91mEgor Sobolev\033[00m \033[93m(Gefion)\033[00m\t\x1b[0;36m[---]\x1b[0m',
'\t\x1b[0;36m[---]\t\t   Version\x1b[0m \033[91m2.0\033[00m \t\t\t\x1b[0;36m[---]\x1b[0m']


lines = [
'\n',
'\033[93m00001101000010100101011101100101001000000\033[00m',
'\033[93m11000010111001001100101001000000100000101\033[00m',
'\033[93m10111001101111011011100111100101101101011\033[00m',
'\033[93m10101011100110010111000100000010101110110\033[00m',
'\033[93m01010010000001100001011100100110010100100\033[00m',
'\033[93m00001001100011001010110011101101001011011\033[00m',
'\033[93m11011011100010111000100000010101110110010\033[00m',
'\033[93m10010000001100100011011110010000001101110\033[00m',
'\033[93m01101111011101000010000001100110011011110\033[00m',
'\033[93m11100100110011101101001011101100110010100\033[00m',
'\033[93m10111000100000010101110110010100100000011\033[00m',
'\033[93m00100011011110010000001101110011011110111\033[00m',
'\033[93m01000010000001100110011011110111001001100\033[00m',
'\033[93m11101100101011101000010111000100000010101\033[00m',
'\033[93m11011000010110100101110100001000000110011\033[00m',
'\033[93m00110111101110010001000000111010101110011\033[00m',
'\n'
]

width = shutil.get_terminal_size().columns
position = (width - max(map(len, textIntro))) // 2

def eggIntro():
    for line in lines: print('    ',line.center(width))

def intro():
    for text in textIntro: print(' '*position + text)
    print('\n')
