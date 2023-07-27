from PySide6.QtWidgets import QApplication, QMainWindow,QFileSystemModel,QFileDialog
from PySide6.QtGui import  *
from PySide6.QtCore import *
import configparser
import shutil
import cv2
from PIL import Image
import numpy as np
import csv

import matplotlib.pyplot as plt
import socket



class Robot:
    # Class variable shared across all instances
    # 0-not ready , 1- ready, 2- runing ,3-pause ,4-stop

    status_value = 0
    line_value = 0
    z_down = 77.00
    z_up = z_down + 15.00

    home_pos = [358.25, -4.63, 200.0, -82.49, 64.88, -85.21]
    draw_pos = [358.25, -4.63, z_down, -82.49, 64.88, -85.21]

    connect_ststus = False


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, value):
        # Instance variable specific to each instance
        self.instance_value = value


    def set_status_value(self, value):
        # Set the class variable to the given value
        Robot.status_value = value

    def get_status_value(self):
        # Get the class variable value
        return Robot.status_value

    def set_connect_status(self, value):
        # Set the class variable to the given value
        Robot.connect_ststus = value

    def get_connect_status(self):
        # Get the class variable value
        return Robot.connect_ststus

    def set_line_value(self, value):
        Robot.line_value = value

    def get_line_value(self):
        # Get the class variable value
        return Robot.line_value

    def set_home_pos(self, value):
        Robot.home_pos = value

    def get_home_pos(self):
        # Get the class variable value
        return Robot.home_pos

    def set_draw_pos(self, value):
        Robot.draw_pos = value

    def get_draw_pos(self):
        # Get the class variable value
        return Robot.draw_pos

    def set_draw_pos(self, value):
        Robot.draw_pos = value

    def get_draw_pos(self):
        # Get the class variable value
        return Robot.draw_pos

    def Connect(self):
        try:
            server_ip = '192.168.0.1'
            server_port = 49152
            Robot.client_socket.connect((server_ip, server_port))

            self.set_connect_status(True)
            self.set_status_value(1)

        except Exception as e:
            Robot.set_status_value(0)

    def Disconnect(self):
        if self.get_status_value()!=2:
            Robot.client_socket.close()
            self.set_status_value(0)
        else:
            print("Could not disconnect, robot running.")

    def SendData(self,bytes):
        if self.get_status_value()!=0:
            Robot.client_socket.sendall(bytes)

    def getData(self):
        if self.get_status_value() != 0:
            return Robot.client_socket.recv(1024)
        else:
            return None







class BackgroundTask(QThread):
    finished = Signal()  # Signal to indicate the background task has finished



    def run(self):
        robot = Robot(0)
        robot.set_status_value(0)
        if not robot.get_connect_status():
            robot.Connect()
        else:
            robot.set_status_value(1)

        if robot.get_status_value()==1:
            statusReady =True
        else:
            statusReady = False

        if statusReady:

            robdataCSV = CSV("roPosData.csv")
            lines = robdataCSV.ReadDate()

            startline = robot.get_line_value()
            robot.set_status_value(2)

            for i in range(startline, len(lines)):
                status = robot.get_status_value()
                if status ==2:
                    line = lines[i]
                    p = f' {line[0]},\r'
                    print(f' No:{i} command : {p}')

                    position_bytes = p.encode()
                    robot.SendData(position_bytes)
                    response = robot.getData()
                    # response = client_socket.recv(1024)
                    print('Received from server:', response)
                    # self.sleep(1)  # Simulate a time-consuming operation
                elif status == 3:
                    robot.set_line_value(i)
                    break
                elif status == 4:
                    robot.set_line_value(0)
                    break
            if robot.get_status_value()==2:
                robot.set_status_value(0)




        # # Your background task goes here
        # for i in range(1, 11):
        #     print(f"Processing: {i}")


        self.finished.emit()

