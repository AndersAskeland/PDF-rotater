# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 786)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_logo = QFrame(self.frame_3)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMaximumSize(QSize(100, 16777215))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_logo)

        self.label_logo = QLabel(self.frame_3)
        self.label_logo.setObjectName(u"label_logo")

        self.horizontalLayout_2.addWidget(self.label_logo)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_tree_files = QLabel(self.frame_4)
        self.label_tree_files.setObjectName(u"label_tree_files")

        self.verticalLayout_2.addWidget(self.label_tree_files)

        self.tree_files = QTreeWidget(self.frame_4)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_files.setHeaderItem(__qtreewidgetitem)
        self.tree_files.setObjectName(u"tree_files")

        self.verticalLayout_2.addWidget(self.tree_files)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_page_previous = QPushButton(self.frame_6)
        self.btn_page_previous.setObjectName(u"btn_page_previous")

        self.horizontalLayout_3.addWidget(self.btn_page_previous)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btn_page_next = QPushButton(self.frame_6)
        self.btn_page_next.setObjectName(u"btn_page_next")

        self.horizontalLayout_3.addWidget(self.btn_page_next)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, -1, 100, -1)
        self.graphicsView_pdf = QGraphicsView(self.frame_7)
        self.graphicsView_pdf.setObjectName(u"graphicsView_pdf")

        self.verticalLayout_4.addWidget(self.graphicsView_pdf)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_rotate_left = QPushButton(self.frame_8)
        self.btn_rotate_left.setObjectName(u"btn_rotate_left")

        self.horizontalLayout_4.addWidget(self.btn_rotate_left)

        self.btn_rotate_right = QPushButton(self.frame_8)
        self.btn_rotate_right.setObjectName(u"btn_rotate_right")

        self.horizontalLayout_4.addWidget(self.btn_rotate_right)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"PDF rotater\n"
"A simple PDF rotater using ****. PDF \n"
"state is automatically saved.", None))
        self.label_tree_files.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_page_previous.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Page * / *", None))
        self.btn_page_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btn_rotate_left.setText(QCoreApplication.translate("MainWindow", u"Rotate left", None))
        self.btn_rotate_right.setText(QCoreApplication.translate("MainWindow", u"Rotate right", None))
    # retranslateUi

