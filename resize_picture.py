"""
This file contains the picture preprocessing on two purpose:
1. resize the all the picture to the row of 480 and col of 480.
2. adjustment of landmarks position referring to the resized pictures.
"""


import os
import cv2
import numpy as np

#rows
img_rows =480
#cols
img_cols = 480
#file path can be changed for other data use.
PICTURE_FILE = '/home/yishu/Desktop/detector127/test127'


def rewrite_size(filename, r_ratio, c_ratio):
    f_read = open(PICTURE_FILE + '/' + 'test127.txt', 'r')
    f_in = open(PICTURE_FILE + '/' + 'test127_resize.txt', 'a')
    for line in f_read.readlines():
        line = line.strip().split(',')
        #one line contains 254 numbers for 127 points and one filename
        if len(line) != 255:
            continue
        else:
            str_sum = ""
            # print(len(line))
            if filename == line[0]:
                num = 1
                #attention pls of out of index
                while num < len(line):
                    if (num % 2) == 0:
                        num_resize = int(int(line[num]) * c_ratio)
                    else:
                        # print(num)
                        num_resize = int(int(line[num]) * r_ratio)
                    str_sum += str(num_resize) + ','
                    num += 1
                f_in.write(filename+ ','+ str_sum[:-1]+ '\n')
                f_in.close()
    f_read.close()


def image_resize(file_path):
    for label_name in os.listdir(file_path):
        image = cv2.imread(PICTURE_FILE + '/' +label_name)
        #estimation of data type
        if image is None:
            continue
        else:
            print(label_name)
            print(image.shape)
            rows_ratio = img_rows/image.shape[0]
            cols_ratio = img_cols/image.shape[1]
            print(rows_ratio, cols_ratio)
            image = cv2.resize(image, (img_rows, img_cols), interpolation=cv2.INTER_CUBIC)
            rewrite_size(label_name, rows_ratio, cols_ratio)
            cv2.imwrite("/home/yishu/Desktop/detector127/resize_test127/" + label_name, image)


        # data.append(image)
        # data = np.array(data)
        # data = data.astype('float32')
        # return data



# def sample():
#     line = ['.jpg',83,171,84,187,85,205,88,223,93,237,99,254,109,267,121,279,152,293,175,291,193,280,206,269,217,254,223,236,227,214,230,191,230,170,94,167,103,161,116,159,131,161,138,167,173,167,186,159,200,157,212,162,219,168,157,193,158,204,157,211,157,220,144,230,150,230,158,236,163,230,169,231,103,185,116,179,132,180,139,191,128,193,115,191,176,191,183,182,195,179,210,185,199,192,186,194,128,254,139,253,147,249,157,249,167,249,174,251,182,252,174,260,166,263,156,263,146,263,139,259,142,256,147,254,158,255,168,254,172,256,167,257,157,257,147,256,105,166,114,166,124,166,184,167,194,165,206,164,98,175,108,172,118,171,129,172,139,174,100,181,109,177,119,174,130,176,139,180,174,175,185,172,196,170,206,173,216,176,175,182,186,177,196,175,205,177,215,180,120,185,126,191,133,185,127,178,127,184,183,186,189,191,195,185,189,178,189,184,99,188,108,193,116,196,127,197,139,195,174,195,183,198,194,199,203,197,212,191,147,194,146,201,146,209,143,218,165,193,166,201,169,209,171,215,110,223,206,224,164,96,94,124,221,121]
#     print(len(line))
#     i = 1
#     while i < len(line):
#         if (i % 2) == 0:
#             print(line[i])
#         else:
#
#             print(line[i])
#         i += 1

if __name__ == '__main__':
    image_resize(PICTURE_FILE)
    # sample()