class INIFile():

    def __init__(self,fileName):
        # Create an instance of ConfigParser
        self.config = configparser.ConfigParser()
        self.Filename = fileName

    def read(self,section_name,key_name):
        self.config.read(self.Filename)
        # Access values from the INI file
        value = self.config.get(section_name, key_name)
        return value

    def write(self,section_name,key_name,value):
        # Set values in the INI file
        self.config[section_name] = {key_name: value}

        # Write the changes to the INI file
        with open(self.Filename, 'w') as configfile:
            self.config.write(configfile)

    def update(self,section_name,key_name,new_value):
        self.config.read(self.Filename)
        # Update the value in the INI file
        self.config.set(section_name, key_name, new_value)

        # Write the changes back to the INI file
        with open(self.Filename, 'w') as configfile:
            self.config.write(configfile)

class Camera():
    def __init__(self,obj):
        self.Camera_Contain =obj

        self.frame_counter = 0
    def setup_camera(self):
        """Initialize camera.
        """
        self.video_size = self.Camera_Contain.size()
        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
        # self.capture.set(cv2.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
        # self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())



    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """

        _, frame = self.capture.read()

        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.Camera_Contain.setPixmap(QPixmap.fromImage(image))

    def CaptureImage(self):
        _, frame = self.capture.read()
        filename = f"frame_{self.frame_counter:04d}.jpg"
        imageLocation = f'Camera/{filename}'
        cv2.imwrite(imageLocation, frame)
        return imageLocation








class CSV():
    def __init__(self,fileName):
        self.filename=fileName

    def WriteData(self,data):
        with open(self.filename, 'w', newline='') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)

    def WriteArray(self,datas):
        with open(self.filename, 'w') as f:
            # Create a CSV writer object
            # csvwriter = csv.writer(csvfile)
            for data in datas:
                f.write(f'{data}\n')


    def SaveAsCSVFile(self,data):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for item in data:
                writer.writerow(item)

    def ReadDate(self):
        # Open the file in read mode
        with open(self.filename, 'r') as csvfile:
            # Create a CSV reader object
            csvreader = csv.reader(csvfile)

            # Read the data from the CSV file
            data = list(csvreader)
        return data

    def read_csv_file(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]

        return data

class ImageCore(QMainWindow,QFileDialog):
    def __init__(self):
        self.FileDialogBox = QFileDialog()
        self.FileDialogBox.setFileMode(QFileDialog.FileMode.AnyFile)


    def filebrowser(self,default_directory):
        # self.FileDialogBox.setDirectory()
        # directory_url = QUrl.fromLocalFile(default_directory)
        self.FileDialogBox.setDirectory(default_directory)
        fileName = self.FileDialogBox.getOpenFileName()
        print(fileName[0])
        return fileName[0]

    def Copyfile(self,src, dst):
        # print(dst)
        shutil.copyfile(src, dst)


def LoadImage(default_directory="Image/"):
    FileDialogBox = QFileDialog()
    FileDialogBox.setFileMode(QFileDialog.FileMode.AnyFile)
    FileDialogBox.setDirectory(default_directory)
    fileName = FileDialogBox.getOpenFileName()

    # img = cv2.imread(fileName[0], 0)
    # frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return fileName[0]



def ResizeImage(image,obj):
    image_path = image  # Replace with your image file path
    image = QImage()
    if image.load(image_path):
        resized_image = image.scaled(obj.width(), obj.height())
        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(resized_image)

        # Create a QLabel and display the QPixmap
        # label = QLabel(self)
        obj.setPixmap(pixmap)



def ShowImage(image,obj):
    size =  obj.width(),obj.height()
    im = Image.open(image)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("Image/tmp_color.png", "PNG")

    obj.setStyleSheet(f"background-image : url(Image/tmp_color.png);"
                                        f"background-position:center;"
                                        f"background-repeat: no-repeat;"
                                        f"background-size: cover;", )
def ClearImage(obj):
    pass

def conver_odd_integer(even_number):
    if even_number % 2 == 0:
        odd_number = even_number + 1
        return odd_number
    else:
        return even_number

def ConverLineImage(imagepath, blur = 1,threshold=100, line_length=100, line_gap=10):
    # imagePath = "Image/image.png"
    blurValue = conver_odd_integer(blur)

    img = cv2.imread(imagepath, cv2.IMREAD_COLOR)

    median_filtered = cv2.medianBlur(img,blurValue)
    # edges = cv2.Canny(median_filtered, 100, 150)
    imageGRAY = cv2.cvtColor(median_filtered, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imageGRAY, 50, 150, apertureSize=3)

    # cv2.THRESH_BINARY -The pixel intensity is set to the max value if it is greater than the threshold, otherwise, it is set to 0.
    # cv2.THRESH_BINARY_INV
    # cv2.THRESH_TRUNC
    # cv2.THRESH_TOZERO
    # cv2.THRESH_TOZERO_INV


    # _, threshold = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY)
    # contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    lines = []
    lines.append([0])
    for arr in contours:
        for data in arr:
            print(f'line {data[0][0]},{data[0][1]}')
            # line = np.array(data[0][0], data[0][1])
            line = [data[0][0], data[0][1]]
            lines.append(line)
        lines.append([1])

    return lines


    # median_filtered = cv2.medianBlur(img, 3)
    # edges = cv2.Canny(median_filtered, 100, 150)
    # _, threshold = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY)
    #
    # contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # lines = []
    # lines.append([0])
    # for arr in contours:
    #     for data in arr:
    #         print(f'line {data[0][0]},{data[0][1]}')
    #         # line = np.array(data[0][0], data[0][1])
    #         line = [data[0][0], data[0][1]]
    #         lines.append(line)
    #     lines.append([1])

    return lines


def ConverLineImage_old(imagepath):
    # imagePath = "Image/image.png"
    img = cv2.imread(imagepath, 0)
    median_filtered = cv2.medianBlur(img, 3)
    edges = cv2.Canny(median_filtered, 100, 150)
    _, threshold = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    lines = []
    lines.append([0])
    for arr in contours:
        for data in arr:
            print(f'line {data[0][0]},{data[0][1]}')
            # line = np.array(data[0][0], data[0][1])
            line = [data[0][0], data[0][1]]
            lines.append(line)
        lines.append([1])

    return lines

def SaveLineDataSCV(lines):
    # SaveAsCSVFile("lineData.csv")
    lineDatascv = CSV('lineData.csv')
    lineDatascv.SaveAsCSVFile(lines)
    # lineDatascv.WriteArray(lines)

def SaveRobotDataSCV(data):
    lineDatascv = CSV('robotData.csv')
    lineDatascv.SaveAsCSVFile(data)
    # lineDatascv.WriteArray(data)

def SaveRobotPosSCV(data):
    lineDatascv = CSV('roPosData.csv')
    # lineDatascv.SaveAsCSVFile(data)
    lineDatascv.WriteArray(data)

def SaveAsCSVFile(file_path,data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow(item)

def SaveAsCSVFile_string(file_path,data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def CreateLineImage(imagepath,lines):
    # img = cv2.imread(imagepath)
    im = cv2.imread(imagepath)
    width,height,channels = im.shape
    image2 = np.zeros((width, height, channels), dtype=np.uint8)
    image2.fill(0)

    for line in lines:
        if len(line)==1:
            x1, y1 = None, None
        else:
            if x1 == None and y1 == None:
                x1, y1 = int(line[0]), int(line[1])
            else:
                x2, y2 = int(line[0]), int(line[1])
                cv2.line(image2, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)
                x1, y1 = int(line[0]), int(line[1])
    cv2.imwrite('Image/lineImage.png', image2)



def ResizeRobotdata(data):
    yMin,yMax = -120,120
    # xMin,xmax = 235,410
    xMin, xmax = 260, 410
    xoffset = 260
    yoffset = 120

    width = xmax - xMin
    height =  yMax - yMin
    # height = 120
    lines=[]
    lines_tmp = []
    p = 10
    for x in range(1, 100, 1):
        lines = []
        lines_tmp = []
        for line in data:
            if len(line) == 1:
                lines.append(line)
            else:

                line_x, line_y =f'{int(line[0])/x:.4f}', f'{(int(line[1])*-1)/x:.4f}'
                # line_x, line_y = f'{int(line[0]) / x:.4f}', f'{int(line[1]) / x:.4f}'
                line_x = float(line_x) + xoffset
                line_y = float(line_y) + height/3
                # line_y = line_y + (yMin/3)



                # line_y = float(line_y) - (height / 4)

                line_x = float("{:.4f}".format(line_x))
                line_y = float("{:.4f}".format(line_y))
                lines.append([line_x,line_y])
                lines_tmp.append([line_x,line_y])

        numpy_array = np.array(lines_tmp)


        # Extract the x and y coordinates from the NumPy array
        x_coordinates = numpy_array[:, 0]
        y_coordinates = numpy_array[:, 1]

        # Find the maximum values of x and y
        max_x = np.max(x_coordinates)
        max_y = np.max(y_coordinates)

        if max_x < (width+xoffset) and max_y< (height-yoffset):
            break


    # line_x, line_y = arraline[:, 0] / 10, arraline[:, 1] / 10
    return lines


def ConverRobotData():
    robCSV = CSV("lineData.csv")
    data = robCSV.read_csv_file()
    convData = ResizeRobotdata(data)
    # print(convData)
    SaveRobotDataSCV(convData)
    robot = Robot(0)


    # rx,ry,rz =-5.20, 86.45, -8.64
    rx, ry, rz = -82.49, 64.88, -85.21

    # rx, ry, rz = 162.0, 85.62, 162.30
    # home =["227.00, 10.0, 90.0, 162.0, 85.62, 162.30"]
    home = ["358.25, -4.63, 137.0, -82.49, 64.88, -85.21"]
    _x = 227.00
    _y = 10.0
    z_up = 90.0
    z_up = robot.z_up
    z_down = robot.z_down
    # z_down = 78.0
    # z_down = 80.54
    # z_down = 75.08

    lines = []

    lines.append(home)
    for val in convData:

        if len(val) == 1:
            if val[0] == "0":
                _z = z_up
                line = home
                lines.append(line)
            if val[0] == "1":
                _z = z_up
                line = [f'{_x},{_y},{_z},{rx},{ry},{rz}']
                lines.append(line)

        else:
            _x = float("{:.4f}".format(val[0]))
            _y = float("{:.4f}".format(val[1]))

            if _z==z_up:
                line = [f'{_x},{_y},{_z},{rx},{ry},{rz}']
                lines.append(line)
                _z = z_down

            line = [f'{_x},{_y},{_z},{rx},{ry},{rz}']
            lines.append(line)
            # line_tmp = line




    print(lines)
    SaveAsCSVFile('roPosData.csv', lines)
    return lines

def GetRobotXY(data):
    xy = []
    for line in data:
        val = line[0].split(",")
        l =(val[0],val[1])
        xy.append(l)
    return xy

def GetRobotPos(data):
    pos = []
    for line in data:
        val = line[0].split(",")
        # l =(val[0],val[1])
        pos.append(val)
    return pos

def MoveToPenPositon():
    robot = Robot(0)
    if not robot.get_connect_status():
        robot.Connect()
    # pen_pos = ["227.00, 10.0, 75.08, 162.0, 85.62, 162.30"]
    pen_pos = robot.get_draw_pos()

    # pos = robot.get_home_pos()
    p = f'{pen_pos[0]},{pen_pos[1]},{pen_pos[2]},{pen_pos[3]},{pen_pos[4]},{pen_pos[5]}\r'
    print(p)
    position_bytes = p.encode()
    robot.SendData(position_bytes)

def MoveToPenPositon_old():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.0.1'
    server_port = 49152
    client_socket.connect((server_ip, server_port))
    home = ["227.00, 10.0, 75.08, 162.0, 85.62, 162.30"]
    p = f'{home[0]},\r'
    print(p)
    position_bytes = p.encode()
    client_socket.sendall(position_bytes)
    response = client_socket.recv(1024)
    print('Received from server:', response)
    client_socket.close()

def MoveToHomePositon():
    robot = Robot(0)
    if not robot.get_connect_status():
        robot.Connect()
    # home = ["358.25, -4.63, 137.0, -82.49, 64.88, -85.21"]
    pos = robot.get_home_pos()

    home = [f'{pos[0]},{pos[1]},{pos[2]},{pos[3]},{pos[4]},{pos[5]}']
    # home = [str(num) for num in robot.get_home_pos()]
    p = f'{home[0]},\r'
    print(p)
    position_bytes = p.encode()
    robot.SendData(position_bytes)

def MoveToHomePositon_old():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.0.1'
    server_port = 49152
    client_socket.connect((server_ip, server_port))
    home = ["358.25, -4.63, 137.0, -82.49, 64.88, -85.21"]
    p = f'{home[0]},\r'
    print(p)
    position_bytes = p.encode()
    client_socket.sendall(position_bytes)
    response = client_socket.recv(1024)
    print('Received from server:', response)
    client_socket.close()

def sendRobot(start_pos):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.0.1'
    server_port = 49152
    robdataCSV= CSV("roPosData.csv")
    lines = robdataCSV.ReadDate()
    if start_pos > 0 and start_pos < len(lines):
        # lines = robdataCSV.read_csv_file()
        client_socket.connect((server_ip, server_port))

        for i in range(start_pos,len(lines)):
            line = lines[i]
            p = f' {line[0]},\r'
            print(f' No:{i} command : {p}')
            position_bytes = p.encode()
            client_socket.sendall(position_bytes)
            response = client_socket.recv(1024)
            print('Received from server:', response)
        client_socket.close()
    # for inx,line in enumerate(lines):
    #     p = f' {line[0]},\r'
    #     print(f' No:{inx} command : {p}')
    #     position_bytes = p.encode()
    #     client_socket.sendall(position_bytes)
    #     response = client_socket.recv(1024)
    #     print('Received from server:', response)


def ShowRobotView():
    robCSV = CSV("roPosData.csv")
    data = robCSV.ReadDate()
    robot = Robot(0)
    line_int_x = []
    line_int_y = []
    z_down = robot.z_down
    for line in data:
        line[0].split(",")
        val =line[0].split(",")
        if val[2] == f"{z_down}":
            # line_int = ([int(x) for x in line])
            line_int_x.append(float(val[0]))
            line_int_y.append(float(val[1]))

    plt.plot(line_int_x, line_int_y)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot')
    plt.grid(True)
    # plt.xticks(x[::-1])
    plt.show()

def ShowRobotView_old():
    robCSV = CSV("robotData.csv")
    data = robCSV.ReadDate()
    line_int_x = []
    line_int_y = []
    for line in data:

        if len(line) > 1:
            # line_int = ([int(x) for x in line])
            line_int_x.append(float(line[0]))
            line_int_y.append(float(line[1]))

    plt.plot(line_int_x, line_int_y)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot')
    plt.grid(True)
    # plt.xticks(x[::-1])
    plt.show()

def ShowImage_1(image,size):

    for x in range(100, 0, -10):
        scale_percent = x  # percent of original size

        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)

        if size[0] > width and size[1] > height:
            break

    size = (width, height)
    # h, w = frame.shape[:2]
    # image = QImage(frame.flatten(), w, h, QImage.Format_RGB888)  # cv::Mat -> Qt(numpy.array)
    resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
    h, w = resized.shape[:2]

    image = QImage(resized.flatten(), w, h, QImage.Format_RGB888)  # cv::Mat -> Qt(numpy.array)
    return image

def PrintRobot(xzy):
    pass
