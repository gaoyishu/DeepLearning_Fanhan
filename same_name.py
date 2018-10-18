import os
import shutil


PicFilePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'img127_data')
FileNamePath = 'test127.txt'


def GetFileNameAndExt(picpath):
    img_source = os.listdir(picpath)
    with open(FileNamePath,'r') as NameFile:
        for line in NameFile.readlines():
            img_name = line.strip().split(',')[0]
            print(img_name)
            for img in img_source:
                if img_name == img:
                    abs_img = os.path.join(PicFilePath,img)
                    shutil.copy(abs_img, '.')

if __name__ == '__main__':
    GetFileNameAndExt(PicFilePath)
