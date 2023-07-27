import sys

import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore,QtWidgets,QtUiTools
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
# from ui_main import Ui_MainWindow
from ui_main_window import Ui_MainWindow
from ui_robotView import Ui_Form
# import ui_robotView
import pandas as pd
import os
from CoreModule import ImageCore ,INIFile
import CoreModule
from CoreModule import Camera
from PIL import Image
import matplotlib.pyplot as plt

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])






class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.UIWindow = QMainWindow()



        self.ui = Ui_MainWindow()
        self.ui_Robotview = Ui_Form()
        self.ui_Robotview.setupUi(self)
        self.ui.setupUi(self)


        self.ImageFunctions = ImageCore()
        self.ui.but_loadImage.clicked.connect(self.load_image_click)
        self.ui.but_conver.clicked.connect(self.conver_image_click)
        self.ui.but_play.clicked.connect(self.play_click)
        self.ui.but_stop.clicked.connect(self.stop_click)
        self.ui.but_robotView.clicked.connect(self.showRobotViewWindow)
        self.ui.but_pen.clicked.connect(self.MoveToPen_click)
        self.ui.but_home.clicked.connect(self.MoveToHome_click)
        self.ui.but_camera.clicked.connect(self.Camera_click)
        self.ui.but_cap.clicked.connect(self.Capture_click)

        self.ui.but_cap.setDisabled(True)
        self.ui.but_home.setDisabled(True)
        self.ui.but_pen.setDisabled(True)
        self.ui.but_play.setDisabled(True)
        self.ui.but_stop.setDisabled(True)
        self.ui.but_robotView.setDisabled(True)

        self.ui.label_LineCount.setText("0/0")
        self.ui.progressBar.setValue(0)


        self.ui.tableView.setStyleSheet('''
    ::section {
        background-color: rgb(71, 71, 71);;
        border-style: flat;
        padding: 0px 5px;
        }''')
        self.imagePath =""
        self.Config()

        self.CamarStatus = False

        self.timer = QTimer(self)
        # self.timer.timeout.connect(self.test)
        self.camera = Camera(self.ui.label_camera)
        self.robot = CoreModule.Robot(0)






    def Config(self):

        self.setting_INI = INIFile('setting.ini')
        self.currentImagePath = self.setting_INI.read('USER', 'PATH')
        self.IMAGE_Path = self.setting_INI.read('IMAGE_SECTION', 'IMAGE_Path')



    def setpayIcon(self):
        if self.ui.but_play.text() =="Start":
            self.ui.but_play.setText("Pause")
            self.ui.but_play.setIcon(QIcon("Icons/pause_circle_FILL0_wght400_GRAD0_opsz48.svg"))
        else:
            self.ui.but_play.setText("Start")
            self.ui.but_play.setIcon(QIcon("Icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg"))

    def load_image_click(self):
        print("Loading image clicked")

        self.imagePath = CoreModule.LoadImage(self.currentImagePath)
        if self.imagePath !="":
            CoreModule.ShowImage(self.imagePath,self.ui.img_Color)

            self.ResetConvert()

    def ResetConvert(self):
        self.ui.img_line.clear()
        self.ui.tableView.reset()
        self.DisableRobotControls(True)

    def DisableRobotControls(self,status = True):
        self.ui.but_home.setDisabled(status)
        self.ui.but_pen.setDisabled(status)
        self.ui.but_play.setDisabled(status)
        self.ui.but_stop.setDisabled(status)
        self.ui.but_robotView.setDisabled(status)



    def setHomePos(self,data):
        numpy_array = np.array(data)
        x_coordinates = numpy_array[:, 0]
        y_coordinates = numpy_array[:, 1]
        x_float = [float(value.strip()) for value in x_coordinates]
        y_float = [float(value.strip()) for value in y_coordinates]
        # Find the minum values of x and y
        min_x = np.min(x_float)
        min_y = np.min(y_float)

        # Find the maximum values of x and y
        max_x = np.max(x_float)
        max_y = np.max(y_float)

        x = min_x + (max_x-min_x)/2

        y = min_y + (max_y-min_y)/2
        cpos = self.robot.get_home_pos()
        cpos[0] = float("{:.4f}".format(x))
        cpos[1] = float("{:.4f}".format(y))
        self.robot.set_home_pos(cpos)

    def ResetRobotTabs(self):
        self.DisableRobotControls(False)
        self.ui.txt_startPos.setText("0")
        self.robot.set_status_value(0)

        self.ui.but_stop.setDisabled(True)
        self.ui.but_play.setText("Start")
        self.ui.but_play.setIcon(QIcon("Icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg"))


    def conver_image_click(self):
        print("conver image clicked")
        if self.imagePath !="":

            self.ResetRobotTabs()
            blur_val = self.ui.txt_blur.text()
            if blur_val == "" : blur_val = 0

            data = CoreModule.ConverLineImage(self.imagePath,blur=int(blur_val))
            CoreModule.SaveLineDataSCV(data)
            CoreModule.CreateLineImage(self.imagePath,data)
            CoreModule.ShowImage("Image/lineImage.png", self.ui.img_line)
            robotData = CoreModule.ConverRobotData()
            # CoreModule.SaveRobotPosSCV(robotData)
            xy = CoreModule.GetRobotXY(robotData)
            pos = CoreModule.GetRobotPos(robotData)

            self.setHomePos(pos)
            self.tableview(pos)
            # CoreModule.ShowRobotView(data)



    def Camera_click(self):
        print("CameraClick")
        if self.CamarStatus:
            self.CamarStatus = False
            self.ui.but_cap.setDisabled(True)
            self.timer.stop()
            self.ui.label_camera.clear()
        else:
            self.CamarStatus =True
            self.ui.but_cap.setDisabled(False)

            self.camera.setup_camera()
            self.timer.timeout.connect(self.camera.display_video_stream)
            # self.timer.start(1000)
            self.timer.start(30)

    def Capture_click(self):
        print("Capture Click")
        self.imagePath = self.camera.CaptureImage()
        CoreModule.ShowImage(self.imagePath, self.ui.img_Color)

    def MoveToPen_click(self):
        CoreModule.MoveToPenPositon()

    def MoveToHome_click(self):
        CoreModule.MoveToHomePositon()

    def update_progress(self, value):
        # Update the progress bar with the current value
        self.ui.progressBar.setValue(value)

    def play_click(self):
        print("play clicked")

        if self.ui.but_play.text() !="Pause":
            self.ui.but_play.setText("Pause")
            self.ui.but_play.setIcon(QIcon("Icons/pause_circle_FILL0_wght400_GRAD0_opsz48.svg"))

            self.Play()

        else:
            self.ui.but_play.setText("Continue")
            self.ui.but_play.setIcon(QIcon("Icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg"))
            self.StarLineNo = int(self.ui.txt_startPos.text())
            self.Pause()


        # self.setpayIcon()

        # self.StarLineNo = int(self.ui.txt_startPos.text())
        # CoreModule.sendRobot(self.StarLineNo)
        # self.setpayIcon()

        # self.Play()



    def Play(self):
        if self.robot.get_status_value()!= 3:
            self.StarLineNo = int(self.ui.txt_startPos.text())
            self.robot.set_line_value(self.StarLineNo)
        else:
            pass
        self.ui.but_stop.setDisabled(False)
        linecount_Obj = self.ui.label_LineCount

        self.background_task = CoreModule.BackgroundTask()
        # self.background_task.ProgressBarSetup(self.ui.progressBar)
        self.background_task.finished.connect(self.onBackgroundTaskFinished)
        # self.background_task.signals.progress.connect(self.update_progress)
        self.background_task.start()

    @Slot()
    def onBackgroundTaskFinished(self):
        # self.robot.set_status_value
        # CoreModule.MoveToHomePositon()
        print("Background task is finished!")
        # self.label.setText("Background task is finished!")

    def Pause(self):
        self.robot.set_status_value(3)

    def stop_click(self):
        print("stop clicked")

        self.robot.set_status_value(4)

        self.ui.but_stop.setDisabled(True)
        self.ui.but_play.setText("Start")
        self.ui.but_play.setIcon(QIcon("Icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg"))

    def tableview(self,data):
        self.table = self.ui.tableView
        data = pd.DataFrame(data,columns = ['X', 'Y' ,'Z','RX', 'RY' ,'RZ' ])

        self.model = TableModel(data)
        self.table.setModel(self.model)


    def showRobotViewWindow(self):
        print("show RobotView Window")
        CoreModule.ShowRobotView()
        # x =[]
        # y =[]
        #
        # for i in range(self.model.rowCount(None)):
        #
        #     index_x = self.model.index(i, 0)
        #     index_y = self.model.index(i, 1)
        #     data_x = self.model.data(index_x, Qt.DisplayRole)
        #     data_y = self.model.data(index_y, Qt.DisplayRole)
        #
        #     x.append(data_x)
        #     y.append(data_y)
        #
        # plt.plot(x, y)
        #
        # # plt.plot(x, y)
        # #
        # plt.xlabel('Y-axis')
        # plt.ylabel('X-axis')
        # plt.title('Line Plot')
        # plt.grid(True)
        # # plt.xticks(x[::-1])
        # plt.show()
        # #











if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())