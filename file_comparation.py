import os

filepath = os.path.dirname(__file__)

def file_compare():
    with open(filepath + '/train127_resize.txt', 'r') as f:
        #first create a list to store the name in txt
        name_list = []
        for line in f.readlines():
            line = line.strip().split(',')[0]
            name_list.append(line)
        print(name_list)
        filename = os.listdir(filepath)
        print(filename)
        for file in filename:
            if file.endswith('jpg'):
                if file not in name_list:
                    print(file)
                    os.remove(filepath + '/' + file)






if __name__ == '__main__':
    file_compare()
