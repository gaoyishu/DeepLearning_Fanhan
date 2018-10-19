"""
This file is used for detect the 127 points for face facilitation to handy-facial landmarks.
"""


import os
import cv2
import numpy as np
import dlib

dir_path = os.path.dirname(__file__)
pic_path = os.path.join(dir_path,'img127_data/4.jpg')

#二等分距离
def half_dis(point_smaller_pos, point_bigger_pos):
    dis = int((point_bigger_pos - point_smaller_pos) / 2)
    return dis

#三等分距离
def third_dis(point_smaller_pos, point_bigger_pos):
    dis = int((point_bigger_pos - point_smaller_pos) / 3)
    return dis


#四等分距离
def quarter_dis(point_smaller_pos, point_bigger_pos):
    dis = int((point_bigger_pos - point_smaller_pos) / 4)
    return dis


#五等分距离
def fifth_dis(point_smaller_pos, point_bigger_pos):
    dis = int((point_bigger_pos - point_smaller_pos) / 5)
    return dis

#计算坐标点的x值
def get_x_num(numpy_list):
    num = numpy_list.tolist()[0][0]
    return num

#计算坐标点的y值
def get_y_num(numpy_list):
    num = numpy_list.tolist()[0][1]
    return num


def point127_art(file_path):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    image = cv2.imread(pic_path, cv2.IMREAD_ANYCOLOR)
    rects = detector(image, 1)
    marks68 = np.matrix([(p.x, p.y) for p in predictor(image, rects[0]).parts()])
    empty_matrix = np.zeros((59,2),dtype=int)
    # 68 pos
    empty_matrix[0] = [get_x_num(marks68[18]) + 2,
                                get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
                                                                   get_y_num(marks68[36]))]
    # 75 pos
    empty_matrix[0] = [get_x_num(marks68[18]) + 1,
                       get_y_num(marks68[18]) + 2 * fifth_dis(get_y_num(marks68[18]),
                                                          get_y_num(marks68[36]))]
    # 80 pos
    empty_matrix[0] = [get_x_num(marks68[18]) + 1,
                       get_y_num(marks68[18]) + 3 * fifth_dis(get_y_num(marks68[18]),
                                                          get_y_num(marks68[36]))]
    # 74 pos
    empty_matrix[0] = [get_x_num(marks68[17]) + 1,
                       get_y_num(marks68[17]) + quarter_dis(get_y_num(marks68[17]),
                                                          get_y_num(marks68[36]))]
    # 79 pos
    empty_matrix[0] = [get_x_num(marks68[17]) + 2,
                       get_y_num(marks68[17]) + 2 * quarter_dis(get_y_num(marks68[17]),
                                                          get_y_num(marks68[36]))]
    # 69 pos
    empty_matrix[0] = [get_x_num(marks68[19]),
                       get_y_num(marks68[19]) + fifth_dis(get_y_num(marks68[19]),
                                                          get_y_num(marks68[37]))]
    # 76 pos
    empty_matrix[0] = [get_x_num(marks68[19]),
                       get_y_num(marks68[19]) + 2 * fifth_dis(get_y_num(marks68[19]),
                                                          get_y_num(marks68[37]))]
    # 81 pos
    empty_matrix[0] = [get_x_num(marks68[19]),
                       get_y_num(marks68[19]) + 3 * fifth_dis(get_y_num(marks68[19]),
                                                          get_y_num(marks68[37]))]
    # 70 pos
    empty_matrix[0] = [get_x_num(marks68[20]) + 2,
                       get_y_num(marks68[20]) + fifth_dis(get_y_num(marks68[20]),
                                                          get_y_num(marks68[38]))]
    # 77 pos
    empty_matrix[0] = [get_x_num(marks68[20]),
                       get_y_num(marks68[20]) + 2 * fifth_dis(get_y_num(marks68[20]),
                                                          get_y_num(marks68[38]))]
    # 82 pos
    empty_matrix[0] = [get_x_num(marks68[20]),
                       get_y_num(marks68[20]) + 3 * fifth_dis(get_y_num(marks68[20]),
                                                          get_y_num(marks68[38]))]
    # 78 pos
    empty_matrix[0] = [get_x_num(marks68[21]) + 2,
                       get_y_num(marks68[21]) + quarter_dis(get_y_num(marks68[21]),
                                                          get_y_num(marks68[36]))]
    # 83 pos
    empty_matrix[0] = [get_x_num(marks68[21]) + 2,
                       get_y_num(marks68[21]) + quarter_dis(get_y_num(marks68[21]),
                                                          get_y_num(marks68[36]))]
    # 94 pos
    empty_matrix[0] = [get_x_num(marks68[36]) + fifth_dis(get_x_num(marks68[36]),get_x_num(marks68[39])),
                                                          get_y_num(marks68[36])]
    # 98 pos
    empty_matrix[0] = [get_x_num(marks68[36]) + 2 * fifth_dis(get_x_num(marks68[36]),get_x_num(marks68[39])),
                                                          get_y_num(marks68[36])]
    # 96 pos
    empty_matrix[0] = [get_x_num(marks68[36]) + 3 * fifth_dis(get_x_num(marks68[36]),get_x_num(marks68[39])),
                                                          get_y_num(marks68[36])]
    # 97 pos
    empty_matrix[0] = [get_x_num(marks68[37]) + half_dis(get_x_num(marks68[37]),
                                                           get_x_num(marks68[38])),
                       get_y_num(marks68[37]) + fifth_dis(get_y_num(marks68[37]),
                                                          get_y_num(marks68[41]))]
    # 95 pos
    empty_matrix[0] = [get_x_num(marks68[41]) + half_dis(get_x_num(marks68[41]),
                                                           get_x_num(marks68[40])),
                       get_y_num(marks68[37]) + 3 * fifth_dis(get_y_num(marks68[37]),
                                                          get_y_num(marks68[41]))]
    # 98 pos
    empty_matrix[0] = [get_x_num(marks68[18]) + 2,
                       get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
                                                          get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]
    # empty_matrix[0] = [get_x_num(marks68[18]) + 2,
    #                    get_y_num(marks68[18]) + fifth_dis(get_y_num(marks68[18]),
    #                                                       get_y_num(marks68[36]))]

    #transfer numpy.array to numpy.matrix
    empty_matrix =np.matrix(empty_matrix)

    # print(empty_matrix)
    for index,point in enumerate(empty_matrix):
        pos = (point[0,0], point[0,1])
        print(index, point)
        print(type(point))

        #
        cv2.circle(image, pos, 5, color=(0, 255, 0))
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(image, str(index), pos, font, 0.4, (0, 0, 255), 1, cv2.LINE_AA)



    cv2.imshow('img', image)
    cv2.waitKey(0)

if __name__ == '__main__':
    point127_art(pic_path)
