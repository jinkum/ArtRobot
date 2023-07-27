# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowdvoQcY.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1173, 743)
        MainWindow.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1200, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QSize(16777215, 500))
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.img_Color = QLabel(self.widget_3)
        self.img_Color.setObjectName(u"img_Color")
        sizePolicy.setHeightForWidth(self.img_Color.sizePolicy().hasHeightForWidth())
        self.img_Color.setSizePolicy(sizePolicy)
        self.img_Color.setMaximumSize(QSize(16777215, 500))
        self.img_Color.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.img_Color)

        self.img_line = QLabel(self.widget_3)
        self.img_line.setObjectName(u"img_line")
        sizePolicy.setHeightForWidth(self.img_line.sizePolicy().hasHeightForWidth())
        self.img_line.setSizePolicy(sizePolicy)
        self.img_line.setMaximumSize(QSize(16777215, 500))
        self.img_line.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.img_line)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.but_loadImage = QPushButton(self.widget_2)
        self.but_loadImage.setObjectName(u"but_loadImage")
        icon = QIcon()
        icon.addFile(u"Icons/upload_file_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_loadImage.setIcon(icon)
        self.but_loadImage.setIconSize(QSize(24, 24))
        self.but_loadImage.setCheckable(False)
        self.but_loadImage.setFlat(True)

        self.horizontalLayout_3.addWidget(self.but_loadImage)

        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.widget_12)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_11.addWidget(self.label_2)

        self.txt_blur = QLineEdit(self.widget_12)
        self.txt_blur.setObjectName(u"txt_blur")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_blur.sizePolicy().hasHeightForWidth())
        self.txt_blur.setSizePolicy(sizePolicy2)
        self.txt_blur.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_11.addWidget(self.txt_blur)


        self.horizontalLayout_3.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_2)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.horizontalLayout_3.addWidget(self.widget_13)

        self.line_6 = QFrame(self.widget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.but_conver = QPushButton(self.widget_2)
        self.but_conver.setObjectName(u"but_conver")
        icon1 = QIcon()
        icon1.addFile(u"Icons/autorenew_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_conver.setIcon(icon1)
        self.but_conver.setIconSize(QSize(24, 24))
        self.but_conver.setCheckable(False)
        self.but_conver.setFlat(True)

        self.horizontalLayout_3.addWidget(self.but_conver)

        self.line_7 = QFrame(self.widget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_7)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget_4)

        self.line_11 = QFrame(self.widget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_11)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_4 = QFrame(self.widget_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.but_camera = QPushButton(self.widget_7)
        self.but_camera.setObjectName(u"but_camera")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.but_camera.sizePolicy().hasHeightForWidth())
        self.but_camera.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u"Icons/photo_camera_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_camera.setIcon(icon2)
        self.but_camera.setIconSize(QSize(24, 24))
        self.but_camera.setFlat(True)

        self.horizontalLayout_5.addWidget(self.but_camera)

        self.line_10 = QFrame(self.widget_7)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_10)

        self.label_camera = QLabel(self.widget_7)
        self.label_camera.setObjectName(u"label_camera")
        sizePolicy.setHeightForWidth(self.label_camera.sizePolicy().hasHeightForWidth())
        self.label_camera.setSizePolicy(sizePolicy)
        self.label_camera.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_camera)

        self.line_8 = QFrame(self.widget_7)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_8)

        self.but_cap = QPushButton(self.widget_7)
        self.but_cap.setObjectName(u"but_cap")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.but_cap.sizePolicy().hasHeightForWidth())
        self.but_cap.setSizePolicy(sizePolicy4)
        icon3 = QIcon()
        icon3.addFile(u"Icons/lens_blur_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_cap.setIcon(icon3)
        self.but_cap.setIconSize(QSize(24, 24))
        self.but_cap.setFlat(True)

        self.horizontalLayout_5.addWidget(self.but_cap)

        self.line_9 = QFrame(self.widget_7)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_9)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.line_12 = QFrame(self.widget_6)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_12)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(500, 500))
        self.verticalLayout_2 = QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy5)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.but_home = QPushButton(self.widget_11)
        self.but_home.setObjectName(u"but_home")
        self.but_home.setMaximumSize(QSize(100, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"Icons/home_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_home.setIcon(icon4)
        self.but_home.setIconSize(QSize(24, 24))
        self.but_home.setCheckable(False)
        self.but_home.setFlat(True)

        self.horizontalLayout_6.addWidget(self.but_home)

        self.line_2 = QFrame(self.widget_11)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)

        self.but_pen = QPushButton(self.widget_11)
        self.but_pen.setObjectName(u"but_pen")
        self.but_pen.setMaximumSize(QSize(100, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"Icons/format_ink_highlighter_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_pen.setIcon(icon5)
        self.but_pen.setIconSize(QSize(24, 24))
        self.but_pen.setCheckable(False)
        self.but_pen.setFlat(True)

        self.horizontalLayout_6.addWidget(self.but_pen)

        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.line = QFrame(self.widget_11)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.widget_5 = QWidget(self.widget_11)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.but_play = QPushButton(self.widget_5)
        self.but_play.setObjectName(u"but_play")
        self.but_play.setMaximumSize(QSize(100, 16777215))
        icon6 = QIcon()
        icon6.addFile(u"Icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_play.setIcon(icon6)
        self.but_play.setIconSize(QSize(24, 24))
        self.but_play.setCheckable(False)
        self.but_play.setFlat(True)

        self.horizontalLayout_7.addWidget(self.but_play)

        self.but_stop = QPushButton(self.widget_5)
        self.but_stop.setObjectName(u"but_stop")
        self.but_stop.setMaximumSize(QSize(100, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"Icons/stop_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_stop.setIcon(icon7)
        self.but_stop.setIconSize(QSize(24, 24))
        self.but_stop.setCheckable(False)
        self.but_stop.setFlat(True)

        self.horizontalLayout_7.addWidget(self.but_stop)

        self.txt_startPos = QLineEdit(self.widget_5)
        self.txt_startPos.setObjectName(u"txt_startPos")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txt_startPos.sizePolicy().hasHeightForWidth())
        self.txt_startPos.setSizePolicy(sizePolicy6)
        self.txt_startPos.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.txt_startPos.setFrame(False)

        self.horizontalLayout_7.addWidget(self.txt_startPos)


        self.horizontalLayout_6.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_11)

        self.line_13 = QFrame(self.widget_8)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_13)

        self.tableView = QTableView(self.widget_8)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"gridline-color: rgb(91, 91, 91);")
        self.tableView.setFrameShadow(QFrame.Sunken)
        self.tableView.verticalHeader().setVisible(True)
        self.tableView.verticalHeader().setMinimumSectionSize(15)
        self.tableView.verticalHeader().setDefaultSectionSize(24)

        self.verticalLayout_2.addWidget(self.tableView)

        self.line_14 = QFrame(self.widget_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_14)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy5.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy5)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.but_robotView = QPushButton(self.widget_9)
        self.but_robotView.setObjectName(u"but_robotView")
        self.but_robotView.setMaximumSize(QSize(100, 16777215))
        icon8 = QIcon()
        icon8.addFile(u"Icons/visibility_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.but_robotView.setIcon(icon8)
        self.but_robotView.setIconSize(QSize(24, 24))
        self.but_robotView.setCheckable(False)
        self.but_robotView.setFlat(True)

        self.horizontalLayout_8.addWidget(self.but_robotView)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_LineCount = QLabel(self.widget_10)
        self.label_LineCount.setObjectName(u"label_LineCount")

        self.horizontalLayout_9.addWidget(self.label_LineCount)

        self.progressBar = QProgressBar(self.widget_10)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_9.addWidget(self.progressBar)


        self.horizontalLayout_8.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.horizontalLayout_4.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget_6)


        self.horizontalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image ", None))
        self.img_Color.setText("")
        self.img_line.setText("")
        self.but_loadImage.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.txt_blur.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.but_conver.setText(QCoreApplication.translate("MainWindow", u"Conver to Line Image", None))
        self.but_camera.setText("")
        self.label_camera.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.but_cap.setText("")
        self.but_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.but_pen.setText(QCoreApplication.translate("MainWindow", u"Pen Position", None))
        self.label.setText("")
        self.but_play.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.but_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.txt_startPos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.but_robotView.setText("")
        self.label_LineCount.setText(QCoreApplication.translate("MainWindow", u"20000/1", None))
    # retranslateUi

